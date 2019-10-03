def startStory():
    print 'Welcome to my morning!'
    decision1()

def decision1():
    userChoice = raw_input('Shower or breakfast?')
    if userChoice == 'Shower' or userChoice =='shower':
        decision4()
    else:
        decision3()

def decision3():
    userChoice = raw_input('Rice chex or oatmeal?')
    if userChoice == 'Rice chex' or userChoice =='rice chex':
        decision6()
    else:
        decision5()

def decision4():
    print 'The water isn\'t working'
    print 'Go eat your breakfast.'
    decision5()

def decision5():
    print 'Oatmeal sounds good but you have no toppings for it. Bummer.'
    #finish this here!

def decision6():
    print 'yum, rice chex! Good choice'
     #finish this here!