class bankacc:
    def __init__(self , balance =0):
        self.balances = balance
    def withdraw(self , amount):
        if (amount <= self.balances):
            self.balances-=amount
            print("done")
        else:
            print("cant ")
    def deposite 