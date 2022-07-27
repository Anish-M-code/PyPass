
import os
import sqlite3
import getpass
import platform
import webbrowser
import csv
import time
import sys

try:
    import passwordsgo.pysecret as p
except ImportError:
    print(" Critical Error : Required Modules Not Found !!!")

# encrypts a given string and key and returns ciphertext
def en(msg, salt):
    ciphertxt = []
    if len(msg) < len(salt):
        msg = msg + '0' * (len(salt) - len(msg)) 
    x = p.f(msg)
    y = salt
    y = p.f(y)
    if len(x) <= len(y):
        for i in range(len(x)):
            if type(x[i]) is int and type(y[i]) is int:
                ciphertxt.append(((x[i] + y[i]) % len(p.A)))
            else:
                ciphertxt.append(' ')
    else:
        x = input(' Press any key to continue...')
        sys.exit(1)
    ciphertxt = tuple(ciphertxt)
    ctxt = p.rf(ciphertxt)
    return ctxt

def valid_db(db):
    if db.endswith('.cry'):
        return db
    return db+'.cry'

def check(db):
    if os.path.exists(db) is False:
        print('\n Database doesnot exist!!!\n')
        return False
        
def init():
    if os.path.exists('PyPassDB') is False:
       os.mkdir('PyPassDB')
    os.chdir('PyPassDB')

def cls():
    os.system("cls" if platform.system().lower() == "windows" else "clear" )

def pause():
    p.wait()
        
def task_start():
    p.start()

def task_end():
    p.end()

def task_fail():
    p.tskf()

def generate_key(msg):
    c_msg = len(msg) / 32
    msg = len(msg) // 32
    if c_msg > msg:
        msg += 1
    key = p.ikey('0' * msg * 32)
    key = p.rf(key)
    return key

        

def create_masterpassword(db):
    db = valid_db(db)
    while 1:

        while 1:
             mpassword1 = getpass.getpass(" Create Master Password:")

             if len(mpassword1) > 9 :
                 break
             else:
                 print(" The Password must be atleast 10 characters long.\n")

        mpassword2 = getpass.getpass(" Re-enter Master Password:")
        if mpassword1 == mpassword2:
            if os.path.exists("masterpassword.db") is False:
                connect = sqlite3.connect("masterpassword.db")
                cursor = connect.cursor()
                cursor.execute('''create table map ( 
                        database varchar(250) primary key ,
                        password varchar(2000) not null 
                        )''')
                cursor.execute('insert into map values (?, ?)', (db, generate_key(mpassword1)))
                connect.commit()
                cursor.close()
                connect.close()
            else:
                connect = sqlite3.connect("masterpassword.db")
                cursor = connect.cursor()
                cursor.execute('insert into map values(?, ?)', (db, generate_key(mpassword1)))
                connect.commit()
                cursor.close()
                connect.close()
            
            break
        else:
            print(" Passwords Not Matching Try Again !!!\n")
    

def get_masterpassword(db):
    db = valid_db(db)
    try:
        connect = sqlite3.connect('masterpassword.db')
        cursor = connect.cursor()
        return cursor.execute('select password from map where database=?', (db,)).fetchall()[0][0]
    except Exception as e:
        print("masterpassword.db file is corrupted!!!\n")

def create_database(db):
    db = valid_db(db)
    task_start()
    
    if os.path.exists(db):
        print(" Database Already Exists !!!")
        task_fail()
        return 1

    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    cursor.execute('''create table passwordb ( 
                        account varchar(250) primary key ,
                        username varchar(250) not null ,
                        password varchar(2000),
                        website varchar(250)
                        )''')
    
    create_masterpassword(db)
    connect.commit()
    cursor.close()
    connect.close()
    task_end()

def delete_database(db, mode = 'n'):
    db = valid_db(db)
    task_start()
    if mode == 'n':
        connect = sqlite3.connect('masterpassword.db')
        Cursor = connect.cursor()
        Cursor.execute('delete from map where database=?', (db,))
        connect.commit()
        Cursor.close()
        connect.close()

    if os.path.exists(db):
        os.remove(db)
        print(' Database Deleted successfully.')
        task_end()
        return
    print("\n Database Not Found!\n")
    task_fail()

