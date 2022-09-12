
 ### FAQ
 
 - <b> Is this password manager secure ? </b>
 
 yes , this password manager is reasonably secure. provided an attacker doesnot gains access to your password manager database keyfiles and gets any one password generated using those database keyfiles.
 
 In Lay man's language , this password manager is extremely secure for the following purposes:-
 
 1) Passwords for protecting Files.
 2) Passwords for PGP keys.
 3) Password for Full Disk Encryption
 4) Passwords for Encrypted Volumes like VeraCrypt where one can take advantage of hidden volumes and plausible deniability.
 5) And almost any use where your password is unlikely to get leaked!
 
 Incase if you want to use it for storing passwords for online services, you can use it but keep the database keyfiles
 as securely as possible , if they get compromised it would be game over. ( we assume attackers can get generated passwords from
 leaked sources / data breaches which are fairly common nowadays. )
 
 However there is a way to mitigate this , you can create 3 separate database ( We recommend more than 3 ) with unique master passwords and use one of them for highly sensitive tasks like protecting PGP keys , Full disk encryption , Bank passwords etc, another database for High Security passwords like Gmail , Linkedin which are highly unlikely to get breached , and the other database for storing passwords for Less secure Applications.
 
 The advantage of this Compartmentalization is that if one of the database gets compromised the security of other password databases won't be affected if you use unique passwords.
 
 - <b> If this password Manager is secure why are you recommending against high security use ? </b>
 
 Because this work has not been peer reviewed by security experts and i am not an expert myself.
 
 - <b> Why Another Password Manager ? </b>
 
  Because most other password managers use complex cryptography and have huge amount of code which cannot be easily trusted. Moreover in certain special cases like for use with Veracrypt Hidden volumes this password manager supports plausible deniability which is not present in other password managers. And unlike other password managers this password manager cannot be bruteforced to give away passwords. See the question above for limitations.
  
  - <b> My Password Manager has more features like online sync , extensions , Why use an offline Password Manager like Yours? </b>
   
   Google Project Zero's Researcher Tavis Ormandy has a explaination refer https://lock.cmpxchg8b.com/passmgrs.html .
   This password manager has less features and hence less security bugs :)
   
   - <b> Why use custom Cryptography ? , how do we know it is secure ? </b>
 
   We use custom cryptography because most other ciphers are highly complex and humans cannot compute them easily.
   We aim to backup password databases by printing them on paper and allow people to compute passwords manually.
   Paper has long retention capacity than any electronic media and might serve as good backup.
 
   As for cryptography we use One Time Pad Cipher tweaked for this project , which is as secure as source of randomness.
   This program gets randomness from secrets standard module in python which is cryptographically secure , this essentially
   converts the one time pad cipher to a stream cipher which is secure enough to keep your passwords safe. The secrets module in python 
   can be used for secure randomness source for iv , nonces etc which are heavily used in Modern cryptography , this gurantees this 
   password storage system is no weaker than modern cryptosystems.
   
   Incase you need Information-theoretic security you can export the password database as csv and fill the values of keys using randomness generated
   from true random number source or trustworthy source like pair of dices or any number of combination of dices or coins ( hope you use a blanket so that no one can see the random results generated and being typed in csv using a computer )  
   
   - <b> How to make use of Plausible deniability </b>

   While making accounts give as little information as possible, The master password is used for getting user's passwords
   but the master password is not validated , so simply use another value of master password you will get different value for user password which can be used for plausible deniability. use 2nd master password as steath/hidden password to retrieve your deniable passwords.

   In this way you can use your master password for normal accounts & use stealth master password for getting stealthy deniable passwords.
   
   - <b> Why doesn't this password manager prevent shoulder surfing by hiding passwords and allow copy to clipboard feature ? </b>
   
   I believe password managers are supposed to be used in a lonely place and you should cover yourself in a blanket before using them , password managers should not be used  in a place full of people , even if you have have feature to not display password and copy to clipboard , bystanders can simply snatch your computer and get your password while password manager is unlocked and you have copied password to clipboard.
   
   Second reason is it is difficult to implement such a feature in a command line program and making it cross platform securely.

   - <b> I have found a security issue or more questions , how to contact ? </b>

   Please raise an github issue :)
