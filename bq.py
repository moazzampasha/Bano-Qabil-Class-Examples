#write in file
f=open('first.txt','w')
f.write("pasha")
f.close()

#open text file
f=open('first.txt')
print(f.read())

#read and write
f=open('first.txt', 'a')
f.write("  So practice it daily")
f=open('first.txt')
print(f.read())