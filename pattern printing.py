num = int(input("Enter the number of rows: "))
b=bool(int(input("enter 0 or 1")))

if b==True:
 for i in range(1,num + 1):
    print('*' *i)
else:
    for i in range(num,0,-1):
        print('*' *i)



