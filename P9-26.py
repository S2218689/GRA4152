from itertools import count


class Customer:

  def __init__(self):
    self.acprice = 0
    self.count = 0
# created a function thats first checks if the count is bigger than 100 if thats true, it adds to amount and then gives discount. 
# if it purchase was under it added the amount to the count. then subtrackted by 100 + amount - 10, to make it posible to get discounts on next purchase and save the amount over thats over 100.
  def makePurchase(self, amount):
    if self.discountReached():
        self.acprice += amount - 10
        self.count = self.count - 100 + amount - 10
        
    else:
        self.count += amount
        self.acprice += amount
    


    # used a boolean to check if count was larger than 100 and should result in a discount

  def discountReached(self):
    if self.count >= 100:
        return True
    else:
        return False



# checked if the program works with the textbook exercises, then checked if the program handles totals > 100 and gives discount on the next.
purchase = Customer()
"""purchase.makePurchase(100)
purchase.makePurchase(90)
purchase.makePurchase(50)"""
purchase.makePurchase(90)
purchase.makePurchase(50)
purchase.makePurchase(50)
print(purchase.count)