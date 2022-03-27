# PyPass Password Manager v3.2.2

<p>A simple ,Highly secure and trustable password Manager developed in Python3.</p>
<img src="https://github.com/Anish-M-code/PyPass/blob/master/screenshots/1.cleaned.png">

Quick Installation
------------------

To Install from [PyPI](https://pypi.org/project/passwordsgo/):

Run the following commands in Linux terminal / Windows powershell / command prompt to install:-

```
pip install passwordsgo
```
Then to get started , simply type :-

```
passwordsgo
```
 To run program by directly downloading from github refer [ Instructions](/Install.md) here.
 
 ### Main Features and Highlights
 * It is free and fully Open Source!
 * It uses Quantum Safe Cryptography.
 * If used correctly it supports plausible deniability of passwords.
 * The code is Simple, Modular and Trustable which even beginners can audit for correctness.
 * It does not use any third party modules other than standard python libraries.
 * It is Practically very hard to use Brute-force attacks to recover user passwords.
 * It Uses Robust Offline Password Backup System to backup passwords. 
 
 <img src="https://github.com/Anish-M-code/PyPass/blob/master/screenshots/10.cleaned.png" width=800 height=600>
 
 ### FAQ
 
 - <b> Is this password manager secure ? </b>
 
 yes , this password manager is reasonably secure. provided an attacker doesnot gains access to your password manager database keyfiles
 and any one password generated using those database keyfiles.
 
 In Lay man's language , this password manager is extremely secure for the following purposes:-
 
 1) Passwords for protecting Files.
 2) Passwords for PGP keys.
 3) Password for Full Disk Encryption
 4) Passwords for Encrypted Volumes like VeraCrypt where one can take advantage of hidden volumes and plausible deniability.
 5) And almost any use where your password is unlikely to get leaked!
 
 Incase if you want to use it for storing passwords for online services, you can use it but keep the database keyfiles
 as securely as possible , if they get compromised it would be game over. ( we assume attackers can get generated passwords from
 leaked sources / data breaches which are fairly common nowadays. )
 
 However there is a way to mitigate this , you can create 3 separate database ( We recommend more than 3 ) with unique master passwords and use one of them
 for highly sensitive tasks like protecting PGP keys , Full disk encryption , Bank passwords etc, another database for High Security passwords 
 like Gmail , Linkedin which are highly unlikely to get breached , and the other database for storing passwords for Less secure Applications.
 
 The advantage of this Compartmentalization is that if one of the database gets compromised the other password databases won't be affected if you
 use unique passwords.
 
 - <b> Why Another Password Manager ? </b>
 
  Because most other password managers use complex cryptography and have huge amount of code which cannot be easily trusted. Moreover in certain special
  cases like for use with Veracrypt Hidden volumes this password manager supports plausible deniability which is not present in other password managers.
  And unlike other password managers this password manager cannot be bruteforced to give away passwords. See the question above for limitations.
  
  - <b> My Password Manager has more features like online sync , extensions , Why use an offline Password Manager like Yours? </b>
   
   Google Project Zero's Researcher Tavis Ormandy has a explaination refer https://lock.cmpxchg8b.com/passmgrs.html 
   This password manager has less features and hence less security bugs :)
   
   - <b> Why use custom Cryptography ? , how do we know it is secure ? </b>
 
   We use custom cryptography because most other ciphers are highly complex and humans cannot compute them easily.
   We aim to backup password databases by printing them on paper and allow people to compute passwords manually.
   Paper has long retention capacity than any electronic media and might serve as good backup.
 
   As for cryptography we don't use custom one , we use One Time Pad Cipher. 
   
   - <b> I have found a security issue or more questions , how to contact ? </b>

   Please raise an github issue :)
 
 ### Interested in our Project???
 * visit our screenshot gallery: https://github.com/Anish-M-code/PyPass/blob/master/screenshots/Gallery.md
 * Currently i consider this work as personal project so i don't expect public contributions.
 * Feel free to create an issue if you feel something is missing or broken.
 




