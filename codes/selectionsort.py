def selection_sort(arr):
    for i in range(len(arr) - 1):
        pos = i  
        min_val = arr[i]  

        for j in range(i + 1, len(arr)):
            # Rest des Arrays soll durchlaufen werden und kleineres Element finden
            if arr[j] < min_val:
                pos = j  
                min_val = arr[j]  

        # Das bisher kleinstes Element soll mit dem aktuellen Element getauscht werden
        arr[pos] = arr[i]
        arr[i] = min_val

# Beispielaufruf:
if __name__ == "__main__":
    array_to_sort = [64, 25, 12, 22, 11]
    print("Unsortiertes Array:", array_to_sort)

    selection_sort(array_to_sort)

    print("Sortiertes Array:", array_to_sort)
