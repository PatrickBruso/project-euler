"""
Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
even-valued terms.
"""
memo = {}  # Store previously computed fibonacci values for quicker computing


def fibonacci(x):
    if x in memo:
        return memo[x]
    if x <= 2:
        f = 1
    else:
        f = fibonacci(x - 1) + fibonacci(x - 2)
    memo[x] = f
    return f


def main():
    fib_sum = 0
    i = 1
    while fibonacci(i) <= 4000000:
        if fibonacci(i) % 2 == 0:
            fib_sum += fibonacci(i)
        i += 1

    return fib_sum


if __name__ == '__main__':
    print(main())
