# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.
word = str(input("Enter the string: "))
times = int(input("Enter how many times you wanna repeat: "))
print(word*times)


#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
ageInNextYear = str(age +1)
print("Hello, "+name+"! You are "+str(age)+ " years old. Next year, you will be "+ageInNextYear+" years old.")

#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)
sentence = input("Enter the sentence: ")
wordNeedFinding = input("Enter character need to find: ")
print(wordNeedFinding in sentence)

#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
word = input("Enter the word: ")
startIndex = int(input("Enter the first index: "))
endIndex = int(input("Enter the end index: "))
print(word[startIndex:endIndex])

#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.
sentence = str(input("Enter the sentence: "))
sentence = sentence.split()
newSentence = "|".join(sentence)
print (newSentence)
