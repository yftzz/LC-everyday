class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def printTree(t):
    if not t:
        return
    res = ''
    res += str(t.value)
    s1 = s2 = []
    s2.append(t.right)
    s2.append(t.left)
    b = False
    
    
    while len(s1) and len(s2):
        if b:
            while s1:
                node = s1.pop()
                if node:
                    res += ' > ' + str(node.value)
                    s2.append(node.right)
                    s2.append(node.left)
        else:
            while s2:
                node = s2.pop()
                if node:
                    print(node.value)   
                    res += ' > ' + str(node.value)
                    s1.append(node.left)
                    s1.append(node.right)
        b = not b
        
    print(res)

tree = Node(1, Node(2, Node(5,None,None), None), Node(3, Node(7,None, None), None))
printTree(tree)