# 2x3
x= [[1,2,3],
    [4,5,6]]
# 3x2
y = [[1,2],
     [3,4],
     [5,6]]

# result would be 2x2, and we can product it because number of cols in x match number of rows in y

# result = [[1x1+2x3+3x5, 1x2+2x4+3*6],
#            ...]
res = [[0,0],
       [0,0,]]
# row in x
for i in range(len(x)):

    # below 2 loops is to traverse y matrix column wise , so first all elements in column frst then send column and so on.
    # column in y
    for j in range(len(y[0])):
        # row in y
        for k in range(len(y)):
            #  first row of x is multiplied and summed with each column of y
            # then second row again with first col of y, then second row of x with second col of y
            res[i][j] += x[i][k]*y[k][j]


print(res)
