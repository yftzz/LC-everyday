class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        
        father = defaultdict(set)
        child = defaultdict(set)
        
        for course, pre in prerequisites:
            child[pre].add(course)
            father[course].add(pre)
        res = []
        stack = [i for i in range(numCourses) if not father[i]]
        stack = deque(stack)
        while stack:
            curr = stack.popleft()
            res.append(curr)
            for course in child[curr]:
                father[course].remove(curr)
                if not father[course]:
                    stack.append(course)
                
                    
        return res if len(res) == numCourses else []
            
        