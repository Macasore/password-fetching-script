#! python
# passscript.py ---An insecure sort of password lock program.
import sys, pyperclip

#SCRIPT ACCESS CHECKPOINT BEGINS HERE

key = 'maca123'#----- change if interested
while True:
    enter = input('enter key to view password: ')
    if enter == key:
        break
    else:
        continue
#SCRIPT ACCESS CHECKPOINT ENDS HERE

#REQUIRED ACCOUNTS AND PASSWORDS 
PASSWORDS = {'email': 'that one no dey', 'facebook' : 'how many years ago',
             'instagram': 'i cant really remember'} #---of course i wont put my actual password lmao

if len(sys.argv) <2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
account = sys.argv[1]    

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)    
        