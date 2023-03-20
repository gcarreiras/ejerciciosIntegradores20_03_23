# Escribir una función que calcule el mínimo común múltiplo entre dos números


def calcularmcd(x, y):
    if y == 0:
        return x
    else:
        return calcularmcd(y, x % y)
    
def calcularmcm(a, b): 
    mcd = calcularmcd(a,b)
    return abs(a*b)//mcd


print (calcularmcd(180,324))