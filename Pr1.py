#Write a Python program to store marks scored in subject “Fundamental of Data Structure” by N students in the class. Write functions to compute following:
#a) The average score of class
#b) Highest score and lowest score of class
#c) Count of students who were absent for the test
#d) Display mark with highest frequency
marklist=[10,20,80,30,40,50,None,60,80,70,None,70,80]
total=0
ab_st=0
freq={ }
max_value=marklist[0]
min_value=marklist[0]
for mark in marklist:
 if mark== None:
   ab_st+=1
 else:
   total+=mark

if mark < min_value:
  min_value=mark
if max_value < mark :
  max_value=mark
if mark !=None:
  if freq.get(mark)==None:
   freq[mark]=1
  else:
   freq[mark]+=1
print(f"a.Average score of the class = {total/len(marklist)}")
print(f"b.Highest score = {max_value} \n Lowest score = {min_value}")
print(f"c.Number of absent students = {ab_st}")
highest_freq=0
highest_freq_mark=0
for mark in freq:
 if freq[mark]>highest_freq:
   highest_freq=freq[mark]
   highest_freq_mark=mark
print(f"d.Mark with highest frequency = {highest_freq_mark}")