import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time

sample_size = 100
starting_funds = 10000
wager_size = 100
wager_count = 1000

def rollDice():
    roll = random.randint(1, 100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll > 50:
        return True

def doubler_bettor(funds, initial_wager, wager_count, colour='m'):
    value = funds
    wager = initial_wager
    global doubler_busts
    global doubler_profits
    wX = []
    vY = []

    # Gambler's fallacy - if you lose, double the bet expecting a greater chance
    # of winning
    current_wager = 1
    previous_wager = 'win'
    previous_wager_amount = initial_wager

    while current_wager <= wager_count:
        if previous_wager == 'win':
            if rollDice():
                value += wager
                wX.append(current_wager)
                vY.append(value)
            else:
                value -= wager
                previous_wager = 'loss'
                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)

                if value <= 0:
                    doubler_busts += 1
                    break
        elif previous_wager == 'loss':
            if rollDice():
                wager = previous_wager_amount * 2
                if (value - wager) < 0:
                    wager = value
                value += wager
                wager = initial_wager
                previous_wager = 'win'
                wX.append(current_wager)
                vY.append(value)
            else:
                wager = previous_wager_amount * 2
                if (value - wager) < 0:
                    wager = value
                value -= wager
                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)

                if value <= 0:
                    doubler_busts += 1
                    break
                previous_wager = 'loss'
        current_wager += 1
    plt.plot(wX, vY, colour)
    if value > funds:
        doubler_profits += 1

def simple_bettor(funds, initial_wager, wager_count, colour='k'):
    global simple_profits
    global simple_busts
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
    if value <= 0:
        # value = "brok e"
        simple_busts += 1

    plt.plot(wX, vY, colour)
    if value > funds:
        simple_profits += 1

x = 0
simple_profits  = 0.0
simple_busts    = 0.0
doubler_profits = 0.0
doubler_busts   = 0.0

while x < sample_size:
    simple_bettor(starting_funds, wager_size, wager_count)
    doubler_bettor(starting_funds, wager_size, wager_count)
    x += 1

print("Simple bettor profit ratio:", (simple_profits/sample_size)*100.00)
print("Doubler bettor profit ratio:", (doubler_profits/sample_size)*100.00)

plt.axhline(0, color='r')
plt.ylabel('Account Value')
plt.xlabel('Wage Count')
plt.show()
