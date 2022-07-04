import random
def guess(x):
    randomnum=random.randint(1,x)
    guess=0
    while guess!=randomnum:
        guess=int(input(f"Guess the number between 1,{x}: "))
        if guess>randomnum:
            print("more than the number, guess again")
        elif guess<randomnum:
            print("Less than the number,guess again")
        else:
            break
    return guess

x=int(input("Type the range from 1 to :" ))
print(f"the number is {guess(x)}")
