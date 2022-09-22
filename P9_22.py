##
#  This module defines a class that models a bank account.
#

## A bank account has a balance that can be changed by deposits and withdrawals.
#
import mimetypes
from pyexpat import ParserCreate


class BankAccount :
   
   ## Constructs a bank account with a given balance.#  @param initialBalance the initial account balance (default = 0.0)
   
   def __init__(self, initialBalance = 0.0) :
      self._balance = initialBalance

   ## Deposits money into this account. #  @param amount the amount to deposit
   
   def deposit(self, amount) :
      self._balance = self._balance + amount

   ## Makes a withdrawal from this account, or charges a penalty if #  @param amount the amount of the withdrawal, #  sufficient funds are not available.


   def withdraw(self, amount) :
      PENALTY = 10.0
      if amount > self._balance :
         self._balance = self._balance - PENALTY
      else :         
         self._balance = self._balance - amount

   ## Adds interest to this account. #  @param rate the interest rate in percent
  
   
   def addInterest(self, rate) :
      amount = self._balance * rate / 100.0
      self._balance = self._balance + amount

   ## Gets the current balance of this account.  #  @return the current balance
   
   def getBalance(self) :
      return self._balance

# made a two instances of the bankaccount class in my constructor
class Portfolio:
   def __init__(self):
      self._Savings = BankAccount()
      self._checkings = BankAccount()
      

   # used the attributes of method deposit from the bankaccount class and checked witch of the account is getting affected
   def deposit(self, amount, account):
      if account == "S":
         self._Savings.deposit(amount)
      elif account == "C":
         self._checkings.deposit(amount)

         
   
# used the attributes of method withdraw from the bankaccount class and checked witch of the account is getting affected
   def withdraw(self, amount, account):
      if account == "S":
         self._Savings.withdraw(amount)
      elif account == "C":
         self._checkings.withdraw(amount)

# checked if the amount was balance was greater or alike the amount we wanted to tranfer and transferd money if there was coverage
# if there not enough coverage the program prints out Not enough coverage to complete this tranfer.
   def transfer(self, amount, account):
      if account == "S": 
         if self._Savings.getBalance() >= amount:
             self._Savings.withdraw(amount)
             self._checkings.deposit(amount)
         else:
            print("Not enough coverage to complete this tranfer")
      elif account == "c":
      
         if self._checkings.getBalance() >= amount:
            self._checkings.withdraw(amount)
            self._Savings.deposit(amount)
         else:
            print("Not enough coverage to complete this tranfer")

 # used the attributes of method GetBalance from the bankaccount class and checked witch of the account is getting affected

   def getBalance(self, account):
      if account == "S":
        return self._Savings.getBalance()
      elif account == "C":
        return self._checkings.getBalance()
   
# tested the code trying out all the new methods with on saving account and checkings account 
accounts = Portfolio()
accounts.deposit(100, "S")
accounts.deposit(100, "S")
accounts.withdraw(10, "S")
accounts.deposit(300, "C")
print(accounts.getBalance("C"))
print(accounts.getBalance("S")) 
accounts.transfer(1000, "S")