import math

sqrt5 = math.sqrt(5.0)
phi = (1.0 + sqrt5) / 2.0
psi = 1 - phi  # dasselbe wie (1 - sqrt5) / 2

def fibdir(n):
    x1 = math.exp(math.log(phi) * n)  # phi hoch n
    x2 = math.exp(math.log(-psi) * n)  # -psi hoch n

    if n % 2 != 0:
        x2 *= -1  # bei ungeradem n Minus ergänzen

    x = (x1 - x2) / sqrt5
    return int(x + 0.5)  # sonst würde fib(10) =54.9999999 zu 54 abgerundet

# Beispielaufruf
result = fibdir(10)
print(result)
