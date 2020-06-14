import time
from collections import deque
from Queue import Queue

number = 100000
start = time.time()
a = list()
for i in range(number):
	a.append((i))
for _ in range(number):
	a.pop()

print('time for built-in list is {}'.format(time.time()-start))

start = time.time()
a = deque()
for i in range(number):
	a.append((i))
for _ in range(number):
	a.pop()

print('time for deque is {}'.format(time.time()-start))


start = time.time()
a = Queue()
for i in range(number):
	a.put((i))
for _ in range(number):
	a.get()

print('time for deque is {}'.format(time.time()-start))