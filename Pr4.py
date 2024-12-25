#Write a Python program to store first year percentage of students in array. 
#Write function for sorting array of floating point numbers in ascending order using
#Bubble sort and display top five scores.
def Bubble_Sort(marks):
    n = len(marks)
    
    for i in range(n - 1):
        
        for j in range(0, n - i - 1):

           
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]

    print("Marks of students after performing Bubble Sort on the list :")
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
Bubble_Sort(marks)
a = input("\nDo you want to display top five marks from the list (yes/no) : ")
if a == 'yes':
    top_five_marks(marks)
else:
    print("Done")
     #flag = 0