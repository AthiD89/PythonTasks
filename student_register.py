
#Program that asks the user how many students ID's they want to enter

num = int(input("How many students you want to enter?"))
#Counts the number of ID's entered
count = 0
list1 = []
while True: #Loop that runs for the amount of students you want to enter
        list1.append(num)
        student_id = int(input("Enter your ID number:"))
        choice = input("Want to stop? if yes press yes otherwise press any key")
        if choice == "yes":
            break
#Count and display how many student ID's have been entered
sum_list1 = 0


form = open("reg_form.txt", "w") #Opens the text file called reg_form
form.write("How many students")
for i in list1:
    sum_list1 = len(list1)
print("The ID numbers are:", student_id)

 
form.close()

