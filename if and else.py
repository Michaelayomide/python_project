# name=input("ENTER YOUR Name")
# password1='etodavid'
# password2=input("ENTER YOUR PASSWORD")
# # password = input("comfrim password")
# # password>8:1


# if len(name)<8 or password2!=password1:
#     print("not logged in")
    

# else:
    
#     print("logged in")


password='etodave'

inp_password=''

n=3
attempts=0


inp_password=input('enter your password ')

while password != inp_password:

    if attempts < 3:
        print("wrong password")
        inp_password=input('enter your password ')
        
        #attempts=attempts+1
        attempts+=1

        print(f'you have {n-attempts} left')

    else:
        print('your are temporarily blocked')
        print('try again after 2 hourse')
        break

else:
    print('WELCOME USER')


