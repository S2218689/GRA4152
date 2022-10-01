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
   #  Made both the respons and answer with a .lower function 
   # this makes sure that it does not matter wherether the answer is in
   # upper og lower case, cause both getting matched on lower letters and thus return corcect
   # replaced the spaces with nothing so that spaceing does matter when inputing the answer
   def checkAnswer(self, response) :
      return response.lower().replace(" ", "") == self._answer.lower().replace(" ", "") 
## Displays this question.
q = Question()
q.setText("Who is the inventor of Python?")
q.setAnswer("Guido van Rossum")      


response = input("Your answer: ")
print(q.checkAnswer(response))
# Checked that respons worked with guido van rossum, GuIdO vAN rOSSUM and GUIDO VAN ROSSUM and abc-
# as long as the answer was spelled correctly the it return true
