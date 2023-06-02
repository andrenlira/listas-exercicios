# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas. 
def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)
    custo_final = custo + imposto
    return custo_final

taxa_input = input("Digite a taxa percentual do imposto sobre vendas: ")
if taxa_input.endswith('%'):
    taxa_input = taxa_input[:-1]
taxa = float(taxa_input)

custo = float(input("Digite o preço do item: R$ "))

valor_final = somaImposto(taxa, custo)

print(f"O valor final do item é: R$ {valor_final:.2f}")


# Faça uma função que informe a quantidade de dígitos de uma determinada frase informada pelo usuário(a).
import re

def contar(frase):
    digitos = len(list(filter(str.isdigit, frase)))
    caracteres = len(frase)
    numeros = len(re.findall(r'\b\d+(\.\d+)?\b', frase))
    return digitos, caracteres, numeros

frase = input("Digite uma frase: ")

digitos, caracteres, numeros = contar(frase)

print(f"A frase inserida contém {digitos} dígitos (em {numeros} números) e {caracteres} caracteres.")


# Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
def numero_inteiro():
    numero_input = input("Digite um número inteiro: ")
    if not numero_input.isdigit():
        print("Digite um número inteiro válido.")
        return numero_inteiro()
    return int(numero_input)

def reverter(numero):
    numero_str = str(numero)
    reverso_str = numero_str[::-1]
    reverso_com_zeros = reverso_str.zfill(len(numero_str))
    return reverso_com_zeros

numero = numero_inteiro()

reverso = reverter(numero)

print("O reverso do número", numero, "é", reverso)