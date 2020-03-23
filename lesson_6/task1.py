#task1
########################
'''Task 1
Make a program that has some sentence (a string) on input and returns a dict containing
all unique words as keys and the number of occurrences as values. '''
import collections
str = input("Vvedite predlozhenie:\n")  #Vvod predlozhenija
punctuation = ['.',',',':',';','!','?','(',')']
wordList = str.split()
i = 0
for word in wordList:
    if word[-1] in punctuation:
        wordList[i] = word[:-1]
        word = wordList[i]
    if word[0] in punctuation:
        wordList[i] = word[1:]
    i += 1
print(f'{wordList}\n', collections.Counter(wordList))
