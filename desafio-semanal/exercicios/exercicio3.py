# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.

def main():
    frutas = ["pera", "uva", "mamao", "abacaxi", "banana"]

    #
    frutas_ordenadas = sorted(frutas, key=str.lower)

    # Imprime a lista ordenada
    print("Lista de frutas em ordem alfabética:")
    for fruta in frutas_ordenadas:
        print(fruta)

if __name__ == "__main__":
    main()
