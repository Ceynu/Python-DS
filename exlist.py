mylist = ["Apple","Banana","Orange"]
print(len(mylist))

mylist.insert(1,"strawberry") #to add an element to a specified position of a list.
print(mylist)

mylist.append("Cherry") #to add an element to the end of a list.
print(mylist)

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list1.extend(list2) #to join another list(list2) to the end of one list(lis1).
print(list1)

mylist.remove("strawberry") #remove the specified element form the string
print(mylist)

mylist.pop(3) #remove the element of the specified index from the list
print(mylist)

mylist.pop() #
print(mylist)

del mylist[1]
print(mylist)