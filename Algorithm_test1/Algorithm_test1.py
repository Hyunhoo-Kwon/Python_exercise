import random

players = ["Eric", "Jack"]

def isInvalidRange(n):
	if n<1 or n>4294967295:
		return True
	else:
		return False

def startGame(n):
	p = 1
	winner = ""
	cnt = -1

	while isNotFinishing(p, n):
		p = p*generateRandomNumber(2, 10)
		cnt = cnt+1

	winner = getWinner(cnt)
	printResult(winner)

def isNotFinishing(p, n):
	if p<n:
		return True
	else:
		return False

def generateRandomNumber(a, b):
	randomNumber = random.randint(a, b)
	return randomNumber

def getWinner(cnt):
	numberOfPlayers = len(players)
	index = cnt%numberOfPlayers

	if cnt == -1:
		return players[0]
	else:
		return players[index]

def printResult(name):
	print(name + " wins.\n")


while True:
	n = 0

	try:
		n = int(input("input number: "))
		if isInvalidRange(n):
			raise ValueError
	except ValueError:
		print("ValueError\n")
	else:
		startGame(n)
