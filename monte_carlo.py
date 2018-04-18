import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time

'''
def rollDice():
    roll = random.randint(1, 100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll > 50:
        return True
'''

def rollDice():
    roll = random.randint(1, 100)

    if roll <= 50:
        return True
    elif roll >=51:
        return False

def dAlembert(funds, initial_wager, wager_count):
    global profitability
    global da_profits
    global da_busts
    value = funds
    wager = initial_wager
    current_wager = 1
    previous_wager = 'win'
    previous_wager_amount = initial_wager

    while current_wager <= wager_count:
        if previous_wager == 'win':
            if wager == initial_wager:
                pass
            else:
                wager -= initial_wager

            if rollDice():
                value += wager
                previous_wager = 'win'
                previous_wager_amount = wager
            else:
                value -= wager
                previous_wager = 'loss'
                previous_wager_amount = wager
                if value <= 0:
                    da_busts += 1
                    break
        elif previous_wager == 'loss':
            wager = previous_wager_amount + initial_wager
            if (value - wager) <= 0:
                wager = value
            if rollDice():
                value += wager
                previous_wager = 'win'
                previous_wager_amount = wager
            else:
                value -= wager
                previous_wager = 'loss'
                previous_wager_amount = wager
                if value <= 0:
                    da_busts += 1
                    break
        current_wager += 1
    if value > funds:
        da_profits += 1
    # print(value)
    profitability += value



def multiple_bettor(funds, initial_wager, wager_count, colour='c'):
    global multiple_busts
    global multiple_profits

    value = funds
    wager = initial_wager

    wX = []
    vY = []

    current_wager  = 1
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
                    multiple_busts += 1
                    break
        elif previous_wager == 'loss':
            if rollDice():
                wager = previous_wager_amount * random_multiple
                if (value - wager) < 0:
                    wager = value
                value += wager
                wager = initial_wager
                previous_wager = 'win'
                wX.append(current_wager)
                vY.append(value)
            else:
                wager = previous_wager_amount * random_multiple
                if (value - wager) < 0:
                    wager = value
                value -= wager
                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)

                if value <= 0:
                    multiple_busts += 1
                    break
                previous_wager = 'loss'
        current_wager += 1
    # plt.plot(wX, vY, colour)
    if value > funds:
        multiple_profits += 1





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
        value = 0
        simple_busts += 1

    plt.plot(wX, vY, colour)
    if value > funds:
        value = 0
        simple_profits += 1

lower_bust    = 31.235
higher_profit = 63.208

sample_size = 1000
starting_funds = 10000

while True:
    # wager_size = 100
    # wager_count = 10000

    wager_size  = random.uniform(1.0, 1000.0)
    wager_count = random.uniform(10.0, 10000.0)

    profitability = 0.0
    da_profits    = 0
    da_busts      = 0
    da_sample_size = 10000
    counter = 1

    while counter <= da_sample_size:
        dAlembert(starting_funds, wager_size, wager_count)
        counter += 1

    ROI = profitability - (da_sample_size*starting_funds)
    total_invested = da_sample_size*starting_funds

    print('##########################################')
    print('Total invested', da_sample_size*starting_funds)
    print('ROI:', profitability - (da_sample_size*starting_funds))
    print('Total return', profitability)
    print('Bust rate:', (da_busts/da_sample_size)*100.00)
    print('Win rate:', (da_profits/da_sample_size)*100.00)
    print('Wager size:', wager_size)
    print('Wager count', wager_count)
    print('Wager size percentage:', (wager_size/starting_funds)*100.00)
