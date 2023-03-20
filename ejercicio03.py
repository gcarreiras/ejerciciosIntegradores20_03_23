###  Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
###  cada palabra que contiene y la cantidad de veces que aparece (frecuencia).


def contar_palabras(unTexto):
    
    seRepiten = {} # creo el diccionario

    palabras = unTexto.split() #las separo x espacio

    for p in palabras:
        if p in seRepiten:
            seRepiten[p] += 1
        else:
            seRepiten[p] = 1

    return seRepiten

textoDePrueba = "En su capítulo sobre Corrupción y Falta de Transparencia en el Gobierno, el informe señaló que “en septiembre se estaban llevando a cabo varias investigaciones relacionadas con la corrupción contra figuras políticas de alto rango en ejercicio y ex, incluida la vicepresidenta Cristina Fernández de Kirchner"

cuantasHay = contar_palabras(textoDePrueba)

print (cuantasHay)