# Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou menor que 10. O programa deve escrever a mensagem correspondente (maior ou menor) e informar o valor digitado pelo usuário.
def comparar_valores():
    num = input("Digite um número: ")

    if not num.replace('.', '', 1).isdigit():
        print("Valor inválido. Digite um número inteiro ou real.")
        return comparar_valores()

    if "." in num:
        num = float(num)
    else:
        num = int(num)

    if num > 10:
        print(f"{num} é maior que 10.")
    elif num < 10:
        print(f"{num} é menor que 10.")
    else:
        print(f"{num} é igual a 10.")

comparar_valores()


# Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou negativo (considere o valor zero como positivo).
num = input("Digite um número: ")

try:
    if "." in num:
        num = float(num)
    else:
        num = int(num)
except ValueError:
    print("Valor inválido. Digite um número inteiro ou real.")
else:

    if num >= 0:
        print(f"{num} é um número positivo.")
    else:
        print(f"{num} é um número negativo.")


# As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
def macas_compradas():
    try:
        quantidade = int(input("Digite o número de maçãs compradas: "))
    except ValueError:
        print("Quantidade inválida. Digite um número inteiro.")
        return macas_compradas()
    else:
        if quantidade < 0:
            print("Quantidade inválida. Digite um número inteiro positivo.")
            return macas_compradas()
        else:
            if quantidade < 12:
                print(f"{quantidade} maçã(s) custa(m) R$ {quantidade * 1.30:.2f}.")
            else:
                print(f"{quantidade} maçã(s) custa(m) R$ {quantidade * 1.00:.2f}.")

macas_compradas()


# Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print(f"Aprovado com média {media:.2f}.")
else:
    print(f"Reprovado com média {media:.2f}.")


# Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

maior = valor1 if valor1 > valor2 else valor2

print(f"{maior} é o maior valor.")


# Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

maior = valor1 if valor1 > valor2 else valor2
menor = valor2 if valor2 < valor1 else valor1

print(f"Valores em ordem crescente: {menor} e {maior}")


# Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.
numero_conta = input("Digite o número da conta: ")
saldo = float(input("Digite o saldo inicial: "))
debito = float(input("Digite o valor do débito: "))
credito = float(input("Digite o valor do crédito: "))

saldo_atual = saldo - debito + credito

if saldo_atual >= 0:
    mensagem = "Saldo Positivo"
else:
    mensagem = "Saldo Negativo"

print(f"Saldo atual: {saldo_atual:.2f} ({mensagem})")


# Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual a quantidade média, escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.
quantidade_atual = int(input("Digite a quantidade atual em estoque: "))
quantidade_maxima = int(input("Digite a quantidade máxima em estoque: "))
quantidade_minima = int(input("Digite a quantidade mínima em estoque: "))

quantidade_media = (quantidade_maxima + quantidade_minima) / 2

mensagem = "não efetuar compra" if quantidade_atual >= quantidade_media else "efetuar compra"

print(f"A quantidade média é {quantidade_media}, {mensagem}.")


# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# 
# Média de Aproveitamento Conceito
# Entre 9.0 e 10.0	A
# Entre 7.5 e 9.0	B
# Entre 6.0 e 7.5	C
# Entre 4.0 e 6.0	D
# Entre 4.0 e zero	E
# 
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

conceito = ""

if 9.0 <= media <= 10.0:
    conceito = "A"
elif 7.5 <= media < 9.0:
    conceito = "B"
elif 6.0 <= media < 7.5:
    conceito = "C"
elif 4.0 <= media < 6.0:
    conceito = "D"
else:
    conceito = "E"

print(f"Notas: {nota1} e {nota2}")
print("Média:", media)
print("Conceito:", conceito)
    
if conceito in ["A", "B", "C"]:
    print("APROVADO")
else:
    print("REPROVADO")
