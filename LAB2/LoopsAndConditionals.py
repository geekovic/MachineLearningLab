# Conditional Statements
number = int(input("Enter a number: "))
if number > 0:
 print("The number is positive.")
elif number == 0:
 print("The number is zero.")
else:
 print("The number is negative.")
# While Loop: Print numbers from 1 to 5
print("\nWhile Loop: Numbers from 1 to 5")
i = 1
while i <= 5:
 print(i, end=' ')
 i += 1
# For Loop: Print elements in a list
print("\n\nFor Loop: Elements in list")
my_list = [10, 20, 30, 40, 50]
for item in my_list:
 print(item, end=' ')
