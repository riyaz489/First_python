# rotate image
# rotate nxn matrix clockwise 90 without new matrix

# sol: replace first element with element of last col first row, then last col last row element with
# first row last col element, then last row first col with last row and last col element, then first row first col with last row and first col.
# so in above case we are doing 4 replacements , so we need 4 temp variables, bot to optimize this
# store first elem in temp and then replace  then first row first col with last row and first col first. then we can proceed with other replacements.

# apply same steps for next elements similarly. once outer layer is transformed then repeat same steps for inner layer.
# by changing matrix size to n-1*n-1 (basically divide in sub-problem).


# for n row elements we do n-1*4 transformation

def rotate_arr(x, first,end):
    if first>=end:
        return
    else:
        # this loop will automatically run n-1 times
        for i in range(first,end):
            # now we will write our 4 transformations
            # lets assume first index is row and second index is col
            temp = x[first][i]
            # for top side cloclwise rotation we move towards right so introduced i to update col value
            x[first][i] = x[end-i][first]

            # for left side cloclwise rotation we move towards top so introduced i to update row value
            x[end-i][first] = x[end][end-i]

            # for bottom side we move towards left so introduced i to update col
            x[end][end-i] = x[first+i][end]

            #  for right side cloclwise rotation we move towards bottom so introduced i to update col value
            x[first+i][end] = temp
        rotate_arr(x,first+1, end-1)

x=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate_arr(x, 0, len(x)-1)
for y in x:
    print(y)