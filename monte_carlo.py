import random

def rollDice():
    roll = random.randint(1, 100)

    if roll == 100:
        print("Roll was 100, you lose.", sep="")
        return False
    elif roll <= 50:
        print("Roll was ", roll, ". Too low, you lose.", sep="")
        return False
    elif 100 > roll > 50:
        print("Roll was ", roll, ", you WIN.", sep="")
        return True



print(rollDice())
