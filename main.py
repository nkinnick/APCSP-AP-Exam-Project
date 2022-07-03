'''
Create Task Program
Creates a program that takes a user input and creates an output. For this one specifically, the code will simulate input as the student choosing for a schedule and the output will list the classes for them.
'''


#The starting class to choose from will be the math class.
#User chooses a math class from the list that responds to the previously asked question.
credits = 0
def mathSelection():
  global mathChoice
  mathChoice = ""
  while mathChoice not in mathClasses:
    print("Choose a math class (please type exactly as seen above, captitalization matters, no spaces at the end of each choice): ")
    mathChoice = input()
    if mathChoice not in mathClasses:
      print("Retry")
    #Calls the englishSelection() function once the math class has been selected
    if mathChoice in mathClasses:
      global credits
      credits = credits + 2
      print("Credits after Math: ", credits)
      print()
      englishSelection()
      
      

#Creates a definition to continue to schedule creator once a math class is selected. The mathChoice loop will call this definition when the appropriate class is chosen by the user.
def englishSelection():
  print('-----------------------------')
  #Prints out the English class choices for the user to select from
  print("English class choices: " + ', '.join(englishClasses))
  print('')
  global englishChoice
  englishChoice = ""
  while englishChoice not in englishClasses:
    englishChoice = input("Choose an English class now: ")
    if englishChoice not in englishClasses:
      print("Retry")
    if englishChoice in englishClasses:
      global credits
      credits = credits + 2
      print("Credits after English: ", credits)
      print()
      historySelection()
      
def historySelection():
  print('-----------------------------')
  #Prints out the History class choices for the user to select from
  print("History class choices: " + ', '.join(historyClasses))
  print('')
  global historyChoice
  historyChoice = ""
  while historyChoice not in historyClasses:
    historyChoice = input("Choose a History class now: ")
    if historyChoice not in historyClasses:
      print("Retry")
    if historyChoice in historyClasses:
      global credits
      credits = credits + 2
      print("Credits after History: ", credits)
      print()
      scienceYesNo()
    

#In most high schools, science classes are not required during junior year. This code gives the user the option of whether or not they would like to take a science or not.
def scienceYesNo():
  yesNoAnswer = str(input("Would you like to take a science class (yes or no)? ")).lower()
  if yesNoAnswer == "yes":
    scienceSelection()
  if yesNoAnswer == "no":
    print("No science class selected.")
    performingArtsSelection()
    
def scienceSelection():
  print('-----------------------------')
  #Prints out the History class choices for the user to select from
  print("Science class choices: " + ', '.join(scienceClasses))
  print('')
  global scienceChoice
  scienceChoice = ""
  while scienceChoice not in scienceClasses:
    scienceChoice = input("Choose a science class now: ")
    if scienceChoice not in scienceClasses:
      print("Retry")
    if scienceChoice in scienceClasses:
      global credits
      credits = credits + 2
      print("Credits after Science: ", credits)
      print()
      performingArtsSelection()
      
def performingArtsSelection():
  print('-----------------------------')
  #Prints out the History class choices for the user to select from
  print("Performing Arts class choices: " + ', '.join(performingArtsClasses))
  print('')
  global performingArtsChoice
  performingArtsChoice = ""
  while performingArtsChoice not in performingArtsClasses:
    performingArtsChoice = input("Choose a music class now: ")
    if performingArtsChoice not in performingArtsClasses:
      print("Retry")
    if performingArtsChoice in performingArtsClasses:
      global credits
      credits = credits + 2
      print("Credits after Performing Arts: ", credits)
      print()
      artSelection()
      

def artSelection():
  print('-----------------------------')
  #Prints out the History class choices for the user to select from
  print("Art class choices: " + ', '.join(artClasses))
  print('')
  global artChoice
  artChoice = ""
  while artChoice not in artClasses:
    artChoice = input("Choose an art class now: ")
    if artChoice not in artClasses:
      print("Retry")
    if artChoice in artClasses:
      global credits
      credits = credits + 2
      print("Credits after Business: ", credits)
      print()
      businessSelection()
      

def businessSelection():
  print('-----------------------------')
  #Prints out the History class choices for the user to select from
  print("Business class choices: " + ', '.join(businessClasses))
  print('')
  global businessChoice
  businessChoice = ""
  while businessChoice not in businessClasses:
    businessChoice = input("Choose a business class now: ")
    if businessChoice not in businessClasses:
      print("Retry")
    if businessChoice in businessClasses:
      global credits
      credits = credits + 2
      creditTotal()

#-----------------------------------------------------------

#Displays the math classes that a junior can take in a list
mathClasses = ["Honors Pre-Calculus", "Pre-Calculus", "AP Calculus AB", "Honors Geometry", "Geometry", "Algebra II"]
#Displays junior English classes in a list
englishClasses = ["AP English 11", "English 11", "Speech"]
#Displays junior History classes in a list
historyClasses = ["AP US History", "US History", "World History"]
#Displays junior Science classes in a list
scienceClasses = ["Chemistry", "Honors Chemistry", "Physics", "AP Physics 1", "Earth Science", "Anatomy", "Zoology"]
#Displays music classes one can take as an elective
performingArtsClasses = ["Choir", "Band", "Orchestra", "Music Theory", "Theatre"]
#Displays art classes one can take as an elective
artClasses = ["Intro to 2D Art", "2D Art", "3D Art", "Ceramics"]
#Displays business classes one can take as an elective
businessClasses = ["Accounting", "Business Law", "Computer Science A", "Marketing in Hospitality and Tourism", "Administrative and Office Management"]


print("You are a sophomore that is creating a new schedule for junior year. You have a select amount of classes to choose from.")
print("Math Class Choices: " + ', '.join(mathClasses))
print()

#Sets the credits equal to 0 and lets the classes and 2 for each choice.

def creditTotal():
  #Checks for if there are too little credits and lets the user retry.
  print("Total Number of Credits Selected: ", credits)
  print()

  if credits < 12:
    print("Error: You must have a credit amount equal to 12 by the end of the year. Please try again.")
    mathSelection()
  #This time, it checks if the user has over the amount of credits you can have
  elif credits > 14:
    print("Error, you have selected too many classes, please try again.")
  elif credits == 14:
    print("You have enough credits to pass junior year! Here's your final schedule:")
#Calls the first function of the program that will begin the schedule creation process.
mathSelection()



    
#This array combines all the class choices into one list  
schedule = [[mathChoice], [englishChoice], [historyChoice], [scienceChoice], [performingArtsChoice], [artChoice], [businessChoice]]


#Prints the schedule as a 2D array so it appears as a single column and is easy to read
def printSchedule():
    for i in range(len(schedule,)):
        for j in range(len(schedule[i])):
            print(schedule[i][j], end='')
        print()

printSchedule()