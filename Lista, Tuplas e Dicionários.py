# Use um dicionário para armazenar informações sobre uma pessoa que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a cidade em que ela vive. Você deverá ter chaves como primeiro_nome, sobrenome, idade, e cidade. Por fim, mostre cada informação armazenada em seu dicionário.
def cadastrar_pessoas():
    pessoa = {}

    print(".: Cadastro de pessoas :.")
    nome = input("Digite o primeiro nome: ")
    sobrenome = input("Digite o sobrenome: ")
    idade = input("Digite a idade: ")
    cidade = input("Digite a cidade: ")

    pessoa['nome'] = nome
    pessoa['sobrenome'] = sobrenome
    pessoa['idade'] = idade
    pessoa['cidade'] = cidade

    print("Dados informados:")
    print("Nome:", pessoa['nome'])
    print("Sobrenome:", pessoa['sobrenome'])
    print("Idade:", pessoa['idade'])
    print("Cidade:", pessoa['cidade'])

    return pessoa


confirmacao = False

while not confirmacao:
    pessoa = cadastrar_pessoas()

    while True:
        resposta = input("Confirma os dados apresentados? (S/N): ")
        resposta = resposta.upper()

        if resposta == "S":
            confirmacao = True
            break
        elif resposta == "N":
            break
        else:
            print("Resposta inválida. Digite 'S' para sim ou 'N' para não.")

print("Cadastro concluído.")


# Use um dicionário para armazenar os números favoritos de algumas pessoas. Escolha cinco colegas, e pergunte quais seus números favoritos. Use seus nomes para serem as chaves de cada número favorito. Ao final, exiba o nome de cada pessoa e seu número favorito.
numeros_favoritos = {}
colegas = ['Ana', 'Brenda', 'Carla', 'Daniela', 'Eusébia']

for colega in colegas:
    numero_favorito = input("Digite o número favorito de " + colega + ": ")
    numeros_favoritos[colega] = numero_favorito

print("Números favoritos das pessoas:")
for colega, numero_favorito in numeros_favoritos.items():
    print(colega + ": " + numero_favorito)


# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
def calcular_media(aluno):
    print(f"Notas do aluno {aluno}")
    total = 0
    for a in range(0, 4):
        total += float(input(f"Digite a {a+1}ª nota: "))
    return total / 4


def exibir_media(lista):
    aprovados = []
    medias_aprovados = []
    for i, media in enumerate(lista):
        if media >= 7:
            aprovados.append(f"{i+1}º aluno")
            medias_aprovados.append(media)

    lista_aprovados_str = ', '.join(map(str, medias_aprovados))
    print(f"Alunos aprovados: {', '.join(aprovados)}")
    print(f"Médias dos alunos aprovados: {lista_aprovados_str}")
    print(f"Número de alunos aprovados: {len(aprovados)}")


medias = []
for a in range(0, 10):
    medias.append(calcular_media(a + 1))
    print()

exibir_media(medias)


# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
idades = [13, 12, 8, 22, 19, 12, 14, 16, 15, 11]
alturas = [1.62, 1.45, 1.53, 1.70, 1.55, 1.68, 1.72, 1.80, 1.48, 1.50]

media = sum(alturas) / len(alturas)

quantidadeAlunos = sum(1 for idade, altura in zip(
    idades, alturas) if idade > 13 and altura < media)

print("Número de alunos com mais de 13 anos e altura inferior à média: " +
      str(quantidadeAlunos))


# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
lista = []
for a in range(0, 5):
    lista.append(int(input("Digite um número inteiro: ")))
print(", ".join(map(str, lista)))
