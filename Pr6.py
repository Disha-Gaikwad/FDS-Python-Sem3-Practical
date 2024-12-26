#Write a Python program to store second year percentage of students in array. 
#Write function for sorting array of floating point numbers in ascending order using
#Insertion Sort and display top five scores
def insertionSort(arr):
	n = len(arr) 
	if n <= 1:
		return 
	for i in range(1, n): 
		key = arr[i] 
		j = i-1
		while j >= 0 and key < arr[j]: 
			arr[j+1] = arr[j] 
			j -= 1
		arr[j+1] = key 
arr = [35,89.6,65,54.3,78]
print("Percentage of second year students before Sorting")
print(arr)
print()
insertionSort(arr)
print("Percentage of second year students after sorting using Insertion Sort")
print(arr)
print()