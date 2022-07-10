import random

print("Welcome to our random number guesser game")
print("")

guesses = 0

while (True):
    user_input = input("Enter the number upto which you would like to generate random numbers:")
    if (user_input.isdigit()):
            user_input = int(user_input)
            if (user_input == 0):
                print("Kindly enter a number more than 0")
            else:     
                random_num = random.randint(0,user_input)
            
                while(True):
                    guesses +=1
                    user_ans = input("Guess the number:")
                    if user_ans.isdigit():
                        user_ans = int(user_ans)
                    
                        if (user_ans == random_num):
                            print("Your Guess Was Correct")
                            if (guesses == 1):
                                print(f"You took {guesses} guess")
                                quit()
                            else:
                                print(f"You took {guesses} guesses")
                                quit()
                        else:
                             print("Your Guess Was Wrong")
                    else:
                        print("Kindly enter a valid number")
            
    else:
         print("Kindly enter a valid number")
