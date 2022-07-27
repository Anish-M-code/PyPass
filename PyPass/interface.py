
'''
This Python module contains menu interfaces for PyPass project.
Developed by M.Anish only.
'''

# variable to mark if check is done to verify PyPassDB folder is present or not,
#  0 check not done , 1 means check done.
lock = 0

try:
    import os
    import sys
    import passwordsgo.pysecret as s
    import passwordsgo.functions as f
except ImportError:
    print(' Critical Error: Required Modules Not found!\n')
    x = input(' Press any key to continue...')
    sys.exit(1)

# Prints user interface for Database Manager.
def mandb(db):
   db = f.valid_db(db)
   if f.check(db) is False:
      return 
   f.cls()
   print('\n     === PyPass DB Manager Menu ===')
   print('\n 1)Create Account\n 2)View Accounts\n 3)Display Account\n 4)Delete Account\n 5)Modify Account')
   x = input('\n Enter choice:')
   if x == '1':
      account = input('\n Enter Account Name:')
      username = input('\n Enter Username:')
      website = input('\n Enter Website:')
      f.create_account(db, account, username, website)
      f.pause()
      f.cls()
      mandb(db)
     
   elif x == '2':
      f.view_accounts(db)
      f.pause()
      f.cls()
      mandb(db)
     
   elif x == '3':
      account = input('\n Enter Account Name:')
      f.view_account(db, account)
      f.pause()
      f.cls()
      mandb(db)
     
   elif x == '4':
      account = input('\n Enter Account Name:')
      username = input('\n Enter Username:')
      f.delete_account(db, account, username)
      f.pause()
      f.cls()
      mandb(db)

   elif x == '5':
      account = input('\n Enter Account Name:')
      username = input('\n Enter Username:')
      f.modify_account(db, account, username)
      f.pause()
      f.cls()
      mandb(db)

   elif x.lower() == 'c':
      sys.exit()
   elif x.lower() == 'mm':
      main()
  
   else:
      print('\n Please enter a valid choice from 1,2,3,4 or 5\n')
      f.pause()
      f.cls()
      mandb(db)	

# Prints main menu for user interface.  
def main():
   global lock
   if lock == 0:
      f.init()
      f.set_charset()
      lock = 1
   f.cls()
   print('\n     === PyPass Password Manager v4.1 ===')
   print('\n Menu:-\n\n 1)Create Database\n 2)View Database\n 3)Manage Database\n 4)Delete Database\n 5)Import Database\n 6)Export Database\n 7)Backup Masterkey ')
   x = input('\n Enter choice:')
   if x == '1':
      dbname=input('\n Enter Database Name:')
      f.cls()
      f.create_database(dbname)
      f.pause()
      f.cls()
      main()
   elif x == '2':
      f.cls()
      f.view_databases()
      f.pause()
      f.cls()
      main()
   elif x == '3':
      dbname = input('\n Enter Database Name:')
      mandb(dbname)
      f.pause()
      f.cls()
      main()
   elif x == '4':
      dbname = input('\n Enter Database Name:')
      f.cls()
      f.delete_database(dbname)
      f.pause()
      f.cls()
      main()
   elif x == '7':
      f.cls()
      s.mm()
      f.pause()
      f.cls()
      main()
   elif x == '6':
      dbname = input('\n Enter Database Name:')
      print()
      f.export(dbname)
      f.pause()
      f.cls()
      main()
   elif x == '5':
      db = input('\n Enter Database Name:')
      print()
      f.importt(db)
      f.pause()
      f.cls()
      main()
   elif x.lower() == 'c':
      sys.exit(0)
   else:
      print('\n Please enter a valid choice from 1,2,3,4 or 5\n')
      f.pause()
      f.cls()
      main()

	

