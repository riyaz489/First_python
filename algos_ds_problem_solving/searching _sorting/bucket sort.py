# when data is evenly distributed then this algo can be used. like all concecutive elements have difference of 2.
# best case when all buckets has only one element. O(n) and this is only possible when array is evenly distributed.
# worst case one bucket has data and others are empty. O(nlog(n))

# in this algo we simply create n empty buckets and data which lies in specific range into a specific bucket.
# then using insertion sort we sort data inside bucket. as insertion sort is fast for less data.
# then we merge all buckets data.

def bucket_sort(data, k):

    # step 1 create empty k buckets.
    buckets = []
    for i in range(k):
        buckets.append(list())
    max_item = max(data)
    output = []
    # step 2 push data into appropriate buckets. O(n)
    for i in data:
        # i*k//max_item will put data into apropriate bucket.
        # for greater values it choose buckets closer to k and for lower values it will choose bucket
        # closed to 0th index.
        # for example if k is 4 and max_item is 80
        # if current item is 80 only then  80*4//80 = 4th bucket
        # if current item is 40 then 40*4//80 = 2nd bucket
        # so as you can see below formula is perfectly dividing our items into k ranges.
        # as indicies start from 0, so we did max_item +1 so that for max item it will go k-1 index.
        buckets[((i*k)//(max_item+1))].append(i)

    # step 3 sort individual buckets
    for i in buckets:  # O(k)
        i.sort()        # O(nlog(n)) in worst case and O(1) in bst case if bucket length is 1.

    # step 4 merge the buckets
    for i in buckets:
        output.extend(i)

    print(output)



bucket_sort([6,2,4,8,10,16,14,12], 3)