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
    def __init__(self):
        self.route=[]

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
        n = len(G)
        C = [[np.inf for i in range(n+1)] for j in range(2**n)  ] # initialize range to infinity 
        C[1][1] = 0
        
        Sets = range(1, 2**n) 
        for s in sorted(Sets, key=lambda x: bin(x).count('1')):
            if not s & 1: continue # subsets must contains city 0 
            
            for j in range(2, n+1):  
                if not (1 << (j - 1)) & s: continue # subsets must contain city j

                for i in range(1, n+1):
                    if i == j or not (1 << (i - 1)) & s: continue # subsets must contain i where i != j 
                    #print("subset: {}  j: {}  i: {}".format( s, j, i))
                    C[s][j] = min(C[s][j], C[s ^ (1 << (j - 1))][i] + G[j-1][i-1])
                            
        return min([(C[(2**n)-1][j] + G[0][j-1], j) for j in range(1, n)])
    
solver = Solver_DP()
d5 = solver.getData(data+C5)   
d15 = solver.getData(data+C15)
d26 = solver.getData(data+C26)
d42 = solver.getData(data+C42)
d48 = solver.getData(data+C48)

solver.dp_tsp(d15) 
                