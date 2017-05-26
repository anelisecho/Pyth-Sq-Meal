# For completed functions (definitions?) let's put a + in a comment after the name
from random import randint
blockCount = 0
level = 1
arr = [[0 for x in range(0,20)] for x in range(0,20)]
arrSize = len(arr) * len(arr[0])
arr[20][0] = 1 
currentPos = [20, 0]
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
            blockCount++
         
        
    

