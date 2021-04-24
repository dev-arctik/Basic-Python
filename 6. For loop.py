#factorial of number

a=int(input('Enter a number: '))
fact=1

for x in range(1,a+1): #range will start fromm 1 to a
    fact=fact*x   #x will have value of range from one it will increase or every loop

print('Factorial of {} is {}'.format(a,fact)) #format will give value to {} 
