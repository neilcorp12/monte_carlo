import matplotlib
import matplotlib.pyplot as plt
import csv

def graph():
    with open('monteCarloLiberal.csv','r') as montecarlo:
        trials = csv.reader(montecarlo, delimiter=',')

        for bettor in trials:
            percent_ROI = float(bettor[0])
            wager_size_percent = float(bettor[1])
            wager_count = float(bettor[2])
            line_color = bettor[3]

            plt.scatter(wager_size_percent, wager_count, color=line_color)
    plt.show()

graph()
