#find prime factors
n=int(input('Enter a number:'))
d=2
print('Prime factors are:\')
while n>1 and d<=n:
    if n%d==0:
        print(d)
        n=n/2
        continue #from here the code will go back to the loop 
    d=d+1
