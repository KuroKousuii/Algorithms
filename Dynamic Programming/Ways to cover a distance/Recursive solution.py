# A naive recursive Python3 program
# to count number of ways to cover
# a distance with 1, 2 and 3 steps

# Returns count of ways to
# cover 'dist'
def printCountRec(dist):
    # Base cases
    if dist < 0:
        return 0

    if dist == 0:
        return 1

    # Recur for all previous 3 and
    # add the results
    return (printCountRec(dist - 1) +
            printCountRec(dist - 2) +
            printCountRec(dist - 3))


# Driver code
dist = 4
print(printCountRec(dist))