def bubble_sort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                # Elemente tauschen, wenn sie in falscher Reihenfolge sind
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

# Beispielaufruf:
if __name__ == "__main__":
    array_to_sort = [64, 34, 25, 12, 22, 11, 90]
    print("Unsortiertes Array:", array_to_sort)

    bubble_sort(array_to_sort)

    print("Sortiertes Array:", array_to_sort)
