"""
Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def main():
    sum_of_multiples = 0
    for i in range(1000):
        # Check to see if i is multiple of 3 or 5 (or both) and if so add it to the running sum
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples += i

    return sum_of_multiples


if __name__ == '__main__':
    print(main())
