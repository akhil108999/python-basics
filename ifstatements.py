
age=int(input("How old are you: "))

if age == 100:
    print("Your are a century old!!")
elif age >=18:
    print("Your are an adult")

elif age < 0:
    print("You haven't born yet")
else:
    print("Your are an child!")


Check if a number is positive or negative

num=int(input("Give a number: "))

if num>=0:
   print("Number is positive")
else:
    print("Number is negative")

Find largest of two numbers

num1=int(input("Enter first number: "))
num2=int(input("Enter second number "))

if num1>num2:
   print("Great First number is largest",num1," than second number",num2)
elif num2>num1:
    print("Great second number is largest",num2, " than first number",num1)

else:
   print("Bruuhhh two numbers are equal")
 

#Check leap year

leap = int(input("Enter a leap year: "))

if (leap%4==0 and leap%100!=0) or (leap%400==0):
    print("It is a leap year: ",leap)
else:
    print("It is not a leap year")

