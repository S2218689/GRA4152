


class address: 
# Constructs a class called menu
# Made a constructor with all the values that a adress contains 
  def __init__(self, street, city, state, houseNumb, postalcode, apartmentNumb = None):
    self.street = street
    self.city = city
    self.state = state
    self.houseNumb = houseNumb
    self.postalcode = postalcode
# print function using f string and \n to implicate a new line
  def printed(self):
    data = f"Address  {self.street} \n,{self.city} {self.state}, {self.postalcode}"
    print(data)

# checks if the postalcode comes before others postalcode 
  def comesBefore(self, other):
    if self.postalcode < other.postalcode:
      return True
    else:
      return False
    
myaddress = address("Pirkavegen", "Kilpis", "Finland", "59", "9012" )
mysecondadreess = address("Joushuavegen", "Lappland", "Finland", "69", "8969" )
myaddress.printed()








