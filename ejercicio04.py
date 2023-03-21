# . Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia

def contar_palabras(unTexto):
    
    seRepiten = {} 

    palabras = unTexto.split() 

    for p in palabras:
        if p in seRepiten:
            seRepiten[p] += 1
        else:
            seRepiten[p] = 1

    return seRepiten

def funcion_en_tupla (seRepiten):
    #las variables auxiliares que voy a usar para almacenar la palabra y las veces que se repite
    contador_max = ""
    frecuencia_max = 0

    for p , seRepite in seRepiten.items():
        if seRepite > frecuencia_max:
            contador_max = p
            frecuencia_max = seRepite

    return(contador_max, frecuencia_max)



textoDePrueba = "Además de la aplicación de Salud en los dispositivos de Apple, la compañía de tecnología estaría pensando en expandir los servicios relacionados al cuidado personal de sus clientes con una nueva función para los AirPods. Entre los planes de la empresa estaría el implementar sus audífonos con tecnología que tenga la capacidad de diagnosticar problemas de salud auditiva en desarrollo."

cuantasHay = contar_palabras(textoDePrueba)

print (cuantasHay)

contador_max , frecuencia_max = funcion_en_tupla(cuantasHay)
print(f"la palabra mas repetida es'{contador_max}' con {frecuencia_max} veces" )

