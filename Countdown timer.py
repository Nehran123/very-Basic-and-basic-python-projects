import time

my_time=int(input("Enter the time in seconds="))

for x in range(0,my_time):
    print(x)#Print the current countdown value
    time.sleep(0.5)#Pause the execution for 0.5 second to create a delay between counts

print("YO, TIMES UP")

your_time=int(input("Enter the time in seconds"))

for a in range(0,your_time,1):
    print(a)
    time.sleep(1)

print("Hey, time's up")
