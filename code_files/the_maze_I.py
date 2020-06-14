class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        from collections import deque
        openList = deque()
        openList.append(tuple(start))
        actions = ((1,0), (-1,0), (0,1),(0,-1))
        visited = set()
        m,n=len(maze), len(maze[0])
        
        while openList:
            x, y = openList.pop()
            visited.add((x, y))
            if [x, y] == destination:
                return True
            # print(x, y)
            for dx, dy in actions:
                newX, newY = x, y
                while 0 <= newX + dx < m and 0 <= newY + dy < n and maze[newX + dx][newY + dy] != 1:
                    newX += dx
                    newY += dy
                if not (newX, newY) in visited:
                    openList.append((newX, newY))
        return False
    
  


        
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        m,n = len(maze), len(maze[0])
        destination = tuple(destination)
        def search(x, y):
            if (x, y) == destination:
                return True
            if (x, y) in visited:
                return False
            visited.add((x, y))
            actions = [(1, 0), (-1, 0), (0, -1), (0, 1)]            
            for dx, dy in actions:
                newX, newY = x, y
                while 0 <= newX + dx < m and 0 <= newY + dy < n and maze[newX + dx][newY + dy] == 0:
                    newX += dx
                    newY += dy
                if search(newX, newY):
                    return True
        return search(*start)
            