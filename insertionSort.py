import time
import random
start = time.time()
def insertionSort(arr):
	for i in range(len(arr)):
		for j in range(i,0,-1):
			if arr[j-1] > arr[j]:
				temp = arr[j-1]
				arr[j-1] = arr[j]
				arr[j] = temp
					
	
	
arr = random.sample(range(1000000,10000000),500)
insertionSort(arr)
end = time.time()
#print(arr)	
print(end-start)
