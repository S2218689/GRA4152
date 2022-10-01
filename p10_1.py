##
#  This module defines a class that models exam questions. 
#

## A question with a text and an answer.
#





from urllib import response
from decimal import *



class Question :
   ## Constructs a question with empty question and answer strings.
   #
   def __init__(self) :
      self._text = ""
      self._answer = ""
      
   ##  Sets the question text.
   #   @param questionText the text of this question
   #
   def setText(self, questionText) :   
      self._text = questionText

   ## Sets the answer for this question.
   #  @param correctResponse the answer
   #
   def setAnswer(self, correctResponse) :
      self._answer = correctResponse

   ## Checks a given response for correctness.
   #  @param response the response to check
   #  @return True if the response was correct, False otherwise
   #
   def checkAnswer(self, response) :
      return response == self._answer

   ## Displays this question.
   #
   def display(self) :
      print(self._text)         
   
# created a subclass named Numeric question, with the superclass.
class NumericQuestion(Question):
    def __init__(self):
       super().__init__()

# changed the checkAnswer method from superclass
# converted the repsonse and correctResponse to floats and absolute values
# formated the checks to avoid floating errors and only taking in three decimals
# if the boolean where True it prints Corect answer else it prints Wrong answer
# 
    def checkAnswer(self,response):
      
       checks = float(abs(self._answer) - float(response))
       ("{0:.3f}".format(checks))
       if checks <= 0.01:
        print("Corect answer")
       else:
        print("Wrong answer")

# created a instance of the subclass called spm
spm = NumericQuestion()
# made a fucntion that checks takes a user inputs and checks it with complete
# correct or differs with less then 0,01 from with the checkanswer method 
def examquestion(spm):
    spm.display()
    response = input("Write your answer in numbers: ")
    spm.checkAnswer(response)
    
# Set a question and a answer and then testet if the program worked with- 
# the completly right answer (100) and a answer that that was less then 0,01 apart 100.01 both worked
spm = NumericQuestion()
spm.setText("what tempature does water boil at?")
spm.setAnswer(100)
examquestion(spm)
       

