quizPoints = 0

def question1():
    global quizPoints
    userInput = raw_input('How do you describe a variable that represents an input to a function? ')
    if userInput == 'parameter' or userInput == 'parameter variable':
        quizPoints = quizPoints + 1
    question2()

def question2():
    global quizPoints
    userInput = raw_input('How do you describe a variable that is only accessible in a code block? ')
    userInput = userInput.lower()
    if userInput == 'local variable' or userInput == 'local':
        quizPoints += 1
    getResults()
    
def getResults():
    global quizPoints
    total = quizPoints/22.0
    print total


 