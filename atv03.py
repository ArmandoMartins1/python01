from biblioteca import valorEstoque

nome = input("O nome do produto: ")
estoque = int(input("Estoque: "))
valor = float(input("preço do produto: "))

retorno = valorEstoque(nome, estoque, valor)
print(retorno)