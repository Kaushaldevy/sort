import random

def mergeSort(arr):
    
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        j = k = i=0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k]=right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k]  =left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    
#Test cases

#arr = []
#arr = [1]
#arr = [1, 2]
#arr = [1,2,3,4,5]
#arr = [9,8,7,6,5]
#arr = random.sample(range(10,100),45)

mergeSort(arr)
print(arr)

