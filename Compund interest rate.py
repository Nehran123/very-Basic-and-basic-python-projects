principle= 0
rate= 0
time= 0

while principle <= 0:
    principle= float(input("enter the priciple amount= "))

while rate <= 0:
    rate= float(input("enter the interest rate= "))/100


while time <= 0:
    rate= int(input("Enter the time in years= "))
    
n= 1
total= principle * (1+rate/n) ** (n * time)
print(f" Balance aafter time is {total:.2f}")
