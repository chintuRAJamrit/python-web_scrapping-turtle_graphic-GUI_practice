#Develop a class BankAccount that supports these methods:
#a). init(): Initializes the bank account balance to the value of the input argument, or to 0 if noinput argument is given.
#b). withdraw(): Takes an amount as input and withdraws it from the balance.
#c). deposit(): Takes an amount as input and adds it to the balance.
#d). balance(): Returns the balance on the account.


class bankacc:
    def __init__(self , balance = 0):
        self.balances = balance
    def withdraw (self , amount ):
        if self.balances >= amount:
            self.balances -= amount
            print(f"{amount} is withdrawed frm account")
        else:
            print("not enough balance ")
    def deposit (self , amount ):
        self.balances += amount
        print(f"{amount} is  depostied to the account")
    def balance (self):
        print(f"{self.balances} is the balance")

account = bankacc(int(input("enter the initial opening balance ")))
loop_runner = True
while loop_runner:
    print("\n bank account\n")
    print("operations\n 1. withdraw \n 2. deposit\n 3. balance \n 4. exit ")
    option = int(input("enter yr choice" ))
    if option == 1:
        account.withdraw(int(input("enter the amount")))
    elif option == 2:
        account.deposit(int(input("enter the amount")))
    elif option == 3:
        account.balance()
    else:
        loop_runner = False
        
            
