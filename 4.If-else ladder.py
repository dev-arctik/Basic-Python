year=int(input("Enter the year:"))

if year%100==0: 
    if year%400==0:  #this is where the ladder is executed
        print("IT IS A LEAP YEAR")
    else:
        print("IT IS NOT A LEAP YEAR")
else:
    if year%4==0:
        print("IT IS A LEAP YEAR")
    else:
        print("IT IS NOT A LEAP YEAR")
