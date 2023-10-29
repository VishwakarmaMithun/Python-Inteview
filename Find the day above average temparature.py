numDays  =int(input("How many day's temperateure : "))
total = 0
userint=[]
for i in range(numDays):
    nextDay= int(input("Days:"+ str(i+1)+ "'s high temp :"))
    total += nextDay
    userint.append(nextDay)

avg =  round(total/numDays,2)
print("\n Average = " + str(avg))

above = 0
for i in userint :
    if i > avg :
        above +=1;
print(str(above) + "day(s) above average ")