
# Insertion Sort Algorithm
def IsertionSort(A,n):
    pivo =  None
    for i in range(1,n):
        pivo = A[i]
        j = i - 1
        while j >= 0 and A[j] > pivo:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = pivo
    return A
