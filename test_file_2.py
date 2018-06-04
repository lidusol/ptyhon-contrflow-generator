import random
number = random.randint(0,100)
count = 0
while count < 7:
    guess = eval(input("enter your guess(between 0 and 100): "))
    if guess == number:
        print("you are correct")
        break
    elif guess > number:
        print("too high")
    else:
        print("too low")
    count += 1
if count == 7:
    print("you are a loser")
