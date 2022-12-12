from random import randint

def roll(array, startIdx, iterations):
	if iterations == 0:
		return
	for num in range(iterations):
		temp = array[startIdx]
		for i in range(len(array[startIdx:-1])):
			array[startIdx+i] = array[startIdx+i+1]
		array[-1] = temp



def crabSort(array):
	for i in range(len(array)):
		roll(array, i, array[i:].index(min(array[i:])))


array = [randint(0, 1000) for i in range(500)]
print(array)
# crabSort(array)
print(array)