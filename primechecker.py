import time
start_time = time.perf_counter()
def is_prime(n):
    if n in [2,3]:
        return True
    if n<2 or n%2==0:
        return False
    r=3
    while r*r <= n:
        if n%r==0:
            return False
        r+=2
        return True
a = is_prime(9973)
print(a)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(elapsed_time)


start_time = time.perf_counter()
def is_prime(n):
    if n<2:
        return False
    if n in (2, 3):
        return True
    if n%2==0 or n%3==0:
        return False
    i = 5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
        return True
a = is_prime(9973)
print(a)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(elapsed_time)


start_time = time.perf_counter()
def is_prime(n):
    if n<2:
        return False
    if n in (2, 3):
        return True
    if n%2==0 or n%3==0:
        return False
    return not any(
        n%i==0 or n%(i+2)==0
        for i in range(5, int(n**0.5)+1, 6)
    )
a = is_prime(9973)
print(a)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(elapsed_time)


start_time = time.perf_counter()
def is_prime(num):
    for i in range(2, num):
        if num%i == 0:
            print("Not Prime")
    else:
        print("Prime")
a = is_prime(9973)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(elapsed_time)