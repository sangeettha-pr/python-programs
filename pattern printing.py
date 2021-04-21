# -user input to enter the number of rows
# -ask the user to enter a boolean value
# -if bool==True then
#     print the pattern
#          *
#          * *
#          * * *
# -else bool==False then
#      print the pattern
#         * * *
#         * *
#         *


num = int(input("Enter the number of rows: "))
b=bool(int(input("enter 0 or 1")))

if b==True:
 for i in range(1,num + 1):
    print('*' *i)
else:
    for i in range(num,0,-1):
        print('*' *i)



