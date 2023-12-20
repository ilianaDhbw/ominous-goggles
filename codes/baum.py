num = 3
for i in range(1, num+2):
    print(" "*(2*num-i+3) + " ".join("*" for j in range(1, i+1)))
 
 
for i in range(1, num+2):
    print(" "*(2*num-i+1) + " ".join("*" for j in range(-1, i+1)))
 
 
for i in range(1, num+4):
    print(" "*(2*num-i) + " ".join("*" for j in range(-2, i+1)))
 
 
for i in range(1,num):
    print(" "*((2*num)) + " ".join("|" for j in range(3)))