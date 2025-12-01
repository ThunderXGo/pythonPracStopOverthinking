import random
import time

def funny(theInt):
    if theInt == 6:
        print("you lose bucko")
    else:
        print("you win")

alright = random.randint(1, 6)

funny(alright)