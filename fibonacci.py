import time
import functools

start_time = time.perf_counter()
@functools.cache
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(40))

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(elapsed_time)


start_time = time.perf_counter()
def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]
    if n==0:
        return 0
    elif n==1:
        return 1
    cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    return cache[n]
print(fibonacci(40))

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(elapsed_time)