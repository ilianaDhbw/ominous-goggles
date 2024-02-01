def quicksort(F, u, o):
    if o > u:
        l, r = zerlegen(F, u, o)
        quicksort(F, u, r)
        quicksort(F, l, o)

def zerlegen(F, u, o):
    p = F[(u + o) // 2]  # Pivot-Element
    l, r = u, o

    while l <= r:
        while F[l] < p:
            l += 1
        while F[r] > p:
            r -= 1
        if l <= r:
            # F[l] und F[r] tauschen
            F[l], F[r] = F[r], F[l]
            l += 1
            r -= 1

    return l, r

# Beispielaufruf
folge = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
quicksort(folge, 0, len(folge) - 1)
print(folge)
