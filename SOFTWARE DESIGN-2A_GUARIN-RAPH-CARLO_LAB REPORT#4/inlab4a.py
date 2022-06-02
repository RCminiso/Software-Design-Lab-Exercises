# Recursive python 3 program to
# find minimum

# function to print Minimum element
# using recursion
def findMinRec(A, n):
    # if size = 0 means whole array
    # has been traversed
    if (n == 1):
        return A[0]
    return min(A[n - 1], findMinRec(A, n - 1))


# Driver Code
if __name__ == '__main__':
    A = [1, 6, 5, 7, -70, 60, 45]
    n = len(A)
    print(findMinRec(A, n))