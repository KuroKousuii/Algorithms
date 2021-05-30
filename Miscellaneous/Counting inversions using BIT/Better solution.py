# Python3 program to count inversions using Binary Indexed Tree
from bisect import bisect_left as lower_bound


# Returns sum of arr[0..index]. This function assumes
# that the array is preprocessed and partial sums of
# array elements are stored in BITree.
def getSum(BITree, index):
    sum = 0  # Initialize result

    # Traverse ancestors of BITree[index]
    while (index > 0):
        # Add current element of BITree to sum
        sum += BITree[index]

        # Move index to parent node in getSum View
        index -= index & (-index)

    return sum


# Updates a node in Binary Index Tree (BITree) at given index
# in BITree. The given value 'val' is added to BITree[i] and
# all of its ancestors in tree.
def updateBIT(BITree, n, index, val):
    # Traverse all ancestors and add 'val'
    while (index <= n):
        # Add 'val' to current node of BI Tree
        BITree[index] += val

    # Update index to that of parent in update View
    index += index & (-index)


# Converts an array to an array with values from 1 to n
# and relative order of smaller and greater elements remains
# same. For example, 7, -90, 100, 1 is converted to
# 3, 1, 4 ,2
def convert(arr, n):
    # Create a copy of arrp in temp and sort the temp array
    # in increasing order
    temp = [0] * (n)
    for i in range(n):
        temp[i] = arr[i]
    temp = sorted(temp)

    # Traverse all array elements
    for i in range(n):
        # lower_bound() Returns pointer to the first element
        # greater than or equal to arr[i]
        arr[i] = lower_bound(temp, arr[i]) + 1


# Returns inversion count arr[0..n-1]
def getInvCount(arr, n):
    invcount = 0  # Initialize result

    # Convert arr to an array with values from 1 to n and
    # relative order of smaller and greater elements remains
    # same. For example, 7, -90, 100, 1 is converted to
    # 3, 1, 4 ,2
    convert(arr, n)

    # Create a BIT with size equal to maxElement+1 (Extra
    # one is used so that elements can be directly be
    # used as index)
    BIT = [0] * (n + 1)

    # Traverse all elements from right.
    for i in range(n - 1, -1, -1):
        # Get count of elements smaller than arr[i]
        invcount += getSum(BIT, arr[i] - 1)

        # Add current element to BIT
        updateBIT(BIT, n, arr[i], 1)

    return invcount


# Driver program
if __name__ == '__main__':
    arr = [8, 4, 2, 1]
    n = len(arr)
    print("Number of inversions are : ", getInvCount(arr, n))