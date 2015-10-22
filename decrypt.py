#!../svs-vm/bin/python
from random import shuffle
import copy
from random import sample

plain_text = "The baroque finger returns under every poet.".lower()

cipher_text = ""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

dict = zip(alphabet, sample(alphabet,len(alphabet)))

print(dict);

for tupel1 in dict:
    print(tupel1)

text_as_array = []
text_as_array[:0] = plain_text

for c1 in text_as_array:
    


