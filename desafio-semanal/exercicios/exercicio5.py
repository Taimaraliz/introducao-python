# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.

def calcular_preco_final(preco_original, desconto_percentual):
    desconto = preco_original * (desconto_percentual / 100)
    preco_final = preco_original - desconto
    return preco_final

def main():
    try:
        preco_original = float(input("Insira o preço original do produto: "))
        desconto_percentual = float(input("Insira o desconto percentual (%): "))

        if preco_original < 0 or desconto_percentual < 0:
            print("Por favor, insira valores válidos (positivos).")
            return

        preco_final = calcular_preco_final(preco_original, desconto_percentual)
        print("O preço final do produto após aplicar o desconto é:", preco_final)
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()
