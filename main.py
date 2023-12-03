from random import randint

#takes input from the user
def guess():
    '''
    Function takes in the guess from the user and ensures that the guess is within the specified parameters
    '''
    while True:
        try:
            user_guess = (int(input("Type a number between 1-10: " )))
            if user_guess <=10:
                return user_guess
            else:
                print("Please input an integer between 1-10 to continue")
                break
        except ValueError:
            print(f"There is an error with {guess}, please input an integer between 1-10.")





computer = randint(1,10)

while True:
    user_guess = guess()
    if user_guess == computer:
        print(f"You guessed {user_guess} and the computer guessed {computer} . Congrats you guessed the same!")
        break
    else:
        print(f"You guessed {user_guess} and the computer guessed {computer} . Try again.")

