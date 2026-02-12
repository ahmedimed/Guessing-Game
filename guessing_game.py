import random
number = random.randint(1, 100)
while True :
    guess = int(input("try to guess the number: "))
    if guess < 0 or guess > 100:
         print(" enter a number between 0 and 100")
         continue

    if guess == number:
        print ("you guessed right")
        break
    elif guess < number:
        print ( " too low ")
    elif guess > number :
        print ( "too high ")
