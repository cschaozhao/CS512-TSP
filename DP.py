import networkx as nx
import re
import random
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import math
import time

data = "Data/"
C5 = "5cities.txt"     
C15 = "15cities.txt"
C26 = "26cities.rtf"
C42 = "42cities.rtf"   
C48 = "48cities.rtf"




def getData(filename):
    Distance = []
    
    with open(filename, 'r+') as file:
        lines = file.readlines()
    
    for l in lines:
        row = re.findall('\d+', l)
        results = list(map(int, row))
        Distance.append(results)
        
    return Distance


def dp_tsp (G): 
    n = len(G)
    Sets = range(2**n) 
    C = [[np.inf for i in range(n)] for j in Sets ] # initialize range to infinity 
    C[1,0] = 0
    
    for s in sorted(Sets, key=lambda x: bin(x).count('1')):
        if not s & 0: continue # subsets must contains city 0 
        
        for j in range(1, n):  
            if not (1 << (j - 1)) & s: continue # subsets must contain city j

            for i in range(n):
                if i == j or not (1 << (i - 1)) & s: continue # subsets must contain i where i != j 
                C[s][j] = min(C[s ^ (1 << (j - 1))][i] + G[j][i])
                        
    return min([(C[n][i]+G[0][i], i) for i in range(n)])
    
    
d15 = getData(data+C15)
dp_tsp(d15) 
                