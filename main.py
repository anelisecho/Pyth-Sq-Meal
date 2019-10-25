# List contains the numbers 0-3
# 0 == ".", an empty space
# 1 == "#", the block
# 2 == "@", the character
# 3 == ":", the monster

from random import randint

# Variables
numBlocksInMouth = 0
playerPos = [0, 0]
monsterPos = [0, 0]
score = 0
count = 0

arr = [[0 for x in range(0,20)] for x in range(0,20)]   
arrSize = len(arr) * len(arr[0])

def printBoard():
	print('\x1b[36;32m' + "___________________________________________" + '\x1b[0m')
	for i in range(20):
		print('\x1b[36;32m' + "|" + '\x1b[0m', end='')
		for j in range(20):
			if arr[i][j] == 0:
				print(" .", end='')
			elif arr[i][j] == 1:
				print('\x1b[36;32m' + ' #' + '\x1b[0m', end='')
			elif arr[i][j] == 2:
				print('\x1b[36;29m' + ' @' + '\x1b[0m', end='')
			elif arr[i][j] == 3:
				print('\x1b[36;31m' + ' &' + '\x1b[0m', end='')
			elif arr[i][j] == 4:
				print('\x1b[36;31m' + ' %' + '\x1b[0m', end='')
		print('\x1b[36;32m' + " |" + '\x1b[0m')
	print('\x1b[36;32m' + "———————————————————————————————————————————" + '\x1b[0m')
 
def randBlocks():
	for i in range(242):
		e = randint(0, 19)
		c = randint(0, 19)
		if arr[e][c] == 0:
			arr[e][c] = 1
 
def placePlayer():
	e = randint(0, 19)
	c = randint(0, 19)
	while arr[e][c] != 0:
		e = randint(0, 19)
		c = randint(0, 19)
	arr[e][c] = 2
	playerPos[0] = e
	playerPos[1] = c
 
def placeMonster():
	e = randint(0, 19)
	c = randint(0, 19)
	while arr[e][c] != 0:
		e = randint(0, 19)
		c = randint(0, 19)
	arr[e][c] = 3
	monsterPos[0] = e
	monsterPos[1] = c
 
def moveUp():
	if playerPos[0] != 0:
		if arr[playerPos[0] - 1][playerPos[1]] == 0:
			arr[playerPos[0] - 1][playerPos[1]] = 2
			arr[playerPos[0]][playerPos[1]] = 0
			playerPos[0] -= 1
 
def moveDown():
	if playerPos[0] != 19:
		if arr[playerPos[0] + 1][playerPos[1]] == 0:
			arr[playerPos[0] + 1][playerPos[1]] = 2
			arr[playerPos[0]][playerPos[1]] = 0
			playerPos[0] += 1
 
def moveLeft():
	if playerPos[1] != 0:
		if arr[playerPos[0]][playerPos[1] - 1] == 0:
			arr[playerPos[0]][playerPos[1] - 1] = 2
			arr[playerPos[0]][playerPos[1]] = 0
			playerPos[1] -= 1
 
def moveRight():
	if playerPos[1] != 19:
		if arr[playerPos[0]][playerPos[1] + 1] == 0:
			arr[playerPos[0]][playerPos[1] + 1] = 2
			arr[playerPos[0]][playerPos[1]] = 0
			playerPos[1] += 1
 
def pickUpBlocks():
	global numBlocksInMouth
	if playerPos[0] != 19:
		if arr[playerPos[0]+1][playerPos[1]] == 1: #down
			arr[playerPos[0]+1][playerPos[1]] = 0
			numBlocksInMouth += 1
	if playerPos[1] != 19:
		if arr[playerPos[0]][playerPos[1]+1] == 1: #right
			arr[playerPos[0]][playerPos[1]+1] = 0
			numBlocksInMouth += 1
	if playerPos[0] != 0:
		if arr[playerPos[0]-1][playerPos[1]] == 1: #up
			arr[playerPos[0]-1][playerPos[1]] = 0
			numBlocksInMouth += 1
	if playerPos[1] != 0:
		if arr[playerPos[0]][playerPos[1]-1] == 1: #left
			arr[playerPos[0]][playerPos[1]-1] = 0
			numBlocksInMouth += 1

