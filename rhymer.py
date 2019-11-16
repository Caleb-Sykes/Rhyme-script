import sys

# Author: Caleb Sykes / Date: 16/11/2019
# the good rhymes are always at the top to middle; the bottom arent so good

vowels = ['a','e','i','o','u']
word = str(sys.argv[1])
wordl = list(word)
lst = []
lst2 = []

if len(sys.argv) > 2:
    print("Error: 1 argument needed, got "+str((len(sys.argv))-1))
    exit()

while len(wordl) > 0:
    for vowel in vowels:
        if wordl[0] == vowel:
            lst.append(wordl[0:])
    wordl.pop(0)

while len(lst) > 0:
    lst2.append("".join(lst[0]))
    lst.pop(0)

with open("words.txt","r+") as file:
    words = file.readlines()
    for base in lst2:
        for word in words:
            check = word
            if word[(-(len(base))-1):] == str(base+"\n"):
                print(check)
file.close()
