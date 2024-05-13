# In this problem we have given few jobs with their deadline and their value/profit.
# few of the jobs might overlap with other jobs timing, and we have only one worker.
# and each job takes 1 hour to finish.
# now our task is to pick jobs in such a way that it will maximise our profit.

# job deadline = 4,1,1,1
# job profit = 70,80,30,100   ; respectively
# now we will pick 100 profit job and 70 profit job
# so total profit is 170; we can't pick 80 and 30 profit job as we picked 100 initially and 100 job 1st hour
# and we missed deadlines for 80 and 30 jobs.

# now to solve this we will sort jobs with their  profit.
# and assign the latest available time for execution.
# by latest we mean, time which is more closer to the deadline/
# for example for 70 profit job we will look for 4th hour slot, if its free we will assign that slot to 70 profit job.
# else if 4th is already booked then we will look for 3rd hour slot, if that is also booked then look for 2nd hour
# and so on.
# we doing so, so that we unintentionally book the earlier slow which can be used by some other job.
# so just to avoid that and maximise profit.
def job_scheduling(data):
    data = sorted(data, key=lambda x: x[1], reverse=True)
    # here index represent job times and value will be profit
    # its lenght will be equal to max job deadlin we have
    job_timings = [None] * max(data, key=lambda x: x[0])[0]
    for i in data:

        # try to fit current job in job_timings array of possible
        for j in range(i[0]-1, -1, -1): # doing -1 for starting index as hours starts from 1 and index starts from 0
            # running loop in reverse order. from deadline-1 to 0
            if job_timings[j] is None:
                job_timings[j] = i[1]
                break
            # else if no slot available then current job will not assigned.

    result = 0
    for i in job_timings:
        if i is not None:
            result+=i
    return result

print(job_scheduling([(4,70),(1,80),(1,30),(1,100),]))