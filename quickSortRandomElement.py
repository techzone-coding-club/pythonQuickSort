'''
This file demonstrates the Quick Sort Algorithm in Python
Using a Random Element as the pivot for the algorithm
'''

from random import randrange

def partition(listA, low, high):
    i = (low-1)
    pivot = listA[high]


    for j in range(low, high):
        if listA[j] <= pivot:
            i += 1
            listA[i], listA[j] = listA[j], listA[i]

    listA[i+1], listA[high] = listA[high], listA[i+1]
    return i+1


def partitionR(listA, low, high):
    randomVal = randrange(low, high)
    print("Random Value: {0:}\t\tLow Value: {1:}\tHigh Value{2:}".format(randomVal, low, high))
    if randomVal > low:
        listA[low], listA[randomVal] = listA[randomVal], listA[low]
    return partition(listA, low, high)


def quickSortR(listA, low, high):
    if low < high:
        pi = partitionR(listA, low, high)

        quickSortR(listA, low, pi - 1)
        quickSortR(listA, pi + 1, high)


if __name__ == '__main__':
    list1 = []
    # fill the container with a random set of no more than 1000 random numbers ranging from 0 to 10000
    for x in range(randrange(1000)):
        list1.append(randrange(10000))
    low = 0
    high = len(list1) - 1

    print("Using QuickSort with a Random Element as the pivot\n==================================================")
    print("Before: {:}\n".format(list1))
    print("Size of container: {:}\n".format(len(list1)))
    quickSortR(list1, low, high)
    print("\nAfter: {:}".format(list1))
    print("Size of container: {:}".format(len(list1)))
