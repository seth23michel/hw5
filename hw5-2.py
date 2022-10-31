# Seth Michel U05202326
# Dillon Mathew U76212871

from a5 import insert, printStructure

def mergeSort(numList): #this function will be called after printing out the unsorted list first
    if len(numList) > 1:
        midIndex = len(numList) // 2  # establish middle of the list (if list even then is picks left most index)
        leftList = numList[:midIndex]  # establish two new lists that are seperated from the middle to be sorted
        rightList = numList[midIndex:]

        mergeSort(leftList)  # applies mergesort to left lists
        mergeSort(rightList)  # applies mergesort to right lists
        i = 0
        j = 0
        k = 0
        while i < len(leftList) and j < len(rightList):
            if leftList[i] < rightList[j]:
                numList[k] = leftList[i]
                i += 1
            else:
                numList[k] = rightList[j]
                j += 1
            k += 1

        while i < len(leftList):  # while loops that iterate through the left of the middle we established
            numList[k] = leftList[i]
            i += 1
            k += 1

        while j < len(rightList):   # while loops that iterates through the right side of the middle we established
            numList[k] = rightList[j]
            j += 1
            k += 1


def main():
    head = None

    with open('hw5-2.txt', 'r') as hw5_file:
        numList = list(map(int, hw5_file.read().split(' ')))
    print(numList)  # prints unsorted list
    mergeSort(numList)  # sorts the list via MergeSort
    print(numList)  # prints the newly sorted list

    for element in numList:
        head = insert(element, head)

    print('Linked List (Merge Sorted): ', end='')
    printStructure(head)


if __name__ == '__main__':
    main()
