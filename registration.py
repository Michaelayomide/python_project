passwd=''
passwd2=' '


while passwd2 != passwd:
    passwd=input('enter the your desired password')
    passwd2=input('enter the password again') 
    print('password doesnt match')

    if len(passwd) < 10:
        print("password is too small")


print('your password is set')

    


         
