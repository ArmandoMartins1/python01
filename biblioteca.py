def imprime_nome(nome):
    print(f"Nome: {nome}")

def solicitarNome():
    nome = input("Digite seu nome: ")
    return nome

def piramideNumero(n):
    for i in range(1, n + 1, 1):
        for j in range(i):
            print(i, end=" ")
        print()

def contaVogal(texto):
    cont = 0
    for x in range(len(texto)):
        if texto[x] == "a" or texto[x] == "e" or texto[x] == "i" or texto[x] == "o" or texto[x] == "u":
            cont = cont + 1
    print(cont)

def valorEstoque (nome_produto,estoque_produto,valor_unitario):
    vTotal = estoque_produto*valor_unitario
    return vTotal