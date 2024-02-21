a = {"Brand" : "ford" , "Model" : "Mustang", "Year" : 1964}
print(a)

for i in a:
    print(i)

for i in a.keys():
    print(a[i])

for i in a:
    print(a[i])

for i in a.values():
    print(i)

b = a.copy()
print(b)

c = dict(a)
print(c)