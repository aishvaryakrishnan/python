# Given a list of positive nums return max sum of two disjoint
# segments of the array of lengths K and L.
# If there exists no such two segments, return -1

import sys

def max_disjoint_segments(A, K, L) -> int:
    N = len(A)
    
    if K + L > N:
        return -1

    # prefix[n] would return sum of elements A[0]..A[n - 1]1
    prefix = [0] * (N + 1)

    for i in range(0, N):
        prefix[i + 1] = prefix[i] + A[i]

    max_sum = 0

    for i in range(0, N - K + 1):
        sum_i = prefix[i + K] - prefix[i]
        sum_j = 0
        for j in range(i + K, N - L + 1):
            sum_j = prefix[j + L] - prefix[j]
            
            if is_disjoint(i, K, j, L) and sum_i + sum_j > max_sum:
                max_sum = sum_i + sum_j

    return max_sum
                        
def is_disjoint(start_i, K, start_j, L):
    return start_i + K <= start_j or start_j + L <= start_i

A = input("enter A\n").split(' ')
A = [int(item) for item in A]
K = int(input("enter K\n"))
L = int(input("enter L\n"))
print(max_disjoint_segments(A, K, L))
