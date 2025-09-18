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



print("\n=== 3. GERADOR DE SENHAS ===")
tamanho_senha = 12
caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(random.choice(caracteres) for _ in range(tamanho_senha))
print("Senha gerada:", senha)