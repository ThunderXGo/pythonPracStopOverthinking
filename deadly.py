import random
import time

def funny(theInt):
    if theInt == 6:
        print("you lose bucko (your harddrive is also gone), you rolled " + str(theInt))
    else:
        print("you win, you rolled " + str(theInt))

alright = random.randint(1, 6)

funny(alright)