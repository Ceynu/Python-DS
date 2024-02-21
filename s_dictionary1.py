thisdict = dict(name = "John", age = 36, country ="Norway" )
print(thisdict)

a = {"Brand" :"Ford", "Model" : "Mustang" , "year" : 1964}
print(a)

x = a.get("Model")
print(x)

y = a.keys()
print(y)

z = a.values()
print(z)

t = a.items()
print(t)

a.update({"Model" : "Renault"})
print(a)

a["Type"] = "Racing"
print(a)

a["color"] = ["Matte Navy Blue","Matte Black"]
print(a)