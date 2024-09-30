'''
loop statements.
*break=to come out of the loop quickly.
*continue=continue if condition is satisfied.
*pass=let pass the block of code after satisfying the condition.
'''


#1. WAP to chek if a collection is homomgenous collection or not

print("Program for Homogenous/Heterogenous collection")
collection=eval(input("Enter a collection:  "))
homogenous_collection=True
ref_type=type(collection[0])
for item in collection:
    if type(item)!=ref_type:
        homogenous_collection=False
        break
if homogenous_collection==True:
        print(f" {collection} is an homogenous collection.")
else:
        print(f"{collection} is not homogenous_collection")

a=("\n this is the next program that you're seeing below")
b=a.upper()
print(b)

#2. WAP to check the external number is prime number/not.

num=int(input("enter the desired no: "))
if num==1:
      print(f"{num} is not a prime number")
elif num==2:
      print(f"{num} is an prime number!")
else:
      prime=True
      for i in range(2,num):
            if num%i==1:
                  prime=False
                  break
      if num==prime:
            print(f" The entered {num} is an prime number!")
      else:
            print(f"The entered {num} is not a prime number!")
a=("\n this is the next program that you're seeing below")
b=a.upper()
print(b)

#WAP to validate for username and password using while and for loop
actual_username="Ek Tha Tiger "
actual_password="Zoya143"
while True:
      user_name=input("enter the username: ")
      if user_name!=actual_username:
            break
      for _ in range(3):
            password=input("enter the password: ")
            if password==actual_password:
                  print(f"{actual_password} has been succesfully logged! ")
                  break
else:
      print(f"{actual_username} has been blocked for exceeding maximum limits!")