n=int(input("n: "))
while(n!=0):
    if (n<=12):
        print(" You are a child")
        n=int(input("n: "))
    elif(n>12 and n<=18):
        print("Your a teen.")
        n=int(input("n: "))
    else:
        print("Your too old.")
        n=int(input("n: "))
