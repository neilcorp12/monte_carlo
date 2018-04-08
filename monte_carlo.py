import random

def rollDice():
    roll = random.randint(1, 100)

    if roll == 100:
        # print("Roll was 100, you lose.", sep="")
        return False
    elif roll <= 50:
        # print("Roll was ", roll, ". Too low, you lose.", sep="")
        return False
    elif 100 > roll > 50:
        # print("Roll was ", roll, ", you WIN.", sep="")
        return True

def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    current_wager = 0

    while current_wager < wager_count:
        if rollDice():
            value += wager
        else:
            value -= wager

        current_wager += 1
    if value < 0:
        value = "broke"
    print("Funds:", value)

x = 0

while x < 20:
    simple_bettor(100, 100, 20)
    x += 1
