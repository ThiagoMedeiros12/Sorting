import random


def num_generate(n):
    return random.randint(1, n)


def generate_100(n=100):
    lista = []
    for _ in range(n):
        new_value = num_generate(n)
        if new_value not in lista:
            lista.append(new_value)
    return lista


def bubble_sort(lista):
    while True:
        swaped = False
        for i in range(0, len(lista) - 1):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                swaped = True
        if swaped == False:
            return lista


if __name__ == "__main__":
    x = generate_100()
    print(x)
    print(bubble_sort(x))
