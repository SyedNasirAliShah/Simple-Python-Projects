number = int(input("Enter a number:"))
newNumber = 0

temp = number
while number > 0:
    remainder = number % 10
    newNumber = (newNumber * 10) + remainder
    number = number // 10
if newNumber == temp:
    print("Palindrome")
else:
    print("Not palindrome")