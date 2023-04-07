import time

def recursive_f(n):
    if n < 2:
        return 1
    else:
        return 2 * recursive_f(n-1) + recursive_f(n-3)

def iterative_f(n):
    if n < 2:
        return 1
    f0, f1, f2 = 1, 1, 3
    for i in range(3, n + 1):
        fn = 2 * f2 + f0
        f0, f1, f2 = f1, f2, fn
    return fn if n > 2 else f2

start = time.time()
n = 4
#print(recursive_f(n))
print(iterative_f(n))
end = time.time()

#print(end-start)

fn = 4

def calculate_f(n):
    fn = [1] * (n + 1)
    for i in range(2, n + 1):
        fn[i] = 2 * fn[i-1] + fn[i-3]
    return fn[n]

#print(calculate_f(6))

def iterative_f(n):
    fn = [1] * (n + 1)
    for i in range(2, n + 1):
        fn[i] = 2 * fn[i-1] + fn[i-3]
    return fn[n]

def iterative_f(n):
    fn = [1] * 4
    for i in range(2, n + 1):
        fn[3] = 2 * fn[2] + fn[0]
        fn[0], fn[1], fn[2] = fn[1], fn[2], fn[3]
    return fn[3]

print(iterative_f(5))