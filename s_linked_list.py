class Node:
    def __init__(self,data):
        self.data = data #  reference to the data 
        self.address = None #  Address of the node in memory
  
class LinkedList:
    def __init__(self):
        self.head = None # Head of linked list

    def is_empty(self):
        return self.head is None
    
    def append(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current_node = self.head
            while current_node.address:
                current_node = current_node.address
            current_node.address = new_node

    
    def display(self):
        elements =[]
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.address
        print("->".join(map(str,elements)))



my_linked_list =LinkedList()

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print("Linked list:")
my_linked_list.display()



