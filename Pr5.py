#Write a Python program to store first year percentage of students in array. 
#Write function for sorting array of floating point numbers in ascending order using
#Selection sort and display top five scores.
def Selection_Sort(marks):
    for i in range(len(marks)):

        
        min_idx = i
        for j in range(i + 1, len(marks)):
            if marks[min_idx] > marks[j]:
                min_idx = j

        
        marks[i], marks[min_idx] = marks[min_idx], marks[i]

    print("Marks of students after performing Selection Sort on the list : ")
    for i in range(len(marks)):
        print(marks[i])
def top_five_marks(marks):
    print("Top",len(marks),"Marks are : ")
    print(*marks[::-1], sep="\n")


marks=[]
n = int(input("Enter number of students whose marks are to be displayed : "))
print("Enter marks for",n,"students (Press ENTER after every students marks): ")
for i in range(0, n):
    ele = float(input())
    marks.append(ele)  

print("The marks of",n,"students are : ")
print(marks)
Selection_Sort(marks)
a=input("\nDo you want to display top marks from the list (yes/no) : ")
if a=='yes':
    top_five_marks(marks)
else:
    print("Invalid choice")
