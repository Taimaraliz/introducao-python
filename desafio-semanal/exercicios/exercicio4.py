# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

def contar_frutas(lista_frutas):
    contagem_frutas = {}

    for fruta in lista_frutas:
        if fruta in contagem_frutas:
            contagem_frutas[fruta] += 1
        else:
            contagem_frutas[fruta] = 1

    return contagem_frutas

def main():
    lista_frutas = ["maçã", "banana", "laranja", "abacaxi", "uva", "maçã", "banana", "maçã"]

    # Chama a função para contar as frutas
    contagem_frutas = contar_frutas(lista_frutas)

    # Imprime a contagem de frutas
    print("Contagem de frutas:")
    for fruta, quantidade in contagem_frutas.items():
        print(f"{fruta}: {quantidade}")

if __name__ == "__main__":
    main()
