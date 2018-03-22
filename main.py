print("SPYCHAT")
print("Welcome to SPYCHAT")
spy_name=input('What/s your name')
print(spy_name)
print("Welcome " + spy_name + " How are you?")
type(spy_name)
spy_salutation=input("What should we call you(Mr./Miss.)")
print(spy_salutation)
print(spy_salutation +" " + spy_name)
print("Alright "+ spy_salutation +" " + spy_name + " I would like to know a little bit more about you")
spy_account=input("Tell which account would you prefer to choose(default/new)")
if(spy_account=="new"):
    spy_name = input("Whats your name")
    print(spy_name)
    print("Welcome " + spy_name + " How are you?")
    type(spy_name)
    spy_salutation = input("What should we call you(Mr./Miss.)")
    print(spy_salutation)
    print(spy_salutation + " " + spy_name)
    print("Alright " + spy_salutation + " " + spy_name + " I would like to know a little bit more about you")
else:
    exit(0)
    ############################# project 2 solving the error when adding a string and an integer########################

    len("Hello")
    len("My name is Harshika Gupta")
    len("My name is Harshika Gupta") > 0
     name = "Miss. Harshika Gupta"
    if len(name) > 0 :

        new_message = 'Hurry!Name is not empty'
        print(new_message)
        if len("") > 0 :
            print("print the statement if it is false")
            print("This second if is like a reply comment to parent comment on line 2")
            print("The parent of this comment is on line 2")
            if len("Hello World to Sypchat") > 0 :
                print("It has an advantage in today\s world")
                print("Python is easy to understand if and only if we give our full dedication to understand it")
                if len(" ") > 0 :
                    print("See how it shows an output in console")
                    print("This is like a comment on the original/main post")
print("This print statement is outside all the if statements above.")
print("This is like another new comment.")
#####################################try with space or with name####################################3


name = "Miss. Harshika"
if len(" ") > 0 :
    print("print the statement if it is true or false")
    print("This first if is like a reply comment to parent comment on line 2")
    print("The parent of this comment is on line 2")
    if len("cricket") > 0 :
        print("It is an outdoor game")
        print("This print statement is outside all the if statements above.")
        print("This is like another new comment.")
#####################################let's run the code with the spy_salutation#####################################

spy_name = input("Welcome to spy chat, you must tell me your spy name first: ")
if len(spy_name) > 0 :
    print("Welcome ' + spy_name + '. Glad to have you back with us.")
    spy_salutation = input("Should I call you Mister or Miss?: ")
    spy_name = spy_salutation + " " + spy_name
    print("Alright " + spy_salutation + " " + spy_name + " I would like to know a little bit more about you")
else:
    print("A spy needs to have a valid name. Try again please.")
    #################################try without input the statement in the variable spy_name################################
spy_name = input()
if len("") > 0 :
    print("Welcome ' + spy_name + '. Glad to have you back with us.")
    spy_salutation = input("Should I call you Mister or Miss?: ")
    spy_name = spy_salutation + " " + spy_name
    print("Alright " + spy_salutation + " " + spy_name + " I would like to know a little bit more about you")
else:
    print("A spy needs to have a valid name. Try again please.")
    ##################################code shows that user ask to provide their age; with an and statement###########################
      spy_age = 0
      spy_rating = 0.0
      spy_is_online = False
    spy_age = int(input("What is your age?"))
if spy_age > 17 and spy_age < 60:
          spy_rating = input("What is your spy rating?")
      else:
          print("Sorry you are not of the correct age to be a spy")
          #############with an or statement##############################################
          spy_age = int(input("What is your age?"))
          if spy_age > 31 or spy_age < 70:
              spy_rating = input("What is your spy rating?")
          else:
              print("Sorry you are not of the correct age to be a spy")

              spy_rating = float(input("What is your spy rating?"))
              if spy_rating > 4.5:
                  print("Great ace!")
              elif spy_rating > 3.5 and spy_rating <= 4.5:
                  print("You are one of the good ones.")
              elif spy_rating >= 2.5 and spy_rating <= 3.5:
                  print("You can always do better.")
              else:
                  print("We can always use somebody to help in the office.")
                  spy_name = input("Welcome to spy chat, you must tell me your spy name first: ")
                  spy_age = str(input("What is your age?"))
                  spy_rating = str(input("What is your spy rating?"))
                  spy_is_online = True
                  print("Authentication complete. Welcome " + spy_name +" age: " + spy_age + " and rating of: " + spy_rating + " Proud to have you onboard")




