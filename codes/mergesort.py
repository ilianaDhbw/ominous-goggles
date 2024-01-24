def merge(a, b):
    i, j, k = 0, 0, 0  # Laufindizes
    c = [0] * (len(a) + len(b))  # Platz für Folge c

    while i < len(a) and j < len(b):  # bis ein Array leer ist
        if a[i] < b[j]:  
            c[k] = a[i]  
            i += 1
        else:
            c[k] = b[j]
            j += 1
        k += 1

    while i < len(a):
        c[k] = a[i] 
        i += 1
        k += 1

    while j < len(b):
        c[k] = b[j]
        j += 1
        k += 1

    return c  # Ergebnis abliefern

# Beispielaufruf:
if __name__ == "__main__":
    array_a = [1, 3, 5, 7, 9]
    array_b = [2, 4, 6, 8, 10]

    merged_array = merge(array_a, array_b)
    print("Merged Array:", merged_array)
