import random

N = int(input("Enter the number of random points to generate: "))

n = 0
count = 0

while count < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
        n += 1
    else:
        pass

    count += 1

pi_approx = 4 * n / N
print(f"Approximate value of pi using {N} points: {pi_approx}")