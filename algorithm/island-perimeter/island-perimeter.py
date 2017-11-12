def island_perimeter(grid):
    # The total number of rows and cols
    rows = len(grid)
    cols = len(grid[0])
    # Define the perimeter
    p = 0
    for i in range(rows):
        for j in range(cols):
            # This is a land
            if grid[i][j] == 1:
                p += 4
                if grid[i-1][j] == 1 and i > 0:
                    p -= 2
                if grid[i][j-1] == 1 and j > 0:
                    p -= 2
    print p
        

if __name__ == '__main__':
    grid = [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]
    ]
    island_perimeter(grid)