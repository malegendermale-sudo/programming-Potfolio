correct_password = '12345'

while True:
    password = input('Enter the pssword: ')
    if password == correct_password:
        print('Access Granted')
        break
    else:
        print('Incorrect password. try again later. ')