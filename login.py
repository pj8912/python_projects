import time

uname = "john"
pwd = "123"

uname_input = input('Username*: ')
pwd_input = input('Password*: ')

if uname_input == uname and pwd_input == pwd:
    print('Signing in....')
    time.sleep(2)
    print('Loading...')
    time.sleep(1)
    print('Welcome', uname)
elif uname_input == uname and pwd_input != pwd:
    print('Password Incorrect!')

elif uname_input != uname and pwd_input == pwd:
    print('Username Incorrect!')
else:
    print('Wrong Credentials. Please Try Again!')



