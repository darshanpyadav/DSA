int a = 0, b = 0;
for (i = 0; i < N; i++) {
    a = a + rand();
}
for (j = 0; j < M; j++) {
    b = b + rand();
}

Time: O(N+M)
Space: O(1)

-----------------------------------------------------------------------------------------------------------------------
int a = 0, b = 0;
for (i = 0; i < N; i++) {
    for (j = 0; j < N; j++) {
        a = a + j;
    }
}
for (k = 0; k < N; k++) {
    b = b + k;
}

Time: O(N*N)
Space: O(1)  -> the values of ‘a’ and ‘b’ are updated, which does not increase the space requirements
-----------------------------------------------------------------------------------------------------------------------
int a = 0;
for (i = 0; i < N; i++) {
    for (j = N; j > i; j--) {
        a = a + i + j;
    }
}

Time: O(N(N+1)//2) ~ O(N*N)
Space: O(1)
-----------------------------------------------------------------------------------------------------------------------
What does it mean when we say that an algorithm X is asymptotically more efficient than Y?

-> X will always be a better choice for large inputs

A(x) = 100
B(x) = x

for smaller inputs B(x) < A(x)
-----------------------------------------------------------------------------------------------------------------------
int a = 0, i = N;
while (i > 1) {
    a += i;
    i /= 2;
}

Time: O(logN) -> base2

N = 2, x = 1 (log2 = 1)
N = 4, x = 2 (log4 = 2)
n = 8, x = 3 (log8 = 3)
-----------------------------------------------------------------------------------------------------------------------
int count = 0;
for (int i = N; i > 0; i /= 2) {
    for (int j = 0; j < i; j++) {
        count += 1;
    }
}

Time: O(n)
Inner loop runs N, N/2. N/4,...
So N+N/2+.... = N

N = 3, x = 4
N = 4, x = 7
N = 5, x = 9
N = 6, x = 10
O(2N-1) or O(2N-2) ~ O(N)
-----------------------------------------------------------------------------------------------------------------------
Which of the following is not bounded by O(n^2)?

(15^10) * n + 12099
n^1.98
Answer: n^3 / (sqrt(n))
(2^20) * n
-----------------------------------------------------------------------------------------------------------------------
int i, j, k = 0;
for (i  = n/2; i <= n; i++) {
    for (j = 2; j <= n; j = j * 2) {
        k = k + n/2;
    }
}

Time: O(N*logN)

Outer loop is (N-N/2), inner is logN
-----------------------------------------------------------------------------------------------------------------------
int gcd(int n, int m) {
    if (n%m ==0) return m;
    if (n < m) swap(n, m);
    while (m > 0) {
        n = n%m;
        swap(n, m);
    }
    return n;
}

Time: O(logN)
gcd is logn
-----------------------------------------------------------------------------------------------------------------------
f1(n) = 2^n

f2(n) = n^(3/2)

f3(n) = nLogn

f4(n) = n^(Logn)

Increasing order of time complexity:
f3,f2,f4,f1
-----------------------------------------------------------------------------------------------------------------------

int j = 0;
for(int i = 0; i < n; ++i) {
    while(j < n && arr[i] < arr[j]) {
        j++;
    }
}

Time: O(N)
worst time complexity
-----------------------------------------------------------------------------------------------------------------------
Binary search

Best -> O(1)
Average and Worst -> O(logN)
-----------------------------------------------------------------------------------------------------------------------