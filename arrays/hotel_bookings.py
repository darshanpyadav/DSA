'''
A hotel manager has to process N advance bookings of rooms for the next season. His hotel has K rooms. Bookings contain an arrival date and a departure date.
He wants to find out whether there are enough rooms in the hotel to satisfy the demand. Write a program that solves this problem in time O(N log N) .

Input:


First list for arrival time of booking.
Second list for departure time of booking.
Third is K which denotes count of rooms.

Output:

A boolean which tells whether its possible to make a booking.
Return 0/1 for C programs.
O -> No there are not enough rooms for N booking.
1 -> Yes there are enough rooms for N booking.
Example :

Input :
        Arrivals :   [1 3 5]
        Departures : [2 6 8]
        K : 1

Return : False / 0

At day = 5, there are 2 guests in the hotel. But I have only one room.
'''


def hotel(arrive, depart, K):
    combined_dates = []

    for i in range(len(arrive)):
        combined_dates.append((arrive[i], 1))
        combined_dates.append((depart[i], 0))

    sorted_combined_dates = sorted(combined_dates)

    max_rooms, rooms = 0, 0
    for i in sorted_combined_dates:
        if i[1] == 1:
            rooms += 1
            max_rooms = max(max_rooms, rooms)
        else:
            rooms -= 1

    return 1 if max_rooms <= K else 0


# print(hotel([1, 3, 5], [2, 6, 8], 2))
print(hotel([ 9, 47, 17, 39, 35, 35, 20, 18, 15, 34, 11, 2, 45, 46, 15, 33, 47, 47, 10, 11, 27 ], [ 32, 82, 39, 86, 81, 58, 64, 53, 40, 76, 40, 46, 63, 88, 56, 52, 50, 72, 22, 19, 38 ], 16))
# print(hotel([1,3,5,7,9],[2,6,8,10,11], 2))
# print(hotel([ 1, 2, 3, 4 ], [ 10, 2, 6, 14 ], 2))
