import sys 
import subprocess
import time 

from tsp_brute import Solver_Tsp_Brute
from DP import Solver_DP
from GA import getData, genetic_algorithm

d = "Data/"
DRAW = False 

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
def timer(alg, data):
    tic = time.perf_counter()
    if alg == "en": 
        solver_brute = Solver_Tsp_Brute(getData(data))
        solver_brute.tsp_brute_force()
    elif alg == "dp":
        solver = Solver_DP(data)
        solver.dynamic_algorithm()
    elif alg == "ga": 
        genetic_algorithm(data, DRAW) 
    toc = time.perf_counter()
    print("Runtime is "+ str(toc - tic)+" seconds")



opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")] 
    
if "-d" in opts: 
    DRAW = True
if "-en" in opts:
    # launches enumeration algorithm 
    timer("en", args[0])
elif "-dp" in opts:
    # launches dynamic programming algorithm 
    timer("dp", args[0])
elif "-ga" in opts:
    # launches genetic algorithm 
    timer("ga", args[0])

else:
    raise SystemExit("Usage: " +str(sys.argv[0])+" (-en | -dp | -ga) <data>...")
    

