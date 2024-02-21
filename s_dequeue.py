from collections import deque

my_dequeue = deque()

my_dequeue.append("Item 1")
my_dequeue.append("Item 2")
my_dequeue.append("Item 3")

item = my_dequeue.pop()

print("Deleted item: ",item)

# is_empty = my_dequeue.empty() #checking whether the queue is empty or not by using the '.empty()' function
# print("Is queue empty? F/T: ",is_empty)


