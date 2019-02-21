print("Fibonacci Sayı Dizisi")

a, b = 1, 1
fibonacci = [a,b]
for i in range(10):
    a, b = b, a + b
    fibonacci.append(b)
print(fibonacci)