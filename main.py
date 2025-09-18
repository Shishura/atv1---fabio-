import random
import string

print("\n=== 1. CALCULADORA ===")
a = 10
b = 5

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b if b != 0 else "Erro: divisão por zero"

print(f"Soma: {a} + {b} = {soma}")
print(f"Subtração: {a} - {b} = {subtracao}")
print(f"Multiplicação: {a} * {b} = {multiplicacao}")
print(f"Divisão: {a} / {b} = {divisao}")

print("\n=== 2. CONVERSOR DE TEMPERATURA ===")
celsius = 0
fahrenheit = (celsius * 9/5) + 32
celsius2 = (fahrenheit - 32) * 5/9
print(f"{celsius}°C = {fahrenheit}°F")
print(f"{fahrenheit}°F = {celsius2}°C")