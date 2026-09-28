# check whether a target value exists in tuple
numbers = (1, 2, 3, 4, 5)
for n in numbers:
    if n == 30:
        print("Found")
        break
else:
    print("Not found")

# another approach    
if 3 in numbers:
    print("found")
else:
    print("Not found")       

    
