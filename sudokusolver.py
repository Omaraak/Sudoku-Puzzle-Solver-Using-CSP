file = open('sudoku.txt', 'r')
read_for_file = file.readlines()

#Making the Puzzle Grid
def Make_grid(puzzle_As_string):
    global grid
    print('\nChoosen problem')
    for i in range(0, len(puzzle_As_string), 9): # loop through String in 9's and stop at the length of "puzzle_As_string".
        row = puzzle_As_string[i:i+9]
        temp = []
        for cell in row:
            temp.append(int(cell))
        grid.append(temp)    
    printGrid()


#check if a digit can be placed in the given block
def possible(row,col,digit):
    global grid
    for i in range(0,9): #check all cells in the row
        if grid[row][i] == digit:
            return False
    for i in range(0,9): #check all cells in the column
        if grid[i][col] == digit:
            return False
    square_row = (row//3)*3 #Floor div -- see where is the cell square row starting point
    square_col = (col//3)*3 #Floor div -- see where is the cell square column starting point
    for i in range(0,3):
        for j in range(0,3):
            if grid[square_row+i][square_col+j] == digit: #Is the number already used in the square?
                return False    
    return True

def solveCSP():
    global grid
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0: #if 0 then it is empty space
                for digit in range(1,10): #check all digits as a solution
                    if possible(row,col,digit):
                        grid[row][col] = digit
                        solveCSP()
                        grid[row][col] = 0  #Backtrack step
                return
    print('\nThe Solution')
    printGrid()


#Print 
def printGrid():
    global grid
    for row in grid:
        print(row)


num = int(input ("Enter The Board Number(from 1-5): "))
num-=1
list = []
for line in read_for_file:
    if line[-1] == "\n":
        list.append(str(line[:-1]))

#print(list[num])
puzzle_As_string = str(list[num])
grid = []
Make_grid(puzzle_As_string)
solveCSP()