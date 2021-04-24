a=10
b=-1
r= True

for i in range(a*2-2):
    if a>1 and r:
        a -= 1
        b += 2
        print(a*'-', b*'*', a*'-')
    elif a==1 and r:
        r = False
    elif a>0 and not r:
        a += 1
        b -= 2
        print(a*'-', b*'*', a*'-')
    elif a==20 and not r:
        r= True
