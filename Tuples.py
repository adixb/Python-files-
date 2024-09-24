x = [4 , " hi " , " True "]
# print("x without extension:",x)
x.extend([4,5,False,"hello",'Bro'])
# print("x after extension:",x)

y = x[:]

print(y)
