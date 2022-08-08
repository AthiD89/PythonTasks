numbers = []
f = open("numbers1.txt", "w") #Opens file number1.txt 

for i in range (5):#Writes intigers into the file
    f.write('intiger %d\n' %(i+1))
    print(i+1)
f.close()#closes the file

f = open("numbers2.txt", "w")#Opens file number2.txt
for i in range (5,10):#Writes intigers into the file
    f.write('intiger %d\n' %(i+1))
    print(i+1)
f.close()#closes the file

f = open("all_numbers.txt", "w") #Opens file all_number.txt
f.write(str(numbers))
print(numbers)

f.close
