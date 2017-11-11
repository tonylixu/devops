def island_perimeter(grid):
    land_points = []
    row = 0
    #print "grid is " + str(len(grid))
    while row < len(grid):
        #print "grid row is " + str(len(grid[row]))
        col = 0
        while col < len(grid[row]):
            if grid[row][col] == 1:
                land_points.append((row, col))
            col += 1
        row += 1
    print dict(land_points)

if __name__ == '__main__':
    grid = [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]
    ]
    island_perimeter(grid)