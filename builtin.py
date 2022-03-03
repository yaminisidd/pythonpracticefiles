import builtins
x=dir(builtins)
y=[]
for i in x:
    if i[0].isalpha():
        if i[0].islower():
            y.append(i)
print(y)
print('*'*30)
print(len(y))
