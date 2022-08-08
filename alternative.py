#ask user to input a string
str1 = input("Enter the string:")
#this is to print first name as capital
str1 = str1. title()
#Use of split function to split the string
s = str1.split()
r = ''
#for loop to loop through the string and to change the last word to capital 
for i in s:
   r = r+i [:-1] +i[-1].upper() +' '
print(r)
