#1. while loop to print python word for 5 times.
a=('\n this is just for printing lines at multiple times.\n')
b=a.title()
print(b)
count=0
while count<5:
    print(" Hey! Iam Python....")
    count+=1

a=("\n this is the next  program you're seeing downwards")
b=a.upper()
print(b)

#2 while loop to print n natural numbers
start=1
end=int(input("Please enter your desire ending number to be printed in natural number format:  "))
print('\n')
while start<=end:
    print(start)
    start+=1
a=("\n this is the next  program you're seeing downwards")
b=a.upper()
print(b)

#3 while loop for countdowning the numbers.
start=int(input("enter your desire number to start countdowning:  _"))
print('\n')
end=0
while end<=start:
    print(start)
    start-=1
a=('''\n Thank you. You've succesfully executed today's programs!''')
b=a.upper()
print(b)