import math

# A soma dos numeros
num1= int(input("Digite um numero: "))
num2= int(input("Digite um segundo numero: "))

print(num1 + num2)

# O produto do primeiro numero pelo quadrado do segundo
print(num1 * pow(num2,2))

# O quadrado do primeiro
print(pow(num1,2))

# A raiz quadrada da soma dos quadrados
print(float(math.sqrt(pow(num1,2)+ pow(num2,2))))

# O seno da diferença do primeiro número
print(math.sin(num1-num2))

# O modulo do primeiro numero
if num1 < 0:
    print(num1 * -1)
else:
    print(num1)
