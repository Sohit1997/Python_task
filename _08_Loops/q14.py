"""Calculate Square Root:
Description: Write a program to calculate the square root of a given number using the Newton-Raphson method.
Example:
Input: 16
Output: 4.0"""

# input_number = float(input("Enter a number: "))
#
# if input_number < 0:
#     print("Invalid input: Cannot calculate square root of a negative number.")
# else:
#     num = input_number / 2  # Initial guess
#     epsilon = 0.0001  # Desired level of accuracy
#
#     while abs(num * num - input_number) > epsilon:
#         num = (num + input_number / num) / 2
#
#     print(num)

str2 = input("Enter a string: ")
count = {}
for i in str2:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)










