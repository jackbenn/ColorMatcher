import matplotlib.pyplot as plt

import random
import time
import datetime

def display_colors(color1, color2, ax):
    ax.fill([0, 0, 1, 1], [0, 1, 1, 0], color=color1, alpha=1)
    ax.fill([1, 1, 2, 2], [0, 1, 1, 0], color=color2, alpha=1)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    #plt.axes([0,0,1,1], frameon = True)
    ax.axis('off')
    plt.draw()

def run_session(datafile):

    name = input("What's your name? ").strip()
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    while True:
        color1 = generate_random_color()
        color2 = generate_random_color()
        display_colors(color1, color2, ax)
        plt.draw()
        plt.pause(0.001)
        rating = input("How well do these colors match? (1-5) ").strip()
        while rating not in ['1', '2', '3', '4', '5']:
            rating = input("Please enter a number between 1 and 5?").strip()
        with open(filename, 'a') as f:
            print(f'{name},{time},{color1[0]},{color1[1]},{color1[2]},{color2[0]},{color2[1]},{color2[2]},{rating}', file=f)

def generate_random_color():
    return tuple(random.random() for _ in range(3))

if __name__ == '__main__':
    filename = '../data/ratings'

    fig, ax = plt.subplots(figsize=(4, 3))
    plt.ion()
    plt.show()

    run_session(filename)