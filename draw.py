import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import math


def compute_coordinates(Distance):
    d = Distance[0][1]
    X = [0, 0]
    Y = [0, d]
    a = Distance[0][2]
    b = Distance[1][2]
    y2 = ((a ** 2 - b ** 2) / d + d) / 2
    x2 = (a ** 2 - y2 ** 2) ** 0.5
    X.append(x2)
    Y.append(y2)
    for i in range(len(Distance) - 3):
        index = i + 3
        a = Distance[0][index]
        b = Distance[1][index]
        y = ((a ** 2 - b ** 2) / d + d) / 2
        x = (a ** 2 - y ** 2) ** 0.5
        if (x - x2) ** 2 + (y - y2) ** 2 != Distance[2][index] ** 2:
            x = 0 - x
        X.append(x)
        Y.append(y)
    return X, Y


def draw_real(route, Distance):
    X, Y = compute_coordinates(Distance)
    for i in range(len(X)):
        plt.plot(X[i], Y[i], 'ob')
    for index in range(len(route)):
        index2 = index + 1
        if index == len(route) - 1:
            index2 = 0
        plt.plot([X[route[index]], X[route[index2]]],
                 [Y[route[index]], Y[route[index2]]], 'r')
    plt.show()



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

