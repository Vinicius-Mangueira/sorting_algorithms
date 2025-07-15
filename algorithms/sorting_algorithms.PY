#Importing necessary libraries
import time
# Sorting Algorithms Implementation
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

#Function to read numbers from a file
def readingtest(tests):
    #Reads numbers from a specified file and returns them as a list.
    with open(tests, 'r') as file:
        numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
    return numbers

tests =["num.1000.1.in",
        "num.1000.2.in",
        "num.1000.3.in"
        "num.1000.4.in",
        "num.10000.1.in",
        "num.10000.2.in",
        "num.10000.3.in",
        "num.10000.4.in",
        "num.100000.1.in",
        "num.100000.2.in",
        "num.100000.3.in"
        "num.100000.4.in",]

def Tests_algorithms():

    #test with Insertion Sort
    start_time = time.time()
