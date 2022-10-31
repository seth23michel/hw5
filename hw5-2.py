from a5 import insert, printStructure

def mergeSort(numList):
    if len(numList) > 1:
        mid = len(numList) // 2  # establish middle of the list
        leftList = numList[:mid]  # establish two new lists that are seperated from the middle to be sorted
        rightList = numList[mid:]

        mergeSort(leftList)  # applies mergesort to left lists
        mergeSort(rightList)  # applies mergesort to right lists
        i = j = k = 0
        while i < len(leftList) and j < len(rightList):
            if leftList[i] < rightList[j]:
                numList[k] = leftList[i]
                i = i + 1
            else:
                numList[k] = rightList[j]
                j = j + 1
            k = k + 1

        while i < len(leftList):  # while loops that iterate through their respective lists at each side
            numList[k] = leftList[i]
            i = i + 1
            k = k + 1

        while j < len(rightList):
            numList[k] = rightList[j]
            j = j + 1
            k = k + 1


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
