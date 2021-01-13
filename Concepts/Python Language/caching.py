from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n: int) -> int:
    # print(n)
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(n) for n in range(100000)])
# print([fib(5000)])