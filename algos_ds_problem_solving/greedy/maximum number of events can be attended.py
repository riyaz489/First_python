from heapq import heappush, heappop
from typing import List

# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
class Solution:

    def maxEvents(self, events: List[List[int]]) -> int:
        # idea is simple, first we sort on the basis of start date.
        # then we will traverse from day1 to last day
        # and for each day, we will keep track of events which we can visit.(now it becomes activity selection problem)
        # now out of those possible events for current day we will greedily pick events with the lowest end time.
        # because it will increase portability to join more events in next upcoming days

        slots_booked = 0
        # sorted on the basis of start day.
        events.sort(key=lambda x: x[0])
        ec = 0

        pq = []
        current_day = events[0][0]
        # if both the lists are empty then it means we utilized all events
        while pq or ec < len(events):

            # add events which can be utilized in current day to queue
            while ec < len(events) and events[ec][0] <= current_day:
                heappush(pq, events[ec][1])
                ec += 1
            if len(pq) == 0:
                current_day = events[ec][0]
                continue
            t = heappop(pq)
            # remove events which are expired now
            while t < current_day:
                if len(pq) == 0:
                    t = None
                    break
                t = heappop(pq)
            if t:
                slots_booked += 1
            current_day += 1
        return slots_booked
