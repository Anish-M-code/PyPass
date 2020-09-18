
# Pysecret
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

''' Pysecret is a simple secret sharing tool using python3 developed by M.Anish only.
    Converts secrets to more than one code . The secret can't be recovered even if a single code is missing'''
try:
    import os
    import getpass
    import secrets
except ImportError:
    print(' Critical Error: Required Modules Not found!\n')
    x=input(' Press any key to continue...')
    exit(1)

A=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','o','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9')

#converts Alphanumeric characters to numbers of base 36    
def f(x):
  store=[]
  for s in x:
    count=0
    for i in range(36):
        if A[i].lower()==s.lower():
          store.append(i)
          count=1
          break
    if count==0:
      store.append(' ')
  return tuple(store)                
    
#converts base 36 numbers to alphanumeric charactors.
def rf(x):
  store=[]
  q=''
  for s in x:
    count=0
    for i in range(36):
        if i==s:
          store.append(A[i])
          count=1
          break
    if count==0:
      store.append(' ')
  q=''.join(store)
  return q
    
#generates a key without keyfile.
def ikey(x):
    seed=list(range(36))
    masterkey=[]
    for i in range(len(x)):
        masterkey.append(secrets.choice(seed))
    return tuple(masterkey)

#encrypts a given string and returns ciphertxt and key as a tuple. (no file generated!)
def en(msg):
    ciphertxt=[]
    x=f(msg)
    y=ikey(msg)
    for i in range(len(x)):
            if type(x[i])==int :
                ciphertxt.append(((x[i]+y[i])%36))
            else:
                ciphertxt.append(' ')
    ctxt=rf(tuple(ciphertxt))
    shk=rf(y)
    return (ctxt,shk)

#decrypts a given encrypted string and returns a plaintxt as output.
def de(c,k):
    ciphertxt=[]
    x=f(c)
    y=f(k)
    if len(x)<=len(y):
        for i in range(len(x)):
            if type(x[i])==int and type(y[i])==int:
                ciphertxt.append(((x[i]-y[i])%36))
            else:
                ciphertxt.append(' ')
    else:
        x=input(' Press any key to continue...')
        exit(1)
    return rf(tuple(ciphertxt))

#function for secret splitting interface.
def sprocess():
    table=[]
    print('''\n          ---------------------------------------------------------
          |                Backup Code Generator                  |
          ---------------------------------------------------------''')
    while(1):
        try:
            x=int(input('\n Enter the number of backup codes(atmost 10,atleast 2):'))
            if(x<11)and(x>1):
                break
        except ValueError:
            print('\n Please enter a valid integer greater than 1 but less than or equal to 10!\n')
    msg=getpass.getpass(' Enter the master password:')
    table+=list(en(msg))
    for i in range(2,x):
        tmp=table[-1]
        table.pop()
        table+=list(en(tmp))
    for i in range(len(table)):
        print('CODE',i+1,':',table[i])

#function for secret combining interface.
def cprocess():
    table=[]
    print('''\n          ---------------------------------------------------------
          |                Recover Password from Code              |
          ----------------------------------------------------------''')
    while(1):
        try:
            x=int(input('\n Enter no. of backup codes to combine(atmost 10,atleast 2):'))
            if(x<11)and(x>1):
                break
        except ValueError:
                print('\n Please enter a valid integer greater than 1 but less than or equal to 10!\n')
    for i in range(x):
            table.append(getpass.getpass(str(' Enter Code '+str(i+1)+':')))
    for i in range(x-1):
            hook=[]
            a,b=table[-2],table[-1]
            table.pop()
            table.pop()
            hook.append(de(a,b))
            table+=hook
    print()
    print(''.join(table))
        

def start():
    print('\n<-----Task Started----->\n')
    
def end():
    print('\n<-----Task Completed----->\n')

def tsks():
    start()
    
def tske():
    end()

def tskf():
    print('\n<-----Task Failed !----->\n')


def wait():
      x=input('\n Press any key to continue...\n')

def display(file):
        if os.path.exists(file)==False:
           print('Error: '+file+' not found!')
           wait()
           exit(1)
        with open(file,'r') as f:
            s=f.read(1024)
            print(s)
            while len(s)>0:
                s=f.read(1024)
                print(s)

# function for main interface.    
def mm():
   print('''\n           ---------------------------------------------------
               |   OFFLINE PASSWORD BACKUP SYSTEM    |
           ---------------------------------------------------''')
   print('\n 1)Backup Code Generator.')
   print(' 2)Recover Password from codes.')
   cmd=input('\n Enter command:')
   if cmd=='1':
       sprocess()
       mm()
   elif cmd=='2':
       cprocess()
       mm()
   elif cmd.lower()=='c' or cmd.lower()=='close':
      exit()
   else:
      print(' please enter 1 or 2 or \'c\' to exit!')
      mm()
   exit()
    
   
        
        
