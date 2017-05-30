# For completed functions (definitions?) let's put a + in a comment after the name
from random import randint
blockCount = 0
level = 1
arr = [[0 for x in range(0,20)] for x in range(0,20)]
arrSize = len(arr) * len(arr[0])
arr[20][0] = 1 
currentPos = [20, 0]
score = 0
#Aesha I got the printboard to work
def printBoard(arr): #+
    print("______________________________________________________________")
    for i in range(20):
        print("|", end='')
        for j in range(20):
            if arr[i][j] == 0: # 0 == ".", an empty space
                print(" . ", end='')
            elif arr[i][i] == 1: # 1 == "@", the character
                print(" @ ", end='')
            elif arr[i][j] == 2: # 2 == "#", the block
                print(" # ", end='')
            elif arr[i][j] == 3: # 3 == ":", the monster
                print(" : ", end='')
        print("|")
    print("——————————————————————————————————————————————————————————————")
    print("Block count: " + blockCount)

# Will randomly fill the board with blocks
# I can't get this to work?
def placeBlocks(arr):
    import random
    for i in range(300):
        e = random.randint(0, 19) 
        c = random.randint(0, 19) 
        if arr[e][c] == 0:
            arr[e][c] = 2
 def placeMOnsters(arr):
    import random
    for i in range(100):
        e = random.randint(0, 19) 
        c = random.randint(0, 19) 
        if arr[e][c] == 0:
            arr[e][c] = 3           
    
def move(row, col):
    arr[currentPos[0], currentPos[1]] = 0
    arr[row][col] = 1
    if arr[row][col] ==  
    
def kill(monsterX, monsterY): # takes row and column of monster to be killed
    if blockCount >= 4:
        arr[monsterX][monsterY] = 0
    
if __name__ == '__main__': #main method stuff
   main()

def main() 
    gameOn = true
    while(gameOn) :
        placeMonsters()
        printBoard()
        print "What row do you want to move to?"
        row = raw_input()
        print "What column do you want to move to?"
        col = raw_input()
        initial = arr[row][col]
        move(row, col)
        if initial == 2:
            blockCount = blockCount + 1
        if blockCount >= 4:
            print "Which monster would you like to kill- row?"
            row = raw_input()
            print "Which monster would you like to kill- column?"
            col = raw_input()
            if arr[row][col] == 3:
                blockCount = 0
                arr[row][col] = 1
                score = score + 50
                
         
        
    

# Hey guys I went home bc I'm sick, but here's what I got done this morning.  It eats blocks up to 4 at a time, but will crash if you try to eat blocks on the edges.
# Movements are through wasd, with e to eat blocks.  I was working on adding monsters, I'll continue on that if I can later

# List contains the numbers 0-3                                                 
# 0 == ".", an empty space
# 1 == "#", the block
# 2 == "@", the character
# 3 == ":", the monster
 
import random
 
print("Welcome to Square Python Meal!")
 
numBlocksInMouth = 0
playerPos = [0, 0]
monsterPos = [0, 0]
 
arr = [[0 for x in range(0,20)] for x in range(0,20)]   
arrSize = len(arr) * len(arr[0])

def printBoard(arr):
    print("___________________________________________")
    for i in range(20):
        print("|", end='')
        for j in range(20):
            if arr[i][j] == 0: 
                print(" .", end='')
            elif arr[i][j] == 1:
                print(" #", end='')
            elif arr[i][j] == 2:
                print(" @", end='')
            elif arr[i][j] == 3:
                print(" &", end='')
        print(" |")
    print("———————————————————————————————————————————")
    
def randBlocks(arr):
    for i in range(242):
        e = random.randint(0, 19)
        c = random.randint(0, 19)
        if arr[e][c] == 0:
            arr[e][c] = 1
    
def placePlayer():
    e = random.randint(0, 19)
    c = random.randint(0, 19)
    while arr[e][c] != 0:
        e = random.randint(0, 19)
        c = random.randint(0, 19)
    arr[e][c] = 2
    playerPos[0] = e
    playerPos[1] = c

def placeMonster():
    e = random.randint(0, 19) 
    c = random.randint(0, 19) 
    while arr[e][c] != 0:
        e = random.randint(0, 19) 
        c = random.randint(0, 19) 
    arr[e][c] = 3 
    monsterPos[0] = e 
    monsterPos[1] = c 
    
def moveUp():
    if arr[playerPos[0] - 1][playerPos[1]] == 0:
        arr[playerPos[0] - 1][playerPos[1]] = 2
        arr[playerPos[0]][playerPos[1]] = 0
        playerPos[0] -= 1
    
def moveDown():
    if arr[playerPos[0] + 1][playerPos[1]] == 0:
        arr[playerPos[0] + 1][playerPos[1]] = 2
        arr[playerPos[0]][playerPos[1]] = 0
        playerPos[0] += 1 
        
def moveLeft():
    if arr[playerPos[0]][playerPos[1] - 1] == 0:
        arr[playerPos[0]][playerPos[1] - 1] = 2 
        arr[playerPos[0]][playerPos[1]] = 0 
        playerPos[1] -= 1
    
def moveRight():
    if arr[playerPos[0]][playerPos[1] + 1] == 0:
        arr[playerPos[0]][playerPos[1] + 1] = 2
        arr[playerPos[0]][playerPos[1]] = 0
        playerPos[1] += 1

def pickUpBlocks():
    global numBlocksInMouth
    if arr[playerPos[0]+1][playerPos[1]] == 1:
        arr[playerPos[0]+1][playerPos[1]] = 0
        numBlocksInMouth += 1
    if arr[playerPos[0]][playerPos[1]+1] == 1:
        arr[playerPos[0]][playerPos[1]+1] = 0
        numBlocksInMouth += 1
    if arr[playerPos[0]-1][playerPos[1]] == 1:
        arr[playerPos[0]-1][playerPos[1]] = 0
        numBlocksInMouth += 1
    if arr[playerPos[0]][playerPos[1]-1] == 1:
        arr[playerPos[0]][playerPos[1]-1] = 0
        numBlocksInMouth += 1
        
randBlocks(arr)
placePlayer()
placeMonster()
printBoard(arr)
print(playerPos)
print(monsterPos)
print("Blocks in mouth: " + str(numBlocksInMouth))
move = 'f'
while move != 'q':
    move = input("Move [w, a, s, d, or q (quit)]? ")
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
    printBoard(arr)
    print(playerPos)
    print("Blocks in mouth: " + str(numBlocksInMouth))

#TODO
# First off: the player picks up anything from the 4 spaces up,down,right,left of it when you press e, so it can collect up to 4 blocks at once
# 1. When the player picks up blocks while on the edge or moves into the edge there is an error bc of arrays and whatnot, pls add a crapload of if statements so that when playerPos is on the edges the behavior is modified (ex: player on top corner trying to go up cannot do so, and trying to pick up blocks there can only get blocks from down, left)
# 2. Pls make a release where they spit out blocks, but pay attention to the edges of the board so if they're on the side they can only spit out 3 (again, probs lotsa if statements) Spit out blocks will just go as far down up,right,left,down as it can before hitting another block (this part'll be tricky)
# 3. Monster doesn't move yet.  Have it look for a direction to move in (up down right left) and begin doing so, moving one block at a time when the player moves.  When it hits a block it either looks for a new direction or moves back the way it came (random choice)
# 4. When monster is in the same row as player releasing blocks, it dies (maybe change its symbol to an x for a couple turns before disappearing)
# 5. (Optional) If anyone feels like figuring out how to do a gui we could make it look cooler :D
# Thanks and I'll be back in an hour!
