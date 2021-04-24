day=0
squats=0
total=0
avg=0


while day<=6:
    #All this below statement will be executed this the above condition will be true
    day=day+1
    squats=int(input("Squats on day {}: ".format(day)))
    total=total+squats

avg=total/day
print("In the last {} days, you did an average of {} squats!".format(day, avg))
