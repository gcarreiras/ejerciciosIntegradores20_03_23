# Escribir una función que calcule el máximo común divisor entre dos números.


def calcularmcd(x, y):
    if y == 0:
        return x
    else:
        return calcularmcd(y, x % y)
    
    
print(calcularmcd(12,36))