def create_account(db, account, username, website):
    db = valid_db(db)
    if check(db) is False:
        return 
    task_start()
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    try:
        masterpassword = get_masterpassword(db)
        password = generate_key(masterpassword)
        cursor.execute("insert into passwordb values(?, ?, ?, ?)",(account, username, password, website))
        print(' Account created successfully!')
    except Exception as e:
        print(" Invalid Data ;( ")
        task_fail()
        return

    connect.commit()
    cursor.close()
    connect.close()
    task_end()

def modify_account(db, account, username):
    db = valid_db(db)
    if check(db) is False:
        return
    task_start()
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    masterpassword = get_masterpassword(db)
    password = generate_key(masterpassword)

    try:
        x = cursor.execute("select website from passwordb where account=? and username=?", (account, username)).fetchall()
        if len(x) == 0:
            print(" No such Entry Exists in Database!!!")
            task_end()
            return
    except Exception as e:
        print(" Invalid Data!!!")
        task_end()
        return 
    
    cursor.execute("update passwordb set password=? where account=? and username=?", (password, account, username))
    print(' New Password generated successfully!') 
    connect.commit()
    cursor.close()
    connect.close()
    task_end()

def delete_account(db, account, username):
    db = valid_db(db)
    if check(db) is False:
        return
    task_start()
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    try:
        x = cursor.execute("select website from passwordb where account=? and username=?", (account, username)).fetchall()
        if len(x) == 0:
            print(" No such Entry Exists in Database!!!")
            task_end()
            return
    except Exception as e:
        print(" Invalid Data!!!")
        task_end()
        return 
    
    cursor.execute("delete from passwordb where account=? and username=?", (account, username))
    print(' Deleted Account Successfully!')
    connect.commit()
    cursor.close()
    connect.close()
    task_end()

def view_accounts(db):
    db = valid_db(db)
    if check(db) is False:
        return
    print()
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    
    try:
        accountlist = cursor.execute("select account , username from passwordb ").fetchall()
    except Exception as e:
        print(" Invalid Data Entered!!!")
        return
    
    try:
        maxrecordlength = len(accountlist[0][0])
    except IndexError:
        print(' No Accounts Found!')
        return
    for record in accountlist:
        if len(record[0]) > maxrecordlength :
            maxrecordlength = len(record[0]) 
    
    print(' Accounts' + '     ' + ' ' * (maxrecordlength - 8) + 'Usernames')
    print(' --------' + '     ' + ' ' * (maxrecordlength - 8) + '---------')

    for record in accountlist:
        print(' ' + record[0] + '         ' + ' ' * (maxrecordlength - len(record[0])) + record[1])
    cursor.close()
    connect.close()
    print()

def view_databases():
    dbcount = 0
    print("\n List of Available Databases")
    print(" ---- -- --------- ---------\n")
    filedetected = False

    try:
        connect = sqlite3.connect('masterpassword.db')
        cursor = connect.cursor()
        database = cursor.execute('select database from map').fetchall()
        cursor.close()
        connect.close()
    except Exception as e:
        print(' No Database Found!!!')

    if len(database) == 0:
        print(" No Database Found!!!")
        return

    for entry in database:
        dbcount += 1
        print(' ', entry[0])

    print('\n Total databases Found:', dbcount)

def view_account(db,account):
    db = valid_db(db)
    if check(db) is False:
        return
    task_start()
    masterpassword = getpass.getpass(' Enter Master Password:')
    masterkey = get_masterpassword(db)
    masterkey = en(masterpassword,masterkey)
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    try:
        output = cursor.execute("select account ,username , password , website from passwordb where account=?  ", (account,)).fetchall()
        print(' Account:', output[0][0])
        print(' Username:', output[0][1])
        
        if output[0][3].lower() != 'null':
            print(' Website:', output[0][3])

        print('\n Generated Password:-\n', en(output[0][2], masterkey))

        if output[0][3].lower() != 'null':
            choice = input('\n Do you want to open website in Browser?(Y/N):')
            if choice.lower() == 'y':
                webbrowser.open(output[0][3])
        task_end()
    except:
        print(" Invalid Data supplied!")
        task_fail()
    cursor.close()
    connect.close()

