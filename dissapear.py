#Program that removes other characters of the string
strip =('a','e','i','o','u')#Charecteres a user wants to remove
#ask user to input sentence
sentence = input('Please enter the sentence')

new_sentence = ''
#strip the sentence and print the new sentence
for letter in sentence: #This is to loop through the sentence
    if letter not in strip: #Strip the sencence of vowels
        new_sentence += letter
print(new_sentence)
