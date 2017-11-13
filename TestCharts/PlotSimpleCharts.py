#!/usr/bin/python3.6

import matplotlib.pyplot as plt

# https://matplotlib.org/examples/index.html

def autolabel(rects, ax):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')


def __plot_pie_chart():
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [20, 15, 10, 5]

    #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    explode = (0, 0, 0, 0)  # no explode
    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

def __plot_bar_chart():
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [20, 15, 10, 5]

    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(labels, sizes, width, color='g')
    # autolabel(rects1, ax)


__plot_pie_chart()
__plot_bar_chart()

plt.show()
