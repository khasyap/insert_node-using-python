#!/bin/python3

import math
import os
import random
import re
import sys

# Define Node for Linked List
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

# Define Linked List
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


# Complete the 'solve' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
# 1. INTEGER SINGLY LINKED LIST A
# 2. INTEGER SINGLY LINKED LIST B
def solve(A, B):
    MOD = 10007

    # Store counts of all elements in A
    countA = {}
    temp = A
    while temp:
        countA[temp.data] = countA.get(temp.data, 0) + 1
        temp = temp.next

    # Traverse B and compute product for common elements
    product = 1
    found = False
    temp = B
    while temp:
        if temp.data in countA:
            # Multiply the value of node from B raised to the count of its occurrences in A
            product = (product * (temp.data ** countA[temp.data])) % MOD
            found = True
        temp = temp.next

    # If no common element, return 0
    return product if found else 0


if __name__ == '__main__':
    A_count = int(input().strip())
    A = SinglyLinkedList()

    for _ in range(A_count):
        A_item = int(input().strip())
        A.insert_node(A_item)

    B_count = int(input().strip())
    B = SinglyLinkedList()

    for _ in range(B_count):
        B_item = int(input().strip())
        B.insert_node(B_item)

    result = solve(A.head, B.head)
    print(result)
