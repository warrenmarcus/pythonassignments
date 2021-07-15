# Warren Green
# 006314031

import random


wordlist = list()
# A function that reads content from a file
def read_file():

    file = open('example.txt', 'r')
    print(file.read())


# A function that scrambles letters in a word
def typoglycemia():
    punct = (".", ";", "?", ",")

    # puts the words from the example.txt file into a list to make it easier to manipulate
    # wasn't sure if this belonged in the function, but it seems to work this way
    with open("example.txt", "r") as file1:
        for line in file1:
         for word in line.split():
            wordlist.append(word)



    # variables for the for loop
    i = 0
    file2 = open("scrambled.txt", "w")
    newword =""

    for i in range(len(wordlist)):

        word = wordlist[i] # counts the index of the words instead of the list that the words are in
        if len(wordlist[i]) > 3:

            # split the words with punctuation up so they wouldnt get confused with normal letters
            if wordlist[i].endswith(punct):
                s_word = word[1:-2]
                s_word = random.sample(s_word, len(s_word))
                s_word.insert(0, word[0])
                s_word.append(word[-2])
                s_word.append(word[-1])
                newword = '' .join(s_word) + " "

            # for words without punctuation
            else:
                s_word = word[1:-1]
                s_word = random.sample(s_word, len(s_word))
                s_word.insert(0, word[0])
                s_word.append(word[-1])
                newword = ''.join(s_word) + " "
            file2.write(newword)

        # for words 3 letters or smaller
        else:
            file2.write(word + " ")


# calling the functions in the program


read_file()

typoglycemia()