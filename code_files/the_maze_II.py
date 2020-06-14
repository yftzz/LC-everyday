class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        from queue import PriorityQueue
        visited = set()
        openList = PriorityQueue()
        openList.put((0, start[0], start[1]))
        actions = ((1,0),(-1,0),(0,1),(0,-1))
        m, n = len(maze), len(maze[0])
        
        while openList.qsize():
            cost, x, y = openList.get()
            if [x, y] == destination:
                return cost
            visited.add((x,y))
            for dx, dy in actions:
                newX, newY = x, y
                newCost = cost
                while 0 <= newX + dx < m and 0 <= newY + dy < n and maze[newX + dx][newY + dy] == 0:
                    newX += dx
                    newY += dy
                    newCost += 1
                if not (newX, newY) in visited:
                    openList.put((newCost, newX, newY))
        return -1
            
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        visited = set()
        openList = [(0, start[0], start[1])]
        actions = ((1,0),(-1,0),(0,1),(0,-1))
        m, n = len(maze), len(maze[0])
        
        while openList:
            cost, x, y = heapq.heappop(openList)
            if [x, y] == destination:
                return cost
            visited.add((x,y))
            for dx, dy in actions:
                newX, newY = x, y
                newCost = cost
                while 0 <= newX + dx < m and 0 <= newY + dy < n and maze[newX + dx][newY + dy] == 0:
                    newX += dx
                    newY += dy
                    newCost += 1
                if not (newX, newY) in visited:
                    heapq.heappush(openList, (newCost, newX, newY))
        return -1
            
