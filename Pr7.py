#Write a Python program to store second year percentage of students in array. 
#Write function for sorting array of floating point numbers in ascending order using
#Shell Sort and display top five scores
def shellSort(arr,n):

	n = len(arr)
	gap = n//2
	
	while gap > 0:
		for i in range(gap,n):
		
			temp = arr[i]
			
			j = i
			while j >= gap and arr[j-gap] >temp:
				arr[j] = arr[j-gap]
				j -= gap
			
			arr[j] = temp
		gap //= 2

arr = [ 82.3, 34, 54.8, 92, 73]
n = len(arr)
print ("Percentage of second year student before sorting:")
print(arr)
shellSort(arr,n)
print ("\nPercentage of second year student before sorting after sorting using Shell Sort:")
print(arr)
print()
top5=[]
for i in range(-4,1):
	top5.append(arr[-i])
print("top 5 elements",top5)
