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
    
d5 = getData(data+C5)   
d15 = getData(data+C15)
d26 = getData(data+C26)
d42 = getData(data+C42)
d48 = getData(data+C48)

dp_tsp(d15) 
                