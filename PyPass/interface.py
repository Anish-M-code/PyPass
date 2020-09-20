
#This Python module contains menu interfaces for pypass project.
#Developed by M.Anish only.

lock=0

try:
    import pysecret as s
    import functions as f
except ImportError:
    print(' Critical Error: Required Modules Not found!\n')
    x=input(' Press any key to continue...')
    exit(1)

def mandb():
  f.cls()
  f.load()
  f.cls()
  print('\n     === PyPass DB Manager Menu ===')
  print('\n 1)Create Account\n 2)View Accounts\n 3)Display Account\n 4)Delete Account\n 5)Modify Account')
  x=input('\n Enter choice:')
  if x=='1':
     f.createac()
     f.pause()
     f.cls()
     mandb()
     exit(0)
  elif x=='2':
     f.viewac()
     f.pause()
     f.cls()
     mandb()
     exit(0)
  elif x=='3':
     f.display()
     f.pause()
     f.cls()
     mandb()
     exit(0)
  elif x=='4':
     f.delac()
     f.pause()
     f.cls()
     mandb()
     exit(0)
  elif x=='5':
     f.modac()
     f.pause()
     f.cls()
     mandb()
     exit(0)
  elif x.lower()=='c':
      exit()
  elif x.lower()=='mm':
      f.release()
      main()
      exit()
  
  else:
     print('\n Please enter a valid choice from 1,2,3,4 or 5')
     f.pause()
     f.cls()
     mandb()
     exit(1)
	
  
def main():
  global lock
  if lock==0:
    f.init()
    lock+=1
  f.cls()
  print('\n     === PyPass Password Manager v3.0 ===')
  print('\n Menu:-\n\n 1)Create Database\n 2)View Database\n 3)Manage Database\n 4)Delete Database\n 5)Import Database\n 6)Export Database\n 7)Backup Masterkey ')
  x=input('\n Enter choice:')
  if x=='1':
     f.createdb()
     f.pause()
     f.cls()
     main()
     exit(0)
  elif x=='2':
     f.viewdb()
     f.pause()
     f.cls()
     main()
     exit(0)
  elif x=='3':
     global count
     mandb()
     f.pause()
     f.cls()
     main()
     exit(0)
  elif x=='4':
     f.deldb()
     f.pause()
     f.cls()
     main()
     exit(0)
  elif x=='7':
     s.mm()
     f.pause()
     f.cls()
     main()
     exit(0)
  elif x=='6':
     f.export()
     f.pause()
     f.cls()
     main()
     exit(0)
  elif x=='5':
     f.importt()
     f.pause()
     f.cls()
     main()
     exit(0)
  elif x.lower()=='c':
     exit(0)
  else:
     print('\n Please enter a valid choice from 1,2,3,4 or 5')
     f.pause()
     f.cls()
     main()
     exit(1)
	