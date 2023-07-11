


password='etodave'

inp_password=''

n=3

attempts=0



def display_balance(balance):
    print(f"Available Balance: ${balance}")

def deposit(balance):
    amount = float(input("Enter the to deposit: $"))
    balance += amount
    print(f"${amount} deposited successfully.")
    return balance

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: $"))
    if amount > balance:
        print("insufficient Balance.")
    else:
        balance -= amount
        print (f"${amount} withdraw successfull.")
        
        return balance   
    




def run_atm():
    balance = 0.0

    while True:
        print("\nATM MENU:")
        print("1. Display Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your chpice (1-4):")
        if choice == "1":
            display_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice.")



#password validator

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
        print('try again after 2 hours')
        break

else:
    print('WELCOME USER')

    run_atm()            

        
