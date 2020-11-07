'''
This file demonstrates the Quick Sort Algorithm in Python
Using the Middle Element as the pivot for the algorithm
'''

def partition(listA, low, high):
    i = low
    pivot = listA[len(listA)//2]

    for j in range(low, high):
        if listA[j] <= pivot:
            i += 1
            listA[i], listA[j] = listA[j], listA[i]

    listA[i+1], listA[high] = listA[high], listA[i+1]
    return i+1


def quickSortM(listA, low, high):
    if low < high:
        pi = partition(listA, low, high)

        quickSortM(listA, low, pi - 1)
        quickSortM(listA, pi + 1, high)


if __name__ == '__main__':
    list1 = [45, 3, 24, 10, 14, 95, 100, 73]
    low = 0
    high = len(list1) - 1

    print("Using QuickSort with the Middle Element as the pivot\n==================================================")
    print("Before: {:}\n".format(list1))
    quickSortM(list1, low, high)
    print("After: {:}\n".format(list1))
