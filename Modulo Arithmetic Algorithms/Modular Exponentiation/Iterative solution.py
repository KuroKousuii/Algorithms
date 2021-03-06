# Iterative Function to calculate (x^y) in O(log y)
def power(x, y):
    # Initialize result
    res = 1

    while (y > 0):

        # If y is odd, multiply x with result
        if ((y & 1) != 0):
            res = res * x

        # y must be even now
        y = y >> 1  # y = y/2
        x = x * x  # Change x to x^2

    return res