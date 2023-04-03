import time
import matplotlib.pyplot as plt

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

recursive_times = []
iterative_times = []
n_values = list(range(1, 51))

for n in n_values:
    start = time.time()
    recursive_f(n)
    end = time.time()
    recursive_times.append(end - start)

    start = time.time()
    iterative_f(n)
    end = time.time()
    iterative_times.append(end - start)

table_data = []
for i, n in enumerate(n_values):
    table_data.append([n, recursive_times[i], iterative_times[i]])

print('{:<7}|{:<22}|{:<22}'.format('n', 'Recursive time (s)', 'Iterative time (s)'))
print('-' * 55)
for data in table_data:
    print('{:<7}|{:<22}|{:<22}'.format(data[0], data[1], data[2]))

plt.plot(n_values, recursive_times, label='Recursive')
plt.plot(n_values, iterative_times, label='Iterative')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Comparing Recursive and Iterative Approaches')
plt.legend()
plt.show()
