# here we can  move top/down or left/right not diagonally.
# 1 means path and 0 means wall. so we can only travel on 1's.
# bottom-right corner of matrix is destination
res_path = []
traversed_path = set()
def find_path_for_maze(data, row_index=0, col_index=0):
    # idea is simple we will recursively travel in all feasible paths.

    if row_index == len(data)-1 and col_index == len(data[0])-1:
        res_path.append((row_index, col_index))
        return True

    if row_index >=len(data) or col_index>=len(data):
        return False

    if data[row_index][col_index] == 0 or (row_index, col_index) not in traversed_path:
        # this back tracking part, as we did early return if path is already traversed or
        # current node is not 1.
        return False
    traversed_path.add((row_index, col_index))
    res_path.append((row_index, col_index))
    if find_path_for_maze(data, row_index+1, col_index) or find_path_for_maze(data, row_index, col_index+1):
        return True
    # removing path from list if designation not found from this coords.
    else:
        res_path.remove((row_index, col_index))
        return False

data = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,1],

]
print(find_path_for_maze(data))
print(res_path)
