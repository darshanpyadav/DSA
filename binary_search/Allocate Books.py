'''
Given an array of integers A of size N and an integer B.

College library has N bags,the ith book has A[i] number of pages.

You have to allocate books to B number of students so that maximum number of pages alloted to a student is minimum.

A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
Calculate and return that minimum possible number.

NOTE: Return -1 if a valid assignment is not possible.



Input Format

The first argument given is the integer array A.
The second argument given is the integer B.
Output Format

Return that minimum possible number
Constraints

1 <= N <= 10^5
1 <= A[i] <= 10^5
'''


def books(books_list, students):
    def all_gets_books(total_pages):
        left_pages, count,  = total_pages, 1
        remaining_students = students - count
        for pages in books_list:
            if pages > total_pages:
                return False
            left_pages -= pages
            if left_pages < 0 or remaining_students < 0:
                count += 1
                left_pages = total_pages - pages
        return count <= students

    start, end = 0, sum(books_list)

    if len(books_list) < students:
        return -1

    while start <= end:
        mid = (start+end)//2
        if all_gets_books(mid):
            end = mid - 1
        else:
            start = mid + 1
    return start


A = [ 73, 58, 30, 72, 44, 78, 23, 9 ]
B = 5
print(books(A,B))
