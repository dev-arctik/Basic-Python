#triangle

#1
for i in range(0,10):
    for j in range(0,i+1):
        print('* ', end='')
    print(end='\n')


#2
for i in range(0,10):
    print('* '*i)
    

#3
n=11

for i in range(0,11):
    for j in range(0,n):
        print(end=' ')

    n=n-1

    for k in range(0,i):
        print(end='* ')

    print(end='\n')


#4

n=11

for i in range(0,11):
    for j in range(0,2*n):
        print(end=' ')

    n=n-1

    for k in range(0,i):
        print(end='* ')

    print(end='\n')




