#In second year computer engineering class, group A student’s play cricket, group B students play badminton and group C students play football.
#Write a Python program using functions to compute following: -
#1.List of students who play both cricket and badminton
#2.List of students who play either cricket or badminton but not both
#3.Number of students who play neither cricket nor badminton
#4.Number of students who play cricket and football but not badminton.
comp=[ ]
n=int(input("Enter the no. of students : "))
for i in range(n):
 a=input("Enter the name of student : ")
 comp.append(a)
print("List of students in class is : ",comp)

cric=[ ]
n1=int(input("Enter the no. of students playing Cricket : "))
for j in range(n1):
 b=input("Enter the name of student : ")
 cric.append(b)
print("List of students in class is : ",cric)

badm=[ ]
n2=int(input("Enter the no. of students playing Badminton : "))
for k in range(n2):
 c=input("Enter the name of student : ")
 badm.append(c)
print("List of students in class is : ",badm)
 
foot=[ ]
n3=int(input("Enter the no. of students playing Football : "))
for l in range(n3):
 d=input("Enter the name of student : ")
 foot.append(d)
print("List of students in class is : ",foot)

def candb(a,b):
 l=[ ]
 for i in a:
   if i in b:
     l.append(i)
 print("List of students in Cricket and Badminton : ",l)

def corb(a,b):
 l=[ ]
 for i in a:
    if i not in b:
     l.append(i)
 print("List of students in either Cricket or Badminton : ",l)

def f(a,b,c):
 l=[]
 for i in c:
  if i not in a:
   if i not in b:
     l.append(i)
 print("List of students in Football : ",l)

def candf(a,b,c):
 l=[]
 for i in a:
  if i in c:
   if i not in b:
     l.append(i)
 print("List of students in Cricket and Football but not in Badminton : ",l)

flag=1
while flag==1:
  choice=int(input("Enter the choice enter 1 for students playing both Cricket and Badminton\nEnter 2 for students playing either Cricket or Badminton\nEnter 3 for students playing neither Cricket nor Badminton\nEnter 4 for students playing Cricket and Football but not Badminton "))
  if choice==1:
    print("Students playing both Cricket and Badminton are : ")
    candb(cric,badm)
  elif choice==2:
    print("Students playing either Cricket or Badminton are : ")
    corb(cric,badm)
  elif choice==3:
    print("Students playing neither Cricket nor Badminton are : ")
    f(cric,badm,foot)
  elif choice==4:
    print("Students playing both Cricket and Football but not Badminton are : ")
    candf(cric,badm,foot)
  else:
    print("Invalid choice")
  A= input("Say yes to continue with the program and no for exit ")
  if A =="yes":
    flag==1
  else:
    flag=0