import re
import random
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import math
import time
from draw import draw, draw_real, compute_coordinates

POPULATION = 500
ITERATION = 1000
BESTFITNESS = 100000
BESTROUTE = []
C5 = "Data/5cities.txt"     # wrong data
C15 = "Data/15cities.txt"
C26 = "Data/26cities.rtf"
C42 = "Data/42cities.rtf"   # wrong data
C48 = "Data/48cities.rtf"


def getData(filename):
    Distance = np.loadtxt(filename)
    return Distance


def generate_population(city_number, population_size):
    generation = []
    individual = []
    for i in range(city_number):
        individual.append(i)
    for i in range(population_size):
        for j in range(20):
            index_1 = random.randint(0, city_number - 1)
            index_2 = random.randint(0, city_number - 1)
            temp = individual[index_1]
            individual[index_1] = individual[index_2]
            individual[index_2] = temp
        generation.append(individual[:])
    return generation


def fitness_distance(tour, Distance):
    dist = 0
    for i in range(len(tour) - 1):
        u, v = tour[i], tour[i + 1]
        dist = dist + Distance[u][v]
    u, v = tour[len(tour) - 1], tour[0]
    dist = dist + Distance[u][v]
    return dist


def population_fitness(generation, Distance, X, Y):
    global BESTFITNESS, BESTROUTE
    fit_generation = []
    fit_prob_generation = []
    sum_fit = 0
    for i in range(len(generation)):
        fit = fitness_distance(generation[i], Distance)
        if fit < BESTFITNESS:
            BESTFITNESS = fit
            BESTROUTE = generation[i][:]
            # print('The best rout so far:', BESTROUTE)
            print('The best distance so far:', BESTFITNESS)
            print('pending...')
            draw_real(BESTROUTE, X, Y)
            time.sleep(1.5)
        fit_generation.append(1 / (fit - BESTFITNESS + 10))
    for i in range(len(fit_generation)):
        sum_fit += fit_generation[i]
    for i in range(len(fit_generation)):
        prob = fit_generation[i] / sum_fit
        fit_prob_generation.append(prob)
    return fit_prob_generation


def cum_fit_prob(generation, Distance, X, Y):
    prob = population_fitness(generation, Distance, X, Y)
    cum = 0
    cum_prob = []
    for i in range(len(prob)):
        cum += prob[i]
        cum_prob.append(cum)
    return cum_prob


def select(cum_prob):
    ran = random.random()
    if ran < cum_prob[0]:
        return 0
    for i in range(len(cum_prob) - 1):
        if ran > cum_prob[i] and ran <= cum_prob[i + 1]:
            index = i + 1
            return index


def crossover(route_1, route_2):
    start = random.randint(0, (len(route_1) - 1))
    end = random.randint((start + 1), len(route_1))
    new_route_1 = route_1[start:end]
    new_route_2 = route_2[start:end]
    for i in range(len(route_2)):
        if route_2[i] not in new_route_1:
            new_route_1.append(route_2[i])
    for i in range(len(route_1)):
        if route_1[i] not in new_route_2:
            new_route_2.append(route_1[i])
    return new_route_1, new_route_2


def mutate(P, route):
    p = random.random()
    length = len(route)
    if p <= P:
        index_1 = random.randint(0, length - 1)
        index_2 = random.randint(0, length - 1)
        temp = route[index_1]
        route[index_1] = route[index_2]
        route[index_2] = temp
    return route


def next_generation(generation, Distance, X, Y, P_mutate, P_crossover):
    new_generation = []
    cum_prob = cum_fit_prob(generation, Distance, X, Y)
    for i in range(int(len(generation) / 2)):
        parentA_index = select(cum_prob)
        parentB_index = select(cum_prob)
        if random.random() < P_crossover:
            child_1, child_2 = crossover(generation[parentA_index], generation[parentB_index])
            child_1 = mutate(P_mutate, child_1)
            child_2 = mutate(P_mutate, child_2)
            new_generation.append(child_1)
            new_generation.append(child_2)
        else:
            new_generation.append(mutate(P_mutate, generation[parentA_index]))
            new_generation.append(mutate(P_mutate, generation[parentB_index]))
    return new_generation


def genetic_algorithm(datasource):
    Distance = getData(datasource)
    X, Y = compute_coordinates(Distance)
    city_num = len(Distance)
    generation = generate_population(city_num, POPULATION)
    for i in range(ITERATION):
        generation = next_generation(generation, Distance, X, Y, P_mutate=0.15, P_crossover=0.8)
    print('The Best Route is: ', BESTROUTE)
    print('The Total Distance is: ', BESTFITNESS)
    print('complete!!')


genetic_algorithm(C26)
