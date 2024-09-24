#empty set declaration 

x=set()
y=set()
#Dictionary
x={4,2,6,6}
y={8,9,10,22}

#set functions 
x.add(5)
x.remove(4)
print(x)

#difference , union ,intersection 

print(x.union(y)) 
print(x.difference(y)) 
print(x.intersection(y))