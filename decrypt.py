#!../svs-vm/Scripts/python
from random import shuffle
import copy
from random import sample

#plain_text = "the manager consults the attack a b c d e f g h i j k l m n o p q r s t u v w x y z".lower()
plain_text = "Halt die Fresse krieg ein Kind".lower()
cipher_text = ""

alphabet = []
for i in range(32,123):
    alphabet.append(chr(i))

print(alphabet)

tupleList = zip(alphabet, sample(alphabet,len(alphabet)))

text_as_array = []
text_as_array[:0] = plain_text

for c1 in text_as_array:
    listIndex = alphabet.index(c1)
    newChar = tupleList[listIndex][1]
    cipher_text += newChar

print(cipher_text)

