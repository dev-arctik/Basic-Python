#check for prime number

num=int(input('Enter a number:'))
for x in range(2,num):
    if num%x==0:
        print('{} is not a prime number.'.format(num))
        break
else: # this else keyword is for 'for loop' i.e. if for loop fails this else will be executed
    print('{} is a prime number.'.format(num))
