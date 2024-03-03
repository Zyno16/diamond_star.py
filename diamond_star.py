l = int(input("enter the number: "))
space = l -1
star = 1
for i in range(1,l*2):
    for j in range (0,space):
        print("  ",end ="")
    for j in range(1,star*2):
        print("* ",end ="")

    if i < l:
        space -= 1
        star += 1

    else:
        space += 1
        star -= 1
    print()

    
                 
    


    