import networkx as nx
import re
import random
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import math
import time
from draw import draw, draw_real, compute_coordinates

data = "Data/"
C5 = "5cities.txt"     
C15 = "15cities.txt"
C26 = "26cities.rtf"
C42 = "42cities.rtf"   
C48 = "48cities.rtf"


class Solver_DP(): 
    def __init__(self, data):      
        self.distances = self.getData(data)
        self.n = len(self.distances)      
        self.prev=[[-1 for i in range(self.n+1)] for j in range(2**self.n) ]
        self.itinerary = []

    def getData(self, filename):
        Distance = []
        
        with open(filename, 'r+') as file:
            lines = file.readlines()
        
        for l in lines:
            row = re.findall('\d+', l)
            results = list(map(int, row))
            Distance.append(results)
            
        return Distance


    def dp_tsp (self, G): 
        n = self.n
        C = [[np.inf for i in range(n+1)] for j in range(2**n) ] # initialize range to infinity 
        C[1][1] = 0
        
        Sets = range(1, 2**n) 
        for s in sorted(Sets, key=lambda x: bin(x).count('1')):
            if not s & 1: continue # subsets must contains city 0 
            
            for j in range(2, n+1):  
                if not (1 << (j - 1)) & s: continue # subsets must contain city j

                for i in range(1, n+1):
                    if i == j or not (1 << (i - 1)) & s: continue # subsets must contain i where i != j 
                    #print("subset: {}  j: {}  i: {}".format( s, j, i))
                    
                    old = C[s][j]
                    new = C[s ^ (1 << (j - 1))][i] + G[j-1][i-1]
                    if old > new: 
                        C[s][j] = new 
                        self.prev[s][j] = i
        
        final  = min([(C[(2**self.n)-1][j] + G[j-1][0], j) for j in range(1, self.n)])
        last = final[1]
        rem = (2**self.n)-1
        
        #print(self.prev)
        # build iternary from the best path data 
        for i in range(0,self.n): 
            
            self.itinerary.append(last)
            old_last = last 
            last = self.prev[rem][last]      
            rem = rem ^ (1 << (old_last - 1))
            
        self.itinerary.reverse()
        
        return final
    
    
    def dynamic_algorithm(self):
        X, Y = compute_coordinates(self.distances)
        result = self.dp_tsp(self.distances)
        return result, self.itinerary
    
solver = Solver_DP(data+C5)
x, y = solver.dynamic_algorithm()
print(x,y)
                