import random


def num_generate():
    return random.randint(1,100)

def generate_100():
    lista_100 = []
    for _ in range(100):
        new_value = num_generate()
        if new_value not in lista_100:
            lista_100.append(new_value)
    return  lista_100

def bubble_sort(lista):
    while True:
        swaped = False
        for i in range(0,len(lista)-1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista [i + 1]
                lista[i + 1] = aux
                swaped = True
        if swaped == False:
            return lista


if __name__ == '__main__':
    x = generate_100()
    print(x)
    print(bubble_sort(x))