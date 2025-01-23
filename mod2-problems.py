# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")

# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
number1st = float(input("Enter the frist number: "))
number2nd = float(input("Enter the second number: "))
print("+:  ", number1st + number2nd)
print("-:  ", number1st - number2nd)
print("*:  ", number1st * number2nd)
print("/:  ", number1st / number2nd)

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

s = float( (a+b+c)/2 )
result = math.sqrt( s*(s-a)*(s-b)*(s-c) ) 

print("S = ",result)

# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).
import math

def CIS141(numbers):
    #total
    total = sum(numbers)
    
    # average
    average = total / len(numbers)
    
    # max & min
    minimum = min(numbers)
    maximum = max(numbers)
    
    # range
    rangeOfValue = maximum - minimum
    
    # standard deviation
    variance = sum((x - average) ** 2 for x in numbers) / len(numbers)
    ''' tính từng giá trị trong mảng numbers / cal each value in numbers array'''

    standard_deviation = math.sqrt(variance)
    
    # result
    print(f"total: {total}")
    print(f"average: {average}")
    print(f"minuimum: {minimum}")
    print(f"maximum: {maximum}")
    print(f"range: {rangeOfValue}")
    print(f"standard deviation: {standard_deviation}")

# example
numbers = [4,8,6,5,3]
CIS141(numbers)
