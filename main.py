# main file to demonstrate all four implementations
# Local Imports
from quickSortRandomElement import quickSortR
from quickSortMiddleElement import quickSortM
from quickSortLastElement import quickSortL
from quickSortFirstElement import quickSortF

# Package Imports
from random import randrange
import copy


# Generate list of integer values
low = 0
high = 1000
original_list = [randrange(x, 10000) for x in range(high)]

# Demonstrate use of Quick Sort First Element
print("=======================================================")
print("\t\tQuick Sort using First Element as Pivot")
qsF_list = copy.deepcopy(original_list)
print("qsR_list before: ", qsF_list)
quickSortF(qsF_list, low, high-1)
print("qsR_list after: ", qsF_list)
print("=======================================================\n\n")

# Demonstrate use of Quick Sort Last Element
print("=======================================================")
print("\t\tQuick Sort using Last Element as Pivot")
qsL_list = copy.deepcopy(original_list)
print("qsL_list before: ", qsF_list)
quickSortL(qsL_list, low, high-1)
print("qsL_list after: ", qsF_list)
print("=======================================================\n\n")

# Demonstrate use of Quick Sort Middle Element
print("=======================================================")
print("\t\tQuick Sort using Middle Element as Pivot")
qsM_list = copy.deepcopy(original_list)
print("qsM_list before: ", qsF_list)
quickSortM(qsM_list, low, high-1)
print("qsM_list after: ", qsF_list)
print("=======================================================\n\n")

# Demonstrate use of Quick Sort Random Element
print("=======================================================")
print("\t\tQuick Sort using a Random Element as Pivot")
qsR_list = copy.deepcopy(original_list)
print("qsR_list before: ", qsF_list)
quickSortR(qsR_list, low, high-1)
print("qsR_list after: ", qsF_list)
print("=======================================================\n\n")