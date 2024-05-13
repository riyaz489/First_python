# in this problem we have given multiple activities in a list with their start and end time.
# and few of the tasks timing are overlapping with each other, and we have only one worker.
# So in case of overlapping we can only pick one task, not both.
# now out task is to maximize the number of taks picked.

# for exmaple: [(1,4),(2,5),(4,6)]
# in this case tasks picked is (1,4), (4,6)
# as if we pick (2,5) then we won't able be to pick other 2 tasks.

# idea is simple sort tasks in ascending order by ending time.
# then start traversing from left to right, if current item is overlapping with previous item then skip current item
# as you notice we are picking task with lower ending times. because if we pick task with lower ending time,
# then it will be high probability of getting next tasks which are not overlapping.
# i.e we are increasing probability of close current task first before next task starts.

def activity_selection(data:list):
    data = sorted(data, key=lambda x: x[1])
    res = [data[0]] # adding first data to res, as we are picking min ending time items
    for i in data[1:]:

        # if next item starting time is less than previous item ending time, then it means it is overlapping
        # no need to check other parameters for overlapping as we already sorted data on the basis of ending time.
        # that means next task is guaranteed to end after prev task.
        if i[0]< res[-1][1]:
            continue
        else:
            res.append(i)

    return res

print(activity_selection([(2,5),(1,4),(4,6)]))
