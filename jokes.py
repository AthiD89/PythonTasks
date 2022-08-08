#List of jokes
jokes = ["What you get when you put radio in the fidge\n\t> Cool music", "What do you get when you are on fire?\n\t> A hot mess", "Why did the turtle cross the road?\n\t> To get to the other side.", "Why did the fat turkey cross the road?\n\t> To get hit my car"]

from random import randint #Impots randint
print(jokes[randint(0, len(jokes) -1)])#Prints the joke every time a code runs
   
