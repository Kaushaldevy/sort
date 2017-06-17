import time
import random
start = time.time()
def bubbleSort(arr):
	for j in range(len(arr)-1):
		for i in range(len(arr)-1):
			if arr[i] > arr[i+1]:
				temp = arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = temp



arr = random.sample(range(100,100000),500)
#arr = []
#arr = [1]
#arr = [1,2]
#arr = [4,4,4,4,4,4,4]
#arr = [1,2,3,4,5,6,7,8,9]
#arr = [9,8,7,6,5,4,3,2,1]
#arr = [1,3,3,3,3,3,3]
bubbleSort(arr)
end = time.time()
print(arr)
print(end-start)
