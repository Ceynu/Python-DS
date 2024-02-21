a = {"Brand" : "ford" , "Model" : "Mustang", "Year" : 1964}
print(a)

if "Model" in a:
    print("Yes , Model is present in the key list")

a["Year"] = 1980
print(a)

a.update({"Type" : "Racing"})
print(a)

a["Color"] = ["Matte Navy Blue","Matte Black"]
print(a)

a.pop("Type")
print(a)

a.popitem()
print(a)

del a["Year"]
print(a)

a.clear()
print(a)