#for loops 
#range(start,stop,step)




# for  i in range(2,8,1):
#     print(i)
    

#range can be in the form of array 
# x=[1,2,3,4,5]

# for i in x:
#     print(i)
    
#enumerate()
# x=[4,5,6,7]

# for i ,element in enumerate(x):
#     print(i,element)
    
    
#while loop 
x = [1, 2, 3, 4, 5]

i = 0

while i < len(x):  # Use len(x) instead of a fixed number
    print(x[i])
    i += 1  # This is equivalent to i = i + 1
