valores = []

# Abrir o arquivo usando o context manager
with open("num.1000.2.in", "r") as arquivo:
    # Ler a primeira linha e converter para inteiro
    n = int(arquivo.readline().strip())
    
    # Ler as próximas n linhas e armazenar os valores em uma lista
    for _ in range(n):
        linha = arquivo.readline().strip()
        numero = int(linha)
        valores.append(numero)

# Agora 'valores' contém todos os inteiros do arquivo
print(valores[:10])  # Mostra os 10 primeiros valores como exemplo