# For completed functions (definitions?) let's put a + in a comment after the name
from random import randint

numBlocksInMouth = 0
level = 1
arr = [[0 for x in range(0,20)] for x in range(0,20)]
arrSize = len(arr) * len(arr[0])

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

# Will randomly fill the board with blocks
# I can't get this to work?
def randBlocks(arr):
    import random
    for i in range(300):
        e = random.randint(0, 19) 
        c = random.randint(0, 19) 
        if arr[e][c] == 0:
            arr[e][c] == 1
    
def move(blockNum):
    #......        

def kill(monsterNum):
    #.........
def placeMonsters():
    #..........
    for i in range (len(list)*3/5):
        random = randint(0, )
        
    

