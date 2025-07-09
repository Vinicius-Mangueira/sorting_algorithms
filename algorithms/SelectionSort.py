# Selection Sort Algorithm Implementation
def selectionSort(A,n):
    for i in range(0, n - 1):
        i_min = i
        for j in range(i + 1, n):
            if A[j] < A[i_min]:
                i_min = j
        if(A[i] != A[i_min]):
            temp = A[i]
            A[i] = A[i_min]
            A[i_min] = temp
    return A
