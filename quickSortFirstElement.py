'''
This file demonstrates the Quick Sort Algorithm in Python
Using the First Element as the pivot for the algorithm
'''

def partition(listA, low, high):
    i = low
    pivot = listA[low]

    for j in range(low+1, high+1):
        if listA[j] <= pivot:
            listA[i], listA[j] = listA[j], listA[i]
            i += 1

    listA[i+1], listA[high] = listA[high], listA[i+1]
    return i


def quickSortF(listA, low, high):
    if low < high:
        pi = partition(listA, low, high)

        quickSortF(listA, low, pi-1)
        quickSortF(listA, pi+1, high)


if __name__ == '__main__':
    list1 = [45, 3, 24, 10, 14, 95, 100, 73]
    low = 0
    high = len(list1) - 1

    print("Using QuickSort with the First Element as the pivot\n==================================================")
    print("Before:\t{:}\n".format(list1))
    quickSortF(list1, low, high)
    print("After:\t{:}\n".format(list1))
