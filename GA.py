import re
import random
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import math
from draw import draw

POPULATION = 200
ITERATION = 500
BESTFITNESS = 10000
BESTROUTE = []


def getData(filename):
    Distance = []
    with open(filename, 'r+') as file:
        lines = file.readlines()
        for l in lines:
            row = re.findall('\d+', l)
            results = list(map(int, row))
            Distance.append(results)
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


def fitness(tour, Distance):
    dist = 0
    for i in range(len(tour) - 1):
        u, v = tour[i], tour[i + 1]
        dist = dist + Distance[u][v]
    u, v = tour[len(tour) - 1], tour[0]
    dist = dist + Distance[u][v]
    return dist


def population_fitness(generation, Distance):
    global BESTFITNESS, BESTROUTE

    fit_generation = []
    fit_prob_generation = []
    sum_fit = 0
    for i in range(len(generation)):
        fit = fitness(generation[i], Distance)
        if fit < BESTFITNESS:
            BESTFITNESS = fit
            BESTROUTE = generation[i][:]
            print('The best rout so far:', BESTROUTE, '\nThe best distance so far:', BESTFITNESS)
            print('pending...')
            draw(BESTROUTE)
        fit_generation.append(1 / fit)
    for i in range(len(fit_generation)):
        sum_fit += fit_generation[i]
    for i in range(len(fit_generation)):
        prob = fit_generation[i] / sum_fit
        fit_prob_generation.append(prob)
    return fit_prob_generation


def cum_fit_prob(generation, Distance):
    prob = population_fitness(generation, Distance)
    cum = 0
    cum_prob = []
    for i in range(len(prob)):
        cum += prob[i]
        cum_prob.append(cum)
    return cum_prob


def select(generation, Distance):
    cum_prob = cum_fit_prob(generation, Distance)
    ran = random.random()
    if ran < cum_prob[0]:
        return 0
    for i in range(len(cum_prob) - 1):
        if ran > cum_prob[i] and ran <= cum_prob[i + 1]:
            index = i + 1
            return index


def crossover(route_1, route_2):
    start = random.randint(0, len(route_1) - 1)
    end = random.randint(start, len(route_1))
    new_route_1 = route_1[start:end]

    for i in range(len(route_2)):
        if route_2[i] not in new_route_1:
            new_route_1.append(route_2[i])

    return new_route_1


def mutate(P, route):
    r = random.randint(1, 100)
    p = r / 100
    length = len(route)
    if p <= P:
        index_1 = random.randint(0, length - 1)
        index_2 = random.randint(0, length - 1)
        temp = route[index_1]
        route[index_1] = route[index_2]
        route[index_2] = temp
    return route


def next_generation(generation, Distance, P_mutate, P_crossover):
    new_generation = []
    for i in range(len(generation)):
        parentA_index = select(generation, Distance)
        parentB_index = select(generation, Distance)
        child = crossover(generation[parentA_index], generation[parentB_index])
        child = mutate(P_mutate, child)
        new_generation.append(child)
    return new_generation


def genetic_algorithm(datasource="Data/CityData.rtf"):
    generation = []
    Distance = getData(datasource)
    city_num = len(Distance)
    generation = generate_population(city_num, POPULATION)
    for i in range(ITERATION):
        generation = next_generation(generation, Distance, P_mutate=0.05, P_crossover=0.8)
    print('The Best Route is: ', BESTROUTE)
    print('The Total Distance is: ', BESTFITNESS)
    print('complete!!')



genetic_algorithm(datasource="Data/CityData.rtf")
