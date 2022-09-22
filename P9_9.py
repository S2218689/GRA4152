
from turtle import right


class Combolock:

# constructor with two empty lists
    def __init__(self):
        self._dial = []
        self.click = []
       
    
    

    
    # made a setlock method to that does the math behind a codelock
    # takeing in to account that you sometimes need to cross the whole lock if the first left if is bigger then the first right you first need 40  and then you can take secret 1 - 2
    # used an F string to show witch way we turn and then appended it to our self.dial list
    def setLock(self, secret1, secret2, secret3):
        self._dial.append(f"Right {secret1}")
        if secret2 >= secret1:
            self._dial.append(f"Left {40 - secret2 + secret1}")
        else:
            self._dial.append(f"Left {secret1 - secret2}")

        if secret3 > secret2:
            self._dial.append(f"Right {secret3-secret2}")
        else:
            self._dial.append(f"Right {secret3-secret2 + 40}")
        print(self._dial)


    
    # made a turnRight method and appeded it to the self.click list
        
    def turnRight(self, turn):
        self.click.append(f"Right {turn}")

        
        

        
        

    # made a turnLef method and appended it to the self.click list
    def turnLeft(self, turn):
        self.click.append(f"Left {turn}")



# created a metjod to check if the self.dial and self.click eqauls and if they do, the look would open. 
# If they did not match it prints Wrong combo 
    def open(self):
        if self._dial == self.click:
            print(True)
        else:
            print("Wrong combo")

# resets the lock to a emtpy list
    def reset(self):
        self.click = []

# checked if all combinations worked as antisipated
minlås2 = Combolock()
minlås2.setLock(1,2,3)
minlås2.turnRight(1)
minlås2.turnLeft(39)
minlås2.turnRight(1)
minlås2.open()
# checked if the resetbutton works
minlås1 = Combolock()
minlås1.setLock(1,2,3)
minlås1.turnRight(1)
minlås1.turnLeft(39)
minlås1.turnRight(1)
minlås1.open()
minlås1.reset()
minlås1.turnRight(23)
minlås1.turnLeft(10)
minlås1.turnRight(28)
minlås1.open()






