def factorial2 (a):
  if a==0:
      return 1

  else:
      return a*factorial2(a-1)

a=int(input("enter the number"))
result=factorial2(a)
print("the factorial of",a,"is",result)
