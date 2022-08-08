#Enter students names and stop when done
list1 = []
while True:
        student = input("enter student names")
        list1.append(student)
        choice = input("Want to stop? if yes press yes otherwise press any key")
        if choice == "yes":
            break
#Count and display how many students entered
sum_list1 = 0
for i in list1:
    sum_list1 = len(list1)
print("The total number of students entered is:", sum_list1)
 
