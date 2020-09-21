n = int(input("Enter the number\n"))
b = int(input("Enter True'1' or False'0'\n"))

if b==True:
    for b in range(n):
        for e in range(b+1):
            print("*",end=" ")
        print()
    print("This is for True boolen")
if b==False:
    for b in range(n):
        for e in range(b,n-0):
            print("*",end=" ")
        print()
    print("This is for False boolen")