import sys

def max_disjoint_segments(A, K, L) -> int:
    N = len(A)
    
    if K + L > N:
        return -1

    # prefix[n] would return sum of elements A[0]..A[n - 1]1
    prefix = []
    
    prefix.append(0)
    prefix.append(A[0])
    for i in range(1, N):
        prefix.append(prefix[i] + A[i])
    
    start_i = 0
    start_j = start_i + K

    sum_i = 0
    sum_j = 0

    max_sum_i = sum_i
    max_sum_j = sum_j

    max_i = start_i
    max_j = start_j

    while is_segment_in_range(start_i, K, N) or is_segment_in_range(start_j, L, N):

        if is_segment_in_range(start_i, K, N):
            sum_i = prefix[start_i + K] - prefix[start_i]
        if is_segment_in_range(start_j, L, N):
            sum_j = prefix[start_j + L] - prefix[start_j]
                    
        if is_disjoint(start_i, K, start_j, L):
            if is_disjoint(max_j, L, start_i, K) and sum_i > max_sum_i:
                max_sum_i = sum_i
                max_i = start_i
            if is_disjoint(max_i, K, start_j, L) and sum_j > max_sum_j:
                max_sum_j = sum_j
                max_j = start_j

                # check if we want to update max_sum_i again now that max_sum_j and max_j is changed
                if is_disjoint(max_j, L, start_i, K) and sum_i > max_sum_i:
                    max_sum_i = sum_i
                    max_i = start_i
                
        start_i = start_i + 1
        start_j = start_j + 1

    return max_sum_i + max_sum_j

def is_segment_in_range(start, length, N):
    # we check for equality here as well since prefix[] is of length N + 1
    return start + length <= N
                        
def is_disjoint(start_i, K, start_j, L):
    return start_i + K <= start_j or start_j + L <= start_i

A = input("enter A\n").split(' ')
A = [int(item) for item in A]
K = int(input("enter K\n"))
L = int(input("enter L\n"))
print(max_disjoint_segments(A, K, L))
