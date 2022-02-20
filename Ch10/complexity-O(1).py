#****   O(1) ****
def FindMin(x, y):
    if x < y:
        return x
    else:
        return y


#**** O(log N) ****
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
            return mid

    return -1   #not found


print(FindMin(12, 36))

my_nums = list(range(0, 101,2))

print(BinarySearch(my_nums,len(my_nums), 12))
