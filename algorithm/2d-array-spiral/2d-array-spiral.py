A = [
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9, 10, 11, 12),
    (13, 14, 15, 16)
]

start_row_index = 0
end_row_index = len(A)
start_col_index = 0
end_col_index = len(A[0])

while (start_row_index < end_row_index) and (start_col_index < end_col_index):
    # Print the first row for the matrix
    for i in range(start_col_index, end_col_index):
        print A[start_row_index][i]
        i += 1
    # Shrink the maxtix by by row
    start_row_index += 1
    
    # Print the last column of the matrix
    for i in range(start_row_index, end_row_index):
        print A[i][end_col_index-1]
        i += 1
    end_row_index -= 1

'''
(rows, cols) = (len(A), len(A[0]))
print "Matrix rows is " + str(rows)
print "Matrix columns is " + str(cols)
(r, c) = (0, -1) # Start here
nextturn = stepsx = cols # Move so many steps
print "nextturn is " + str(nextturn) + ", stepsx is " + str(stepsx) + ", cols is " + str(cols)
stepsy = rows - 1
print "stepsy is " + str(stepsy)
(inc_col, inc_row) = (1, 0) # At each step move this much
turns = 0 # How many times our snake had turned
for i in range(rows * cols):
    print "=" * 10
    print "step " + str(i)
    c += inc_col
    r += inc_row
    print "coordinates: " + str(r) + ", " + str(c)
    
    print A[r][c]
    
    if i == nextturn - 1:
        turns += 1
        print "tunrs is " + str(turns)
        # At each turn reduce how many steps we go next
        if turns % 2 == 0:
            nextturn += stepsx
            stepsy -= 1
            print "nextturn is " + str(nextturn)
            print "stepsy is " + str(stepsy)
        else:
            nextturn += stepsy
            stepsx -= 1
            print "nextturn is " + str(nextturn)
            print "stepsy is " + str(stepsy)
        # Change direction
        print "direction before: " + str(inc_row) + ", " + str(inc_col)
        (inc_col, inc_row) = (-inc_row, inc_col)
        print "direction: " + str(inc_row) + ", " + str(inc_col)
'''     
