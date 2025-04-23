file1=open("input1.txt","r")
file2=open("input2.txt","w")

lines=file1.readlines()
list1=[]
for i in lines:
    line=i.strip()
    list1.append(line)

list2=sorted(list1,key=lambda x:len(x))
for lines in list1:
    file2.write(lines + "\n")

file1.close()
file2.close()
