x=input("enter your string:").casefold()
y=""
i=len(x)-1
while i >=0:
    y+=x[i]
    i =-1
if x==y:
   print("given string is palindrom string")
else:
    print("given string is not a palindrom string")
