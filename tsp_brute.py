import numpy as np

class Solver_Tsp_Brute():
    def __init__(self,arr):
        self.arr = arr
        self.num = len(arr)
        self.result = {}
        self.route=[]
        self.total_set = set([i for i in range(self.num)])

    def _brute_force(self,last_visit=0 , visited=[0],sum_dist=0):
        '''
        select next city to visit recursively
        :param last_visit: last city visited
        :param visited: visited cities in order, list type
        :param sum_dist: sum of distance from start to last visited city
        :return:
        '''
        unvisited = self.total_set-set(visited)
        if not len(unvisited):
            route = (i+1 for i in visited)
            self.result[route] = sum_dist+self.arr[last_visit][0]

        else:
            for v in unvisited:
                self._brute_force(v,visited+[v],sum_dist+self.arr[last_visit][v])

    def tsp_brute_force(self):
        '''
        Solve tsp using brute force, calculate (n-1)! routes and output the minimum.
        :return:
        '''
        self._brute_force()
        min_route = min(self.result,key=self.result.get)
        min_sum_dist = self.result[min_route]
        return list(min_route),min_sum_dist


file_name = 'Data/5cities.txt'
arr = np.loadtxt(file_name)
solver_brute = Solver_Tsp_Brute(arr)
route, dist = solver_brute.tsp_brute_force()
print('Route: ',route,'\nDistance: ', dist)

