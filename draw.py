import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import math

route = [1, 2, 0, 3, 4]


def calculate_position(ox, oy, radius, num):
    alpha_unit = 2 * math.pi / num
    position = []
    for i in range(num):
        alpha = i * alpha_unit
        x = ox + radius * (math.cos(alpha))
        y = oy + radius * (math.sin(alpha))
        position.append([x, y])
    return position


def draw(route, ox=20, oy=20, radius=10, num=42):
    positions = calculate_position(ox, oy, radius, num)
    for i in range(len(positions)):
        plt.plot(positions[i][0], positions[i][1], 'ob')
    for index in range(len(route)):
        index2 = index + 1
        if index == len(route) - 1:
            index2 = 0
        plt.plot([positions[route[index]][0], positions[route[index2]][0]],[positions[route[index]][1], positions[route[index2]][1]], 'r')
    plt.show()

