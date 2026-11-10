import time
import matplotlib.pyplot as plt

# 1. Fibonacci sin programación dinámica 
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 2. Fibonacci con programación dinámica 
def fibonacci_dp(n):
    if n <= 1:
        return n
    F = [0] * (n + 1)
    F[1] = 1

    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]

valores_n = list(range(1, 31))
tiempos_recursivo = []
tiempos_dp = []

for n in valores_n:
    inicio = time.perf_counter()
    fibonacci(n)
    tiempos_recursivo.append(time.perf_counter() - inicio)

    inicio = time.perf_counter()
    fibonacci_dp(n)
    tiempos_dp.append(time.perf_counter() - inicio)

plt.figure(figsize=(8, 5))
plt.plot(valores_n, tiempos_recursivo, label='Sin PD ', color='red', marker='o')
plt.plot(valores_n, tiempos_dp, label='Con PD ', color='green', marker='s')

plt.title('Comparación de Tiempo de Ejecución: Fibonacci')
plt.xlabel('Valor de n')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.grid(True)
plt.legend()

plt.show()