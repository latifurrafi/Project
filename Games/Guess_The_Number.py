import random

number = random.randint(1,10)

while True:
    guess = input("Get a Number between 1 to 10 : ")
    if guess == number:
        print("Congratulations")
    else:
        print("Sorry")
