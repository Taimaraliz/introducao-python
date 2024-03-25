# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.

def remove_duplicatas(lista):

    conjunto_sem_duplicatas = set(lista)

    lista_sem_duplicatas = list(conjunto_sem_duplicatas)
    return lista_sem_duplicatas


lista_com_duplicatas = [1, 2, 3, 4, 2, 3, 5, 6, 4]

lista_sem_duplicatas = remove_duplicatas(lista_com_duplicatas)

# Imprimindo a lista
print(lista_sem_duplicatas)
