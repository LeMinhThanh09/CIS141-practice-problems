
from random import randint 
print("Choose ONE choice:ROCK, PAPER, SCISSORS")
player = input()
computer = randint(0,2)

if computer == 0: 
	computer = "SCISSORS"

if computer == 1:
	computer = "ROCK"

if computer == 2:
	computer = "PAPER"

print("------------")

print("YOUR CHOICE :"+ player)
print("------------")
print("COMPUTER CHOICE :"+ computer)

print("------------")

print("FINAL RESULT :")



# PEACE
if player == "SCISSORS":
	if computer == "SCISSORS":
		print("PEACE")

if player == "ROCK":
	if computer == "ROCK":
		print("PEACE")

if player == "PAPER":
	if computer == "PAPER":
		print("PEACE")

# SCISSORS
if player == "SCISSORS":
	if computer == "ROCK":
		print("---Player LOSE----COMPUTER WIN---")


if player == "SCISSORS":
	if computer == "PAPER":
		print("---Player win----computer LOSE---")


# rock
if player == "ROCK":
	if computer == "PAPER":
		print("---Player LOSE----computer win---")


if player == "ROCK":
	if computer == "SCISSORS":
		print("---Player win----computer LOSE---")


# paper
if player == "PAPER":
	if computer == "ROCK":
		print("---Player win----computer LOSE---")

if player == "PAPER":
	if computer == "SCISSORS":
		print("---Player LOSE----computer win---")
