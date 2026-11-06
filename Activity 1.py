import random
p = 4
y = random.randint(0, 10)
while p>=0:
    p = p-1
    try:
        x = int(input("Try and guess the computer's number from 0 to 10. You have five tries: "))
        if x == y:
            print(f"Good guess! the number was {x}.")
        else:
            print(f"Unlucky! Guess again!.")
    except:
        print("Enter a digit!")