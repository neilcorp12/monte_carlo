import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time

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

def doubler_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    wX = []
    vY = []

    # Gambler's fallacy - if you lose, double the bet expecting a greater chance
    # of winning
    current_wager = 1
    previous_wager = 'win'
    previous_wager_amount = initial_wager

    while current_wager <= wager_count:
        if previous_wager == 'win':
            print('We won the last wager')
            if rollDice():
                value += wager
                print(value)
                wX.append(current_wager)
                vY.append(value)
            else:
                value -= wager
                previous_wager = 'loss'
                print(value)
                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)

                if value < 0:
                    print('we went broke after'.current_wager, 'bets')
                    break
        elif previous_wager == 'loss':
            print('Double the bet because we lost last time.')
            if rollDice():
                wager = previous_wager_amount * 2
                print('We won', value)
                value += wager
                print(value)
                wager = initial_wager
                previous_wager = 'win'
                wX.append(current_wager)
                vY.append(value)
            else:
                wager = previous_wager_amount * 2
                print("We lost wager", wager)
                value -= wager
                if value < 0:
                    print("We went broke after", current_wager,'bets')
                    break
                print(value)
                previous_wager = 'loss'
                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)
        current_wager += 1
    print(value)
    plt.plot(wX, vY)

doubler_bettor(10000, 100, 1000)
plt.show()

time.sleep(666)

def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    # Wager and value lists
    wX = []
    vY = []

    current_wager = 1

    while current_wager <= wager_count:
        if rollDice():
            value += wager
            wX.append(current_wager)
            vY.append(value)
        else:
            value -= wager
            wX.append(current_wager)
            vY.append(value)

        current_wager += 1
    if value < 0:
        value = "broke"
    # print("Funds:", value)

    plt.plot(wX, vY)
x = 0

while x < 20:
    simple_bettor(10000, 100, 100000)
    x += 1

# Show the chart
plt.ylabel('Account Value')
plt.xlabel('Wage Count')
plt.show()
