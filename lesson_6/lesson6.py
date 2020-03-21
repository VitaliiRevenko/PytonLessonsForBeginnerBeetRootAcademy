#task1
########################
str = input("Vvedite predlozhenie:\n")
punctuation = ['.',',',':',';','!','?','(',')']
wordList = str.split()
#wordDict = {}
i = 0
for word in wordList:
    if word[-1] in punctuation:
        wordList[i] = word[:-1]
        word = wordList[i]
    if word[0] in punctuation:
        wordList[i] = word[1:]
    i += 1
print(f"{wordList},\n" , set(wordList))