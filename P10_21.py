## 
#  This module defines several classes that implement a banking account
#  class hierarchy.
#

## A bank account has a balance and a mechanism for applying interest or fees at 
#  the end of the month.
#
class BankAccount :
   ## Constructs a bank account with zero balance.
   #
   def __init__(self) :
      self._balance = 0.0

   ## Makes a deposit into this account.
   #  @param amount the amount of the deposit
   #
   def deposit(self, amount) :
      self._balance = self._balance + amount
   
   ## Makes a withdrawal from this account, or charges a penalty if
   #  sufficient funds are not available.
   #  @param amount the amount of the withdrawal
   #
   def withdraw(self, amount) :
      self._balance = self._balance - amount
   
   ## Carries out the end of month processing that is appropriate
   #  for this account.
   #
   def monthEnd(self) :
      return
   
   ## Gets the current balance of this bank account.
   #  @return the current balance
   #
   def getBalance(self) :
      return self._balance
      
      
## A savings account earns interest on the minimum balance.
#
class SavingsAccount(BankAccount) :
   ## Constructs a savings account with a zero balance.
   #
   def __init__(self) :
      super().__init__()
      self._interestRate = 0.0
      self._minBalance = 0.0

   ## Sets the interest rate for this account.
   #  @param rate the monthly interest rate in percent
   #
   def setInterestRate(self, rate) :
      self._interestRate = rate
  

   ## Overrides superclass method.
   #
   def withdraw(self, amount) :
      super().withdraw(amount)
      balance = self.getBalance()
      if balance < self._minBalance :
         self._minBalance = balance

   ## Overrides superclass method.
   #
   def monthEnd(self) :
      interest = self._minBalance * self._interestRate / 100
      self.deposit(interest)
      self._minBalance = self.getBalance()
      
      
# created a subclass of bankaccount.
class CheckingAccount(BankAccount) :
   
 
   def __init__(self) :
      super().__init__()
      self._withdrawals = 0


#extens the superclass so that it also checks checkfee method
   def deposit(self,amount):
    super().deposit(amount)
    self.Checkfee()
    

 # extens the superclass so that it also checks checkfee method
   def withdraw(self, amount):
    super().withdraw(amount)
    self.Checkfee()
   

# added a check fee method that checks if the the the user does more then 3 deposits or withdraws

   def Checkfee(self) :
      FREE_WITHDRAWALS = 3
      WITHDRAWAL_FEE = 1
     
 # checked if withdrwawls was bigger then then the three free, if it was it set the withdrawl fee of one

      self._withdrawals = self._withdrawals + 1
      if self._withdrawals > FREE_WITHDRAWALS :
         super().withdraw(WITHDRAWAL_FEE)
  

    


   # Overrides superclass method since its three free deposist per month
   # so that it starts with zero when theres a new month
   def monthEnd(self):
      self._withdrawals = 0

account1 = SavingsAccount()
account2 = CheckingAccount()

accounts = [account1, account2]

# the testing from book example and tested that it took a fee from both deposit and withdraw if the limit was extended
done = False
while not done :
   action = input("D)eposit  W)ithdraw  M)onth end  Q)uit: ")
   action = action.upper()
   if action == "D" or action == "W" :  # Deposit or withdrawal.
      num = int(input("Enter account number: "))
      amount = float(input("Enter amount: "))

      if action == "D" :
         accounts[num].deposit(amount)
      else :
         accounts[num].withdraw(amount)

      print("Balance:", accounts[num].getBalance())
   elif action == "M" :   # Month end processing.
      for n in range(len(accounts)) :
         accounts[n].monthEnd()
         print(n, accounts[n].getBalance())
   elif action == "Q" :
      done = True

