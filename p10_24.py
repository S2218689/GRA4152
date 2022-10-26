

class Appointment:
    def __init__(self, describtion):
        self._describtion = describtion

    def appointmentdesc(self):
        return self._describtion

# does not get implemented before the subclass
    def occursOn (self, year , month, day):
           raise NotImplementedError("Please Implement this method")

    
    
    def savetofile(self, outfile):# saves the describtion to file
        outfile.write(f"'" + self._description + "'")  


class Onetime(Appointment):

    def __init__(self, describtion, year, month, day):

         super().__init__(describtion)
         self._year = year
         self._month = month
         self._day = day

    def occursOn(self, year, month, day):


        if self._day == day and self._month == month and self._year == year:
            return True
        else: 
            return False 
    def savetofile(self, outfile): # saves the describtion day, month and year to file
        super().savetofile(outfile)
        outfile.write(f" " + str(self._day) + " " + str(self._month) + " " + str(self._year) + "\n")

    
class Daily(Appointment):

    def __init__(self, describtion):
        super().__init__(describtion)

    def occursOn(self, year, month, day):
        return True
    
    def savetofile(self, outfile): # saves the describtion
        super().savetofile(outfile)
        outfile.wirte(f"\n")

class Monthly(Appointment):
    def __init__(self, describtion, day):
        super().__init__(describtion)
        self._day = day
    
    def occursOn(self, year, month, day):
        if self._day == day:
            return True 
        else: 
            return False
    def savetofile(self, outfile): # montly events saves the day to file
        super().savetofile(outfile)
        outfile.write(f" " + str(self._day) + " "  + "\n")


app1 = Onetime("Math exam", 2022, 10, 1)
app2 = Daily("Brush your theeth")
app3 = Monthly("Pay your rent", 15)

day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))
# same code as in p10.22. except for the savetofile method. unfortunately did not have the time to do the p10.23 due to midterms.
appointments = [app1, app2, app3]

for app in appointments:
    if app.occursOn(year, month, day):
        print(app.appointmentdesc())


# set done to false
done = False
while not done: # used a while loop when not finished and takes userinput for what they like to do
    action = input("S)ave appointments L)oad appointments Q)uit ")
    action = action.lower # set action to lower so both lower and uppercase letter works
    if action == "Q":
        finished = True 
        # if user chooses Q the program finishes
    elif action == "L" or action == "S":
        if action == "S":
            filename = input("Enter filename ")
            outfile = open(filename, "w") # if user chooses s, we open the and writes the appointment to the file
            for app in appointments:
                app.savetofile(outfile) # saves using the savetofile method
            outfile.close() # closes file
        
    else: # user wants to load the appointments, since r it standard in open we dont need to write it
        filename = input("Enter filename")
        infile = open(filename) 
        line = infile.readline()
        
        
        number = len(line)
        describtion = []

        if number == 0: # if number  equal to 0 its a daily appointment
            app = Daily(describtion)
            appointments.append(app)
        elif number == 1: # if number is equal to 1 its a montly appointment
            app= Monthly(describtion, int(line[0]))
            appointments.append(app)
        else: # else its a onetimeappointment
            app = Onetime(describtion, int(line[0]), int(line[1]), int(line[2]))
        line = infile.readline()
    infile.close() # closes the file













        


