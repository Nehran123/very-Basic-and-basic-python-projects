n=10 # Number of Fibonacci numbers to generate

a=0 # First Fibonacci number
b=1 # Second Fibonacci numbe

print(f"{a} {b}",end=" ") # Print the first two numbers, end="" ensures that the next print statement continues on the same line.



for i in range(n-2): # Loop to generate the remaining numbers
     c=a+b # Loop to generate the remaining numbers
     print(c,end="") # Loop to generate the remaining numbers

     a=b # Update 'a' to the previous 'b'
     b=c # Update 'b' to the newly calculated 'c'
