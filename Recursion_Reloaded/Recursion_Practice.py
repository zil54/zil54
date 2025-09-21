from functools import lru_cache


#- functools module provides tools for functional programming.
#- lru_cache is a built-in decorator that caches function results to avoid redundant calculations.

@lru_cache(maxsize=None)
# @lru_cache(maxsize=None) enables caching for fibonacci_memoized.
# maxsize=None means unlimited cache size—storing all previously computed Fibonacci values.

def fibonacci_memoized(n):
    #Base Cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)
#Recursive Calculation
# Breaks the problem into smaller subproblems:
# F(n) = F(n-1) + F(n-2)
# Instead of recomputing values, cached results speed up repeated calls.



print(fibonacci_memoized(50))  # Output: 12586269025