def export(db):
    db = valid_db(db)
    task_start()
    if check(db) is False:
        task_fail()
        return
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    os.chdir('..')
    with open((db[:-4] + '.csv'), 'w', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(cursor.execute('select * from passwordb').fetchall())
    cursor.close()
    connect.close()
    os.chdir('PyPassDB')
    print('Generating Cryptographic Tokens...')
    time.sleep(5)
    print('Here is your Secret Token:\n')
    print(get_masterpassword(db))
    print('\nPlease store the above Token Securely, All data will be lost if it is lost...')
    task_end()

def importt(db):
    db = valid_db(db)
    task_start()
    file = input(' Enter csv file to import:')
    if os.path.exists(file) is False:
        print('File Not Found!')
        task_fail()
        sys.exit(1)
    password = getpass.getpass(' Enter Secret Token:')
    if len(password)%32 != 0:
        print('\n\a Invalid Token!!!')
        task_fail()
        return
    if os.path.exists('masterpassword.db') is False:
        connect = sqlite3.connect("masterpassword.db")
        cursor = connect.cursor()
        cursor.execute('''create table map ( 
                        database varchar(250) primary key ,
                        password varchar(2000) not null 
                        )''')
        try:
            cursor.execute('insert into map values (?,?)', (db, password))
            connect.commit()
        except Exception as e:
            print(" Database with same name Already Exists")
            task_fail()
            return
        finally:
            cursor.close()
            connect.close()

    else:
        connect = sqlite3.connect('masterpassword.db')
        cursor = connect.cursor()
        try:
            cursor.execute('insert into map values(?,?)', (db, password))
            connect.commit()
        except Exception as e:
            print(" Database with same name Already Exists")
            task_fail()
            return
        finally:
            cursor.close()
            connect.close()
    
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    cursor.execute('''create table passwordb ( 
                        account varchar(250) primary key ,
                        username varchar(250) not null ,
                        password varchar(2000),
                        website varchar(250)
                        )''')
    
    os.chdir('..')
    try:
        with open(file, newline = '') as csvfile:
            reader = csv.reader(csvfile, dialect = 'excel')
            for line in reader:
                cursor.execute('insert into passwordb values(?,?,?,?)', (line[0], line[1], line[2], line[3]))
    except Exception as e:
        print(e)
        sys.exit(1)
    os.chdir('PyPassDB')
    connect.commit()
    cursor.close()
    connect.close()
    task_end()

def set_charset():

    cls()
    print('\n     === PyPass Password Manager v4.1 ===')
    print("\n Select Symbols to be used for password generation")
    print(" -------------------------------------------------\n")
    print('\n1) Use Capital letters + small letters + numbers + symbols')
    print('2) Use Alphabets + Numbers')
    print('3) Use Numbers')
    print('4) Custom Range')

    while 1:
        choice = input('\nEnter choice:')
        if choice == '1':
            break

        elif choice == '2':
            p.A = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','o','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9')
            break
        
        elif choice == '3':
            p.A = ('0','1','2','3','4','5','6','7','8','9')
            break

        elif choice == '4':
            file = input('\n\nEnter File containing characterset :')
            os.chdir("..")
            fil = ''
            try:
                with open(file,'r') as f:
                    fil = f.read().strip()
                
                p.A = []
                for i in fil:
                    p.A.append(i)
                
                p.A = tuple(p.A)

                os.chdir('PyPassDB')
            except FileNotFoundError as e:
                print('File Not Found!')
                time.sleep(3)
                sys.exit(1)
            break
            
        print('Please enter valid choice! Either 1 or 2 or 3 or 4')
    cls()     
