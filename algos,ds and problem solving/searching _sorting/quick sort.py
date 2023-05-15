# worst n2
# best/average nlogn
# sapce complxity - O(n)
# here we will chose a pivot (random,first or last)
# then move all smaller elements than pivot value to left and greater will be on the right side
# so here we basically do  things find correct position of pivot and
# move all other greater element to right and smaller elemts to left and return new pivot position

# quick and heap are unstable algos
def pivot(f,l,ar):
    pi = ar[l]
    i = f-1
    for j in range(f,l):
        # moving all greater element to right side of ith index
        if ar[j]< pi:
            i += 1
            ar[j], ar[i] = ar[i], ar[j]

    # swapping i th and last element
    ar[l], ar[i+1] = ar[i+1 ], ar[l]
    return i+1

def sorting(f,l,ar):
    if f<l:
        pi = pivot(f,l,ar)
        sorting(f, pi-1, ar)
        sorting(pi+1, l, ar)




x = [1, 2, 5, 1, -4, 9, 3]
sorting(0, len(x)-1,x)
print(x)