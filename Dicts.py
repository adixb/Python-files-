x = {'NewDelhi':110019,
     'Rohini':110035,
     'Naraina':110055,
     'Saket':110017,
     }

print(x.values()) #dictionary values only 
print(list(x.keys())) #list of dictionary keys 
print(x) #dictionary full with key and values 

#iterating over the dictionary
for key,value in x.items():
    print(key,value)
    
    
print("\nNew Loop Values: \n")
    
#the above code can also be written as 
for key in x:
    print(key,x[key])    