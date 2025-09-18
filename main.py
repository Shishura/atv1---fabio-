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


cpf = "123.456.789-09"
cpf_limpo = ''.join(filter(str.isdigit, cpf))
cpf_valido = len(cpf_limpo) == 11 and not cpf_limpo == cpf_limpo[0] * 11
print("CPF informado:", cpf)
print("CPF limpo:", cpf_limpo)
print("É válido?", "Sim" if cpf_valido else "Não")