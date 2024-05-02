""" definir una funcion que dada una lista
retorne los elementos unicos de la lista"""



lista1 = [1, 2, 3, 3, 4, 5, 6]

"""def elementos_unicos(lista1):
    elementos_unicos = []
    for elemento in lista1:
        if elemento not in elementos_unicos:
            elementos_unicos.append(elemento)
    return elementos_unicos

print(elementos_unicos(lista1))"""

print(set(lista1))