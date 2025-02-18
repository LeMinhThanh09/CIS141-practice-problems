#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.

listOfNumber = [1,2,3,4,5,6,7,8]
i = 0 
sum = 0

while i < len(listOfNumber):
    if listOfNumber[i] % 2 == 0:
        sum += listOfNumber[i]
    i+=1

print(sum)


#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list, and then print the count.
listOfWord = ["dfsdfsd","Olympic","Olympic","fsdfsdfsdf"]
i = 0 
count = 0 
while i < len(listOfWord):
    if listOfWord[i] == "Olympic":
        count += 1 
    i+=1
print(count)

#3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters. Print the resulting filtered list.
listOfWord = ["dfd","Olympic","Olympic","fsdfsdfsdf"]
i = 0 
newList = []
while i < len(listOfWord):
    if len(listOfWord[i]) > 3:
        newList.append(listOfWord[i])
    i+=1
print(newList)

#4. For a list of integers, write code that counts how many numbers are positive and how many are negative, then print both counts.
listOfNumber = [-1,3,-4,-1,3,4,5,6,4]
i = 0 
negative = 0
positive = 0

while i < len(listOfNumber):
    if listOfNumber[i] > 0:
        positive += 1
    elif listOfNumber[i] < 0:
        negative += 1
    i+=1
print(positive)
print(negative)


#5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element in the original list. Print the new list.

listOfNumber = [-1,3,-4,-1,3,4,5,6,4]
i = 0 
newList = []

while i < len(listOfNumber):
    newList.append(listOfNumber[i] * listOfNumber[i])
    i+=1
print(newList)
