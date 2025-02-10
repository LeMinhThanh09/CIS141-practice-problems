#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.
n = int(input("Enter number: "))
sum = 0
i = 0

while i <= n :
    sum = sum + i
    i+=1
print("Total from 1 to n = ", sum)


#2. Define a string variable (e.g., my_string = "Olympic College"). Use a for loop to print each character on its own line. Convert each character to uppercase before printing.
name = str(input("Enter the string: "))
count = len(name)
i = 0
for i in range(count):
    print("\n", name[i].upper())
    i+=1

#3. Use a for loop and the range() function to print all even numbers from 2 to 20.

for num in range(2, 21, 2):
    print(num)
# or use if else
for i in range(1,21):
    if i%2 == 0:
        print (i)


  
#4. Use nested for loops to create a simple multiplication table for numbers 1 through 5. Format your output so that each row corresponds to multiplying by a specific number. Example output:


for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")

    print(" ")

  

#5. Write a program that continuously asks the user to input a number. If the user enters 0, immediately stop asking for more numbers. Otherwise, print the number they entered. Sample interaction:


while True: 
    number = int(input("Enter the number (0 to stop): "))
    if number == 0:
        print("Exit...")
        break

    print("You entered: ", number)
    
