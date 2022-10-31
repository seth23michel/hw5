"""
File: a5.py
Assignment 5

Define a length function.
Define a printStructure function.
Define an insert function.
Test the above functions and the Node class.
"""
from node import Node


def length(head):
    """Returns the number of items in the linked structure
    referred to by head."""
    probe = head
    count = 0
    while probe:
        count += 1
        probe = probe.next
    return count


def insert(newItem, head):
    if head is None:
        head = Node(newItem)
        # if structure is empty
        # ADD CODE HERE
    elif head.next is None:
        head.next = Node(newItem)
    else:
        insert(newItem, head.next)
    return head


def printStructure(head):
    """Prints the items in the structure referred to by head."""
    if head is None:
        return

    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()
    # ADD CODE HERE


def orderLinkedList(head):
    tempList = []
    temp = head
    while temp:
        tempList.append(temp.data)
        temp = temp.next
    tempList.sort()

    for element in tempList:
        head.data = element
        head = head.next
    return head


def main():
    """Gets words from the user and inserts in the
    structure referred to by head."""

    head = None
    while True:
        userInput = input('Please enter a word (or just hit enter to end): ')
        if userInput == '':
            break
        head = insert(userInput, head)
    orderLinkedList(head)  # method sorts linked list

    print('The structure contains', length(head), 'items: ', end="")
    printStructure(head)


if __name__ == "__main__": main()
