

''' 
For queue we have to import deque from collections 
and it has popleft method which allows us to deque from left
'''


from collections import deque

queue = deque([4, 5 , 8 , 9 , 10])

queue.append(16)
print(queue)
queue.append(12)
print(queue)
queue.popleft()
print(queue)
queue.pop()
print(queue)



 