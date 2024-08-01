import random
import math
#Taking inputs
lower = int(input("Enter Lower bound:-\n"))
upper = int(input("Enter Upper bound:-\n"))

#generating random number between the lower and upper and lower bound
x = random.randint(lower,upper)
A = round(math.log(upper-lower,2))
print("\n\tYou have only ",A," chances to guess the integer!\n")

#Initializing the number of guesses.
count = 0

# for calculation of minimum number of guesses depends upon range
while count < A:
    count+=1

    # taking guessing number as input
    guess = int(input("Guess a number:-"))

    # condition testing
    if x == guess:
        print("Congratulations you did it in ",count,"try")
        #once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too large")

#If guessing is more than required number
if count >= A:
    print("\nThe number is ",x)
    print("\n Better luck next time!")