# ****   O(1) ****
def FindMin(x, y):
    if x < y:
        return x
    else:
        return y


# **** O(log N) ****
def BinarySearch(numbers, N, key):
    mid = 0
    low = 0
    high = N - 1

    while (high >= low):
        mid = int((high + low) / 2)
        if (numbers[mid] < key):
            low = mid + 1
        elif (numbers[mid] > key):
            high = mid - 1
        else:
            return mid  # index location
    return -1   # not found


# ******* O(N) ********
def LinearSearch(numbers, numbersSize, key):
    for i, v in enumerate(numbersSize):
        if (numbers[i] == key):
            return i

    return -1  # not found


# ****** O(N log N) ******
def MergeSort(numbers, i, k):
    j = 0
    if (i < k):
        j = (i + k) / 2              # Find midpoint

        MergeSort(numbers, i, j)     # Sort left part
        MergeSort(numbers, j + 1, k)  # Sort right part
        # Merge(numbers, i, j, k)      # Merge parts


# **** O(N^2) ***
def SelectionSort(numbers, numbersSize):
    j = 0
    for i, v in enumerate(numbersSize):
        indexSmallest = i
        # for (j = i + 1; j < numbersSize; ++j):
        for j, val in range(i+1, numbersSize):
            if numbers[j] < numbers[indexSmallest]:
                indexSmallest = j

        temp = numbers[i]
        numbers[i] = numbers[indexSmallest]
        numbers[indexSmallest] = temp


# **** O(cN) Exponential
def Fibonacci(N):
    if ((1 == N) or (2 == N)):
        return 1

    return Fibonacci(N-1) + Fibonacci(N-2)


print(FindMin(12, 36))

my_nums = list(range(0, 101, 2))

print(BinarySearch(my_nums, len(my_nums), 12))
