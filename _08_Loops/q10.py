"""Print Prime Factors:
Description: Write a program that prints all the prime factors of a given number.
Example:
Input: 24
Output: 2, 3"""

number = int(input("Enter a number: "))
factors=[]
divisor = 2

while number > 1:
    if number % divisor == 0:
        #print(divisor)
        factors.append(divisor)
        #print(factors)
        number //= divisor
        #print(number)
    else:
        divisor += 1

print("Prime factors:",factors)
print(*factors, sep=', ')