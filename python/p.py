class Bank:
    Bank_name='sbi bank'
    ifsc='sbin1001'
    loc='bangalore'
    def __init__(self,acno,name,min_bal=1000):
        self.acno=acno
        self.name=name
        self.bal=min_bal
    @classmethod
    def bank_details(cls):
        print('bank details:')
        print(f'bank name:{cls.bank_name}ifse:{cls.ifsc}loc:{cls.loc}')
    def deposit(self):
        amt=float(input('enter deposit amount:'))
        self.bal+=amt
        print('deposit successfull......deposit amount:',amt)
    def account_details(self):
        print('account details:')
        print(f'acno:{self.acno}name:{self.name}balance:{self.balance}')
        Bank.bank_details: 
        self.balance(self):
               

  
    
    ch=int(input('enter a choice:'))
    if ch==1:
        print('account')
    elif ch==2:
        print('withdraw')
    elif ch==3:
        print('balance')
    elif ch==4:
        print('location')
    elif ch==5:
        exit()
    else:
        print('Invalid Number')
b=BankAccount('sbi',500,1000,'bangalore')
b.bank_details()
    


                
