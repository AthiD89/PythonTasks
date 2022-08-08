#Program to print each word in a new line
def printNewline(word):
    
    for i in range(len(word)):
        print(word[i])
#Ask the user to input a sentence         
printNewline(input("Please enter a sentence"))
