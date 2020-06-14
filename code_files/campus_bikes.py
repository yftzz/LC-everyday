from queue import PriorityQueue
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        workerQ = [PriorityQueue()] * len(workers)
        for i, (x, y) in enumerate(workers):
        	for j, (m, n) in enumerate(bikes):
        		workerQ[i].put((abs(x - m) + abs(y - n), i, j))
        res = [-1] * len(workers)
        used = list()

        currQ = PriorityQueue()
        for q in workerQ:
        	currQ.put(q.get())

        while len(used) < len(workers):
        	pair = currQ.get()
        	if res[pair[1]] >= 0 or pair[2] in used:
        		currQ.put(workerQ[pair[1]].get())
        	else:
        		res[pair[1]] = pair[2]
        		used.append(pair[2])
        return res



class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []
		# create a list of distances for each worker-bike combination, 
		# put distance in the first tuple element and worker index in second tuple element 
		# and bike index in third. we will sort this list of tuples later.
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                distance = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                distances.append((distance, i, j))
				
	    # Sort the tuples
        distances.sort()

        result = [-1] * len(workers)
        bike_taken = set() # Mark a bike as taken by putting it in this set as we traverse the tuples from shortest distance onwards.
        for distance, i, j in distances:
            # print(distance, i, j)
            if result[i] == -1 and j not in bike_taken:
                result[i] = j
                bike_taken.add(j)
        return result