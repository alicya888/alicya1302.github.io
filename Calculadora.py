#Calculadora simples
a = float(input("Digite o primeiro número:  "))
b = float(input("Digite o segundo número:  "))
m= input("O que deseja fazer: ")

soma = (a + b)
subtracao = (a - b)
multiplicacao= (a * b)
divisao= (a / b)

if m == "+":
    print(f"A soma de {a} e {b} é {soma}")

elif m == "-":
    print(f"A subtração de {a} e {b} é {subtracao}")

elif m == "*":
    print(f"A multiplicação de {a} e {b} é {multiplicacao}")

else:
    print(f"A divisão de {a} e {b} é {divisao}")
