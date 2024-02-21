my_tuple = (1,2,3,4,5)
my_list = list(my_tuple)

print(len(my_list))

my_list.insert(1,"Apple")
a = tuple(my_list)
print(a)

my_list = list(a)
my_list.remove("Apple")
my_tuple = tuple(my_list)
print(my_tuple)