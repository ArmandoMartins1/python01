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