# *****************************************************************************
# Author            : darshanp (darshanp@juniper.net)
# Date              : 29/09/19
# Last modified by  : darshanp
# Version           : 1.0
# Description       : Let-s-do-it
# *****************************************************************************
'''
We are given n requests numbered 0 to n – 1. Each request i has a time that it takes to complete t(i) and a deadline
d(i). If a request i starts at time s(i), then its finish time is f(i) = s(i) + t(i). The lateness of request i is
L(i) = f(i) – d(i) if f(i) > d(i). The maximum value of L(i) over all i is called the maximum lateness.
That is, maximum lateness = max(L(0), L(1), …, L(n – 1)). The problem is to schedule all the requests such that the
value of maximum lateness is minimized.
'''


def minimize_lateness(times, deadlines):
    """Return minimum max lateness and the schedule to obtain it.

    (min_lateness, schedule) is returned.

    Lateness of a request i is L(i) = finish time of i - deadline of if
    request i finishes after its deadline.
    The maximum lateness is the maximum value of L(i) over all i.
    min_lateness is the minimum value of the maximum lateness that can be
    achieved by optimally scheduling the requests.

    schedule is a list that contains the indexes of the requests ordered such
    that minimum maximum lateness is achieved.

    ttime[i] is the time taken to complete request i.
    dtime[i] is the deadline of request i.
    """
    max_deadline = 0
    start = 0
    # sort based on deadline
    sorted_times = sorted(zip(times, deadlines), key=lambda ele: ele[1])

    for time, deadline in sorted_times:
        max_deadline = max(max_deadline, start + time - deadline)
        start += time

    return sorted_times, max_deadline


if __name__ == "__main__":
    times = list(map(int, input("Enter times").split()))
    deadlines = list(map(int, input("Enter deadlines").split()))
    schedule, min_lateness = minimize_lateness(times, deadlines)
    print('The minimum maximum lateness:', min_lateness)
    print('The order in which the requests should be scheduled:', schedule)
