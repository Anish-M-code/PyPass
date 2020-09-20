
# PyPass
# Copyright (C) 2018-2020 M.Anish <aneesh25861@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

''' This is a simple Password Manager Developed in Python by M.Anish only. '''

dbpass=0
unlockedkey=0

try:
     import os
     import platform
     import pysecret as p
     import getpass
     import csv
except ImportError:
    print(' Critical Error: Required Modules Not found!\n')
    x=input(' Press any key to continue...')
    exit(1)

def release():
    os.chdir('..')
    
def genkey(msg,file):
    if os.path.exists(file)==False:
     key=p.ikey(msg)
     key=p.rf(key)
     with open(file,'w') as f:
         f.write(key)
 
def load():
  global dbpass
  global unlockedkey
  db=input('\n Enter Database Name:')
  if os.path.exists(db):
     if os.path.isdir(db):
        os.chdir(db)
  else:
     x=input(' Entered Database not Found!\nPress any key to continue...')
     exit(1)
     return  
  dbpass=getpass.getpass(' Enter Master Password:')
  genkey(dbpass,'masterkey')
  unlockedkey=en(dbpass,'masterkey')
  dbpass=0
  
  
  
#encrypts a given string and returns ciphertxt and key as a tuple. (no file generated!)
def en(msg,file):
    ciphertxt=[]
    x=p.f(msg)
    with open(file,'r') as f:
      y=f.read()
      y=p.f(y)
    if len(x)<=len(y):
        for i in range(len(x)):
            if type(x[i])==int and type(y[i])==int:
                ciphertxt.append(((x[i]+y[i])%36))
            else:
                ciphertxt.append(' ')
    else:
        x=input(' Press any key to continue...')
        exit(1)
    ciphertxt=tuple(ciphertxt)
    ctxt=p.rf(ciphertxt)
    return ctxt

         
def cls():
    if platform.system().lower()=='windows':
     os.system('cls')
    else:
     os.system('clear')

def rm(x):
    if platform.system().lower()=='windows':
       os.system('rmdir /s '+x)
    else:
       os.system('rm -rf '+x)
    
def pause():
    x=input('\n Press any key to continue...\n')
    
def start():
    p.start()
    
def end():
    p.end()
    
def init():
    if os.path.exists('PyPassDB')==False:
       os.mkdir('PyPassDB')
    os.chdir('PyPassDB')
    

def createdb():
    start()
    db=input(' Enter Database Name:')
    if os.path.exists(db)==False:
       os.mkdir(db)
       end()
    else:
       print('\n\a Task Failed!...\n')
    

def createac():
    start()
    ac=input(' Enter Account Name:')
    if os.path.exists(ac):
      print('\n Account Already exists!')
      p.tskf()
      os.chdir('..')
      pause()
    else:          
      genkey(unlockedkey,ac)
      os.chdir('..')
      end()
            
    
    
def viewdb():
    start()
    print('     === List of Available Databases ===\n')
    if len(os.listdir())==0:
       print('\n No Database Found!\n')
       end()
    else:
       for i in os.listdir():
         print(' '+i)
       end()
           

def viewac():
    start()
    print('      === List of Accounts ===\n')
    if len(os.listdir())==0:
       print('\n No Accounts Found!\n')
    else:
       for i in os.listdir():
         print(' '+i)
    os.chdir('..')
    end()
    
def importt():
  os.chdir('..')
  file=input(' Enter File to be imported:')
  try:
   db=file[:file.index('.')]
  except:
   print('Invalid Filename!!!')
   p.tskf()
  try:
   with open(file) as f:
     os.chdir('PyPassDB')
     if os.path.exists(db)==False:
       os.mkdir(db)
       os.chdir(db)
     else:
       os.chdir(db)
     csv_r=csv.reader(f)
     for i in csv_r:
        with open(i[0],'w') as w:
          w.write(i[1])
   os.chdir('..')
   end()
  except:
        p.tskf()
        pause()
        exit(1)
        
def export():
    store=dict()
    start()
    db=input(' Enter database name:')
    if os.path.exists(db):
       os.chdir(db)
       for i in os.listdir():
         if os.path.isfile(i):
            with open(i) as f:
              store[i]=f.read()
       os.chdir('..')
       os.chdir('..')
    try:
     with open(db+'.csv','w') as f:
        csv_r=csv.writer(f)
        for i in store:
            csv_r.writerow(list((i,store[i])))
     os.chdir('PyPassDB')
     end()
    except:
        p.tskf()
    
def deldb():
    start()
    db=input(' Enter database name:')
    if os.path.exists(db):
       rm(db)
       end()
    else:
       print('\n Entered Database Not Found!')
       p.tskf()
           
def delac():
    start()
    db=input(' Enter Account name:')
    if os.path.exists(db):
       os.remove(db)
       end()
    else:
       print(' Entered Account Not Found!')
       p.tskf()
    os.chdir('..')
    
def modac():
    start()
    ac=input(' Enter Account name:')
    if os.path.exists(ac):
       os.remove(ac)
    else:
       print(' Entered Account Not Found!')
       p.tskf()
       return        
    genkey(unlockedkey,ac)
    os.chdir('..')
    end()
    
def display():
    start()
    y=0
    db=input(' Enter Account name:')
    if os.path.exists(db)==False:
       print(' Entered Account Not Found!')
       p.tskf()
       return
    print(' Password:',en(unlockedkey,db))
    os.chdir('..')
    end()
    
    