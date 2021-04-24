#randome dice number genrator
import random #importing bulid-in module random

a=random.randint(1,6)    #randint will select a number from 1 to 6
b=random.randrange(1,6)  #randrange will select a number from 1 to 6

print("The values are....{} and {}".format(a,b))
