from queue import Queue #importing modue 'Queue' from pacake 'queue'

my_queue = Queue() #defining an object/instance in the 'Queue' class

my_queue.put("Item1") #Inserting elements into the queue
my_queue.put("Item2")
my_queue.put("Item3")

item = my_queue.get() #getting the element from the queue
print("Deleted item: ",item) 

is_empty = my_queue.empty() #checking whether the queue is empty or not by using the '.empty()' function
print("Is queue empty? F/T: ",is_empty)