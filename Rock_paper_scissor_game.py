user_option=input("enter Rock/Paper/Scissor: ")
computer_option=['Rock','Paper','Scissor']
while True:
    for option in computer_option:
     options=computer_option(option)
     if options=='Rock' and user_option=='Rock':
        print("Draw the game!")
     elif options=='Rock' and user_option=='Paper':
        print("User won!")
     elif options=='Rock' and user_option=='Scissor':
        print("Computer won!")
