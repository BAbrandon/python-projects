import random
print("Number guessing game\n \tby\nBrandon Ashworth\n\n")
guesses = 0
number = random.randint(1,100)
guess = "0"
while(guesses < 10):
    guess = input("Please guess a number 1-100: ")
    
    if(int(guess) < number):
        print("That guess was to low :p")
    if(int(guess) > number):
        print("That guess was to high :O")
    if(int(guess) == number):
        break
    guesses+=1
print("The number was "+str(number))
