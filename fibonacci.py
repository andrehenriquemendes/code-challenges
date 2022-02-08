# recursive / traditional
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)


# memoize
def fib_memo(n, memo):
    if memo[n] is not None:
        return memo[n]
    else:
        result = fib_memo(n-2, memo) + fib_memo(n-1, memo)
        memo[n] = result
        return result


# bottom up
def fib_bottom_up(n):
    memo = [None] * (n+1)
    memo[1] = 1
    memo[2] = 1
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[n]

n = 200
# memo = [None] * (n+1)
# memo[1] = 1
# memo[2] = 1

# print(fib_memo(n, memo))
# print(fib_bottom_up(n))
print(fib(n))