# superclass apointments
class Appointment:
    def __init__(self, describtion): # constructor 
        self._describtion = describtion

# does not get implemented before the subclass
    def occursOn (self, year , month, day):
           raise NotImplementedError("Please Implement this method")
# return the describtion of the appointment
    def appointmentdesc(self):
        return self._describtion
# subclass that inherits from the superclass
class Onetime(Appointment):
# added year, month and day as paramethers to the constructor
    def __init__(self, describtion, year, month, day):

         super().__init__(describtion)
         self._year = year
         self._month = month
         self._day = day
# for a onetime appointment the day, the year and month have to true if its going to occur
    def occursOn(self, year, month, day):


        if self._day == day and self._month == month and self._year == year:
            return True
        else: 
            return False
class Daily(Appointment):# subclass that inherits from the superclass

    def __init__(self, describtion):
        super().__init__(describtion)
# since daily appointments happens every day, it always will be true
    def occursOn(self, year, month, day):
        return True


class Monthly(Appointment):# subclass that inherits from the superclass and add day as a parameter to the constructor
    def __init__(self, describtion, day): 
        super().__init__(describtion)
        self._day = day 
    # montly appointments happens each month, but on the same day so you only need to check the day
    def occursOn(self, year, month, day):
        if self._day == day:
            return True 
        else: 
            return False

# sets up onetime, daily and monthly apoinments 
app1 = Onetime("Math exam", 2022, 10, 1)
app2 = Daily("Brush your theeth")
app3 = Monthly("Pay your rent", 15)

# creates a list of the appointments
appointments = [app1, app2, app3]
# takes user input to check wheather callender is booked
day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))
 # loops over apointments and check and prints if they occur
for app in appointments:
    if app.occursOn(year, month, day):
        print(app.appointmentdesc())
    





        