def upSpit():
	global numBlocksInMouth
	if playerPos[0] != 0:
		i = playerPos[0]
		while arr[i][playerPos[1]] != 1:
			if arr[i][playerPos[1]] == 3:
				monsterDed()
			i-= 1
			if i < 0:
				break
		arr[i+1][playerPos[1]] = 1
		numBlocksInMouth -= 1
 
def downSpit():
	global numBlocksInMouth
	if playerPos[0] != 19:
		i = playerPos[0]
		while arr[i][playerPos[1]] != 1:
			if arr[i][playerPos[1]] == 3:
				monsterDed()
			i+= 1
			if i > 19:
				break
		arr[i-1][playerPos[1]] = 1
		numBlocksInMouth -= 1
 
def rightSpit():
	global numBlocksInMouth
	if playerPos[1] != 19:
		i = playerPos[1]
		while arr[playerPos[0]][i] != 1:
			if arr[playerPos[0]][i] == 3:
   				monsterDed()
			i+= 1
			if i > 19:
				break
		arr[playerPos[0]][i-1] = 1
		numBlocksInMouth -= 1

def leftSpit():
	global numBlocksInMouth
	if playerPos[1] != 0:
		i = playerPos[1]
		while arr[playerPos[0]][i] != 1:
			if arr[playerPos[0]][i] == 3:
				monsterDed()
			i-= 1
			if i < 0:
				break
		arr[playerPos[0]][i+1] = 1
		numBlocksInMouth -= 1
 
def spitBlocks():
	if numBlocksInMouth < 4:
		if numBlocksInMouth == 3:
			upSpit()
			downSpit()
			leftSpit()
		elif numBlocksInMouth == 2:
			rightSpit()
			downSpit()
		elif numBlocksInMouth == 1:
			upSpit()
	else:
		upSpit()
		downSpit()
		rightSpit()
		leftSpit()

def monsterDed():
	global score
	arr[monsterPos[0]][monsterPos[1]] = 4
	score += 50


def help():
	print("'w' moves you up")
	print("’a’ moves you left")
	print("’s’ moves you down")
	print("’d’ moves you right")
	print("’e’ eats up to 4 blocks around you")
	print("’r’ releases blocks in all 4 directions - if you have less than 4 blocks they'll move in random directions")
	print("’q’ quits the game :(")
	print("And lastly, 'i' opens up these instructions!")
	print("Good luck! :D")
 
# Main method-y thing starts below
 
print("Welcome to Square Python Meal!")
print("Each turn, you have 9 options!")
help()
 
randBlocks()
placePlayer()
placeMonster()
print("Move [w, a, s, d, e, r, i, or q]?")
printBoard()
print("Your position: (" +str(playerPos[1] + 1) + ", " +str(playerPos[0] + 1)     + ")")
print("Blocks in mouth: " + str(numBlocksInMouth))
print("Score: " +str(score))

move = 'f'
while move != 'q':
	move = input()
	if move == 'w':
		moveUp()
	if move == 'a':
		moveLeft()
	if move == 's':
		moveDown()
	if move == 'd':
		moveRight()
	if move == 'e':
		pickUpBlocks()
	if move == 'r':
		spitBlocks()
	if move == 'i':
		help()
	print("Move [w, a, s, d, e, r, i, or q]?")
	printBoard()
	print("Your position: (" +str(playerPos[1] + 1) + ", " +str(playerPos[0] + 1) + ")")
	print("Blocks in mouth: " + str(numBlocksInMouth))
	print("Score: " +str(score))
	if count%5 == 0 :
		arr[monsterPos[0]][monsterPos[1]] = 0
		placeMonster()
	count += 1
