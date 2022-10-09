
##
#  This module defines a class that models exam questions. 
#

## A question with a text and an answer.
#
from multiprocessing.spawn import spawn_main
from pickle import TRUE
from urllib import response


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


   
## A question with multiple choices.

class ChoiceQuestion(Question) :
   # Constructs a choice question with no choices.
   def __init__(self) :
      super().__init__()
      self._choices = []

   ## Adds an answer choice to this question.
   #  @param choice the choice to add
   #  @param correct True if this is the correct choice, False otherwise
   #
   def addChoice(self, choice, correct) :
      self._choices.append(choice)
      if correct :
         # Convert len(choices) to string.
         choiceString = str(len(self._choices))
         self.setAnswer(choiceString)
   
   # Override Question.display().
   def display(self) :
      # Display the question text.
      super().display()
      
      # Display the answer choices.
      for i in range(len(self._choices)) :
         choiceNumber = i + 1
         print("%d: %s" % (choiceNumber, self._choices[i]))

# made a subclass of the choicequestion
class multiplequestion(ChoiceQuestion):
    def __init__(self):
       super().__init__()

 
# overides the checked answer method from the choiceclass
# checked if the self._answer was empty first and if then i should add it to correctresponse
# else it adds a space between the answers and then append it 
   
    def setAnswer(self, correctResponse) :
        if self._answer == "":
            self._answer += correctResponse
        else:
            self._answer +=  " " + correctResponse
        


# made a display metod thats explains displays the question and prints instructions for how the program work to the user
    def display(self) :
        super().display()
        print("More then one answer is correct, write all of the correct answers in chronological ordered numbers and separate them by spaces")

# made a functuon that takes in user input as answer to the question         
def presentQuestion(spm) :
    spm.display()
    response = input("Write your answer: ")
    print(spm.checkAnswer(response))


# tested that 1 2 equals true and 2 3 etc equals false
spm = multiplequestion()
spm.setText("What laguage do they speak in Canada?: ")
spm.addChoice("English", True)
spm.addChoice("French", True)
spm.addChoice("Chinese", False)
spm.addChoice("Canadian", False)
spm.display()
presentQuestion(spm)
# called the method and the function and checked that the program worked as expected
