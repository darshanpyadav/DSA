# *****************************************************************************
# Author            : darshanp (darshanp@juniper.net)
# Date              : 29/09/19
# Last modified by  : darshanp
# Version           : 1.0
# Description       : Let-s-do-it
# *****************************************************************************


def interval_scheduling(start_times, end_times):
    """Return largest set of mutually compatible activities.

    This will return a maximum-set subset of activities (numbered from 0 to n -
    1) that are mutually compatible. Two activities are mutually compatible if
    the start time of one activity is not less then the finish time of the other.

    stimes[i] is the start time of activity i.
    ftimes[i] is the finish time of activity i.
    """
    result = set()
    sort_finish_time = sorted(zip(start_times, end_times), key=lambda ele: ele[1])
    
    prev_finish_time = 0
    for start, end in sort_finish_time:
        if start >= prev_finish_time:
            result.add(start)
            prev_finish_time = end

    return result


if __name__ == "__main__":
    start = list(map(int, input("Enter start times").split()))
    end = list(map(int, input("Enter end times").split()))
    max_value = interval_scheduling(start, end)
    print(max_value)

# O(N*logN)