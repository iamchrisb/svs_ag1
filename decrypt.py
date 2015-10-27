#!../svs-vm/bin/python
#!../svs-vm/Scripts/python
from random import shuffle
import copy
from random import sample
from collections import OrderedDict

def prediction(letterOrder, orderedList, cipher_text):
    decryptedText = cipher_text;
    for letter in letterOrder:
        decryptedText = decryptedText.replace(orderedList.pop()[0], letter)
    return decryptedText

#plain_text = "the manager consults the attack a b c d e f g h i j k l m n o p q r s t u v w x y z".lower()
plain_text = 'We will now do an exercise that you must study very carefully. I want you to type this code in and try to understand what is going on. Take note of when you put things in e dict, get from a hash, and all the operations you use. Notice how this example is mapping states to their abbreviations, and then the abbreviations to cities in the states. Remember, mapping or associating is the key concept in a dictionary.'.lower()
cipher_text = ""

alphabetStr = "a b c d e f g h i j k l m n o p q r s t u v w x y z . ,"

alphabet = []
for i in range(32,123):
    alphabet.append(chr(i))

alphabet = alphabetStr.split(" ")
alphabet.append(" ")

print(alphabet)

tupleList = zip(alphabet, sample(alphabet,len(alphabet)))

text_as_array = []
text_as_array[:0] = plain_text

for c1 in text_as_array:
    listIndex = alphabet.index(c1)
    newChar = tupleList[listIndex][1]
    cipher_text += newChar

print(cipher_text)

print("")

frequencyDict = {}

for c in cipher_text:
    frequencyDict[c] = 0

for c in cipher_text:
    frequencyDict[c] = frequencyDict[c]+1

sortedList = sorted(frequencyDict.items(), key=lambda t: t[1])

print(plain_text)
print(" ")
print(cipher_text)
print(" ")

text = prediction([" ", "t", "e", "a", "i"], sortedList, cipher_text);

print(text)


