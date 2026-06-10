def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

distances = [64, 25, 12, 45, 8, 33]
print("Before:", distances)
print("After:", bubble_sort(distances))