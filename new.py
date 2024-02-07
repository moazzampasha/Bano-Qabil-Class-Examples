'''#for open file
f=open('new1.txt')
print(f.read())


#for write in file
f=open('new2.txt','w')
f.write('hello')
f.close

#for assend the file
f=open('new2.txt','a')
f.write('new')
f.close

#use readline command
f=open('new1.txt')
print(f.readline())
print(f.readlines())
print(f.readline(100))'''


#CSV USE
import csv
with open('student.csv','w',newline='') as file:
   write=csv.writer(file)
   write.writerow(["SN","MOVIE","FOOD"])





