
'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to
it.
Write a Python script that reads a file gardening_tips.txt and prints
out each tip one by one.
'''
lineNumber = 1
with open("tipsForGarden.txt","r") as file:
    for line in file:
        print(lineNumber, line, end="")
        lineNumber+=1
'''
#2. Write a Python program that allows users to log their hiking trips. The program
should:
- Use a while loop to repeatedly ask for a hike name and distance in miles
- Save each entry to hiking_log.txt (each hike on a new line)
- When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''

with open("hiking_log.txt","w") as file:
    while True:
        hikeName = input("Enter the hiking name (or press 0 to exit): ")
        if hikeName == "0":
            break

        distance = float(input("Enter the distance: "))
        file.write(f"{hikeName}: {distance} miles\n")


with open("hiking_log.txt", "r") as file:
        print(file.read())



'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
it. Write a Python program that:
- Reads the file
- Requests 5 inputs from the user: 5 words the user would like to count the
frequency of
- Counts how many times each word appears
- Creates a dictionary of the words and their counts
- Print the dictionary to the console
'''

#open file
with open("song.txt", "r") as file:
            lyrics = file.read().lower()

#creative list for five word need to find
five_words_to_count = []
for i in range(5):
    word = input("Enter the word want to counting: ").lower() #not capital
    five_words_to_count.append(word)

#make dictionary
word_count = {}
for word in five_words_to_count: # loop for 5 ưord 
        times = lyrics.split().count(word)
        word_count[word] = times #put the key and the value to the dictionary

for key, value in word_count.items(): #print all in the dictionary
    print(f"{key}: {value}")



'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated
by commas.
Write a program that reads the poll.txt file
Count how many votes "yea" or "nay" received and print the results.
'''
with open("poll.txt","r") as file:
    content= file.read()

allTheVotes = content.split(",") #split the votes between the , 
#counting
yesVote = allTheVotes.count("yes")
noVote = allTheVotes.count("no")

print("Yes Vote: ",yesVote)
print("No Vote: ",noVote)
