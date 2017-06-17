import random
def quickSort(arr,start,end):
   if start < end:

       pivot = partition(arr,start,end)

       quickSort(arr, start, pivot - 1)
       quickSort(arr, pivot + 1, end)

def partition(arr, start, end):
   pivotvalue = arr[start]

   left = start + 1
   right = end

   reached = False
   
   while not reached:

       while left <= right and arr[left] <= pivotvalue:
           left += 1

       while arr[right] >= pivotvalue and right >= left:
           right -= 1

       if right < left:
           reached = True
       else: #swap left value with the right value
           temp = arr[left]
           arr[left] = arr[right]
           arr[right] = temp
           
   #swap	
   temp = arr[start]
   arr[start] = arr[right]
   arr[right] = temp
   return right

#Test cases
#arr = random.sample(range(20,300), 150)
#arr = []
#arr = [1]
#arr = [1, 2]
#arr = [1,2,3,4,5]
arr = [9,8,8,8,7,9,7,6,5]
quickSort(arr, 0, len(arr)-1)

print(arr)
