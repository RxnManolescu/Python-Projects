import random

#function to create a grid with "n" number of rows and columns and "m" number of mines
def minesweeper(n, m):

    #create "n" sized grid populated with 0's
    matrix = [[0 for col in range(n)] for row in range(n)]

    #randomly place "m" mines in the matrix(grid)
    for mine in range(m):
        r = random.randint(0, n-1)
        c = random.randint(0, n-1)
        #mark mines with "#"
        matrix[r][c] = "#"

    #loop to iterate through all rows and cols of the grid
    for row in range(0, n):
        for col in range(0, n):
            #condition to skip if cell is a mine
            if matrix[row][col] == "#":
                continue
            #block of conditions to check all adjacent neighbours of a cell
            #and increase the count by 1 if mines found
            if (row > 0 and col > 0) and (matrix[row-1][col-1]) == "#": #top left
                matrix[row][col] += 1
            if (row > 0) and matrix[row-1][col] == "#": #top centre
                matrix[row][col] += 1
            if (row > 0 and col < n-1) and matrix[row-1][col+1] == "#": #top right
                matrix[row][col] += 1
            if (col < n-1) and matrix[row][col+1] == "#": #centre right
                matrix[row][col] += 1
            if (row < n-1 and col < n-1) and matrix[row+1][col+1] == "#": #bottom right
                matrix[row][col] += 1
            if (row < n-1) and matrix[row+1][col] == "#": #bottom centre
                matrix[row][col] += 1
            if (row < n-1 and col > 0) and matrix[row+1][col-1] == "#": #bottom left
                matrix[row][col] += 1
            if (col > 0) and matrix[row][col-1] == "#": #centre left
                matrix[row][col] += 1
            
    #display grid in a user-friendly manner
    for rows in matrix:
        print("\t".join(str(cols) for cols in rows))
        print("")

minesweeper(5, 8)