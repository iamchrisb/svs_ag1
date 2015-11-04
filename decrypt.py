#!../svs-vm/bin/python
#!../svs-vm/Scripts/python
from random import shuffle
import copy
import pprint
from random import sample
from collections import OrderedDict

def prediction(letterOrder, orderedList, cipher_text):
    decryptedText = cipher_text;
    for letter in letterOrder:
        decryptedText = decryptedText.replace(orderedList.pop()[0], letter)
    return decryptedText

def sortDictForValue(dict):
    sortedList = sorted(dict.items(), key=lambda t: t[1])
    return sortedList

def giveSortedFrequencyList(text, ignore_list):
    i = 0
    frequencyDict = {}
    letterCount = 0
    
    textAr = stringAsArray(text)
    
    for c_i in textAr:
        if  c_i not in ignore_list:
            letterCount +=1
            frequencyDict[c_i] = frequencyDict.get(c_i, 0) + 1

    percentaged_array = []
    for tuple in sortDictForValue(frequencyDict):
        percentage = float(tuple[1]) / float(letterCount) * 100
        percentaged_array.append((tuple[0], round(percentage, 2)))

    return percentaged_array

def getAlphabetFromAscii():
    alphabet = []
    #for i in range(32,123):
    #    alphabet.append(chr(i))
    #print(alphabet)

def compareTwoTexts(text1, text2, ignore_list):
    if len(text1) != len(text2):
        return "the texts must have same length"

    count = 0
    failCount = 0
    valuableCount = 0

    text1_as_ar = stringAsArray(text1)
    text2_as_ar = stringAsArray(text2)

    for c1 in text1:
        c2 = text2_as_ar[count]
        if c1 not in ignore_list:
            if c1 != c2:
                failCount += 1
            valuableCount += 1
        count += 1

    return float(failCount) / float(valuableCount) * 100


def stringAsArray(text):
    text_as_array = []
    text_as_array[:0] = text
    return text_as_array

def getWordDictionary(file):
    word_list_text = open(file).read().lower()
    word_list_text = word_list_text.replace('\r', "")
    word_ar = word_list_text.split('\n')

    word_dict = {}

    for word in word_ar:
        index = get_pattern(word)
        if index == 0:
            continue
        value = word_dict.get(index, [])
        value.append(word);
        word_dict[index] = value
    return word_dict

def split(txt, seps):
    default_sep = seps[0]
    
    # we skip seps[0] because that's the default seperator
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
    return [i.strip() for i in txt.split(default_sep)]

def splitIntoWordsAndMarks(text, marks):
    text_as_array = []
    currentWord = ""
    i = 0
    length = len(text)
    while i < length:
        letter = text[0]
        if letter == " ":
            if len(currentWord) > 0:
                text_as_array.append(currentWord)
                currentWord = ""
        elif letter in marks:
            if len(currentWord):
                text_as_array.append(currentWord)
                currentWord = ""
            text_as_array.append(letter)
        else:
            currentWord += text[:1]
        text = text[1:]
        i += 1
    return text_as_array

def match_word(keys, word, word_dict):
    possible_matches = word_dict[len(word)]
    new_word = replace_letter(word, keys)
    #    print(possible_matches)
    #print(word)
    #    print(new_word)
    if new_word in possible_matches:
        return new_word
    return ""

def replace_letter(ciphered_word, keys):
    #    print("replace letter")
    for k in keys:
        #   print("key: " + str(k))
        ciphered_word = ciphered_word.replace(k[1][0], k[0])
    return ciphered_word

def find_word_with_pattern(word, word_dict):
    possible_words = word_dict[len(word)]

def get_pattern(word):
    pattern = ""
    count = 0
    old_letters = {}
    for c in word:
        if c in old_letters:
            old_letter = c
            pattern = pattern + str(old_letters[c])
        else:
            old_letters[c] = old_letters.get(c,count)
            pattern = pattern + str(count)
            count += 1
        pattern = pattern + "."
    return pattern

def get_text_cipher(text):
    cipher_text = ""
    for c1 in text_as_array:
        if tupleList.has_key(c1):
            newChar = tupleList[c1]
            cipher_text += newChar
        else:
            cipher_text += c1
    return cipher_text

####

ignore_list = [",", ".", "?", "!" ,"\"" ,"\'", ":" ,"\t", "\n", " ", "(", ")", "-", ";"]

plain_text = open('moby_dick.txt').read().lower()

alphabetStr = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabet = alphabetStr.split(" ")

tupleList = dict(zip(alphabet, sample(alphabet,len(alphabet))))

text_as_array = stringAsArray(plain_text)
cipher_text = get_text_cipher(text_as_array)

#print(compareTwoTexts(plain_text, cipher_text, ignore_list))


######
##
##  AFTER TEXT WAS CIPHERED
##
######

cipher_frequency = giveSortedFrequencyList(cipher_text, ignore_list)

#
# heuristic ordering
#
analysisKey = ["e", "t", "a", "o", "i", "n", "s", "r", "h", "l", "d", "c", "u", "m", "f", "p", "g", "w", "y", "b", "v", "k", "x", "j" , "q", "z" ]

#heuristic_word_dict = getWordDictionary("words.en.txt")
heuristic_word_dict = getWordDictionary("words_english.txt")
#print(heuristic_word_dict)

#print(compareTwoTexts(plain_text, text, ignore_list))

words = splitIntoWordsAndMarks(cipher_text, ignore_list)

#print(words)

print(heuristic_word_dict[get_pattern("hello")])

failRatio = 100
new_word_array = []
word_length = len(words)
analysed_words = words

reversed_cipher = list(reversed(cipher_frequency))
#print(reversed_cipher)
cipher_tuples                                                                                                                                                                                                                                           = []

i = 0
while i < len(reversed_cipher):
    tuple = reversed_cipher[i]
    new_tuple = ( analysisKey[i], tuple)
    cipher_tuples.append(new_tuple)
    i += 1

print(cipher_tuples)


def reku(machted_words, not_matched_words, all_words, used_keys, unused_keys, old_fail_ratio, wanted_fail_ratio, ignore_list, heuristic_word_dict):
    if old_fail_ratio <= wanted_fail_ratio:
        print(matched_words)
        return matched_words

    matched_words = []
    not_matched_words = []

    key = unused_keys.pop(0)

    prediction_keys = copy.copy(used_keys)
    prediction_keys.append(key)

#    print("predict keys: " + str(prediction_keys))

    for word in all_words:
        #        print("current word: " + word)
        if word in ignore_list:
            #matched_words.append(word)
            continue
        #print("predict keys in for: " + str(prediction_keys))
        prediction_word = match_word(prediction_keys, word, heuristic_word_dict)
        if len(prediction_word) > 0:
            #print("FOUND MATCHING WORD: " + prediction_word)
            matched_words.append(prediction_word)
        else:
            not_matched_words.append(prediction_word)

    new_fail_ratio = float(len(not_matched_words)) / float(len(all_words)) * 100
    print("current fail ratio: " + str(new_fail_ratio))
    print(unused_keys)
    if new_fail_ratio < old_fail_ratio:
        used_keys.append(key)
        reku(machted_words, not_matched_words, all_words, used_keys, unused_keys, new_fail_ratio, wanted_fail_ratio, ignore_list, heuristic_word_dict)
    else:
        unused_keys.append(key)
        unused_keys = sample(unused_keys, len(unused_keys))
        reku(machted_words, not_matched_words, all_words, used_keys, unused_keys, new_fail_ratio, wanted_fail_ratio, ignore_list, heuristic_word_dict)

#reku([], [], words, cipher_tuples[:3], cipher_tuples[3:], failRatio, 50, ignore_list, heuristic_word_dict)

'''
while failRatio > 60:
    randomKeys = heuristic_part + sample(random_part,len(random_part))
    rkeys = cipher_heuristic_part + sample(cipher_random_part, len(cipher_random_part))
    
    analysisKeys = dict(zip(rkeys, randomKeys))
    #print(analysisKeys)
    
    analysed_words = splitIntoWordsAndMarks(cipher_text, ignore_list)
    not_matched_words = []
    machted_words = []
    
    i = 0
    while i < word_length:
        currentWord = analysed_words[0];
        if currentWord in ignore_list:
            # if the word is a marker or smth like this, just add it to our new array
            machted_words.append(analysed_words.pop(0))
        else:
            match = match_word(analysisKeys, currentWord, heuristic_word_dict)
            if len(match) > 0:
                machted_words.append(analysed_words.pop(0))
            else:
                not_matched_words.append(analysed_words.pop(0))
        i += 1
#print(machted_words)
    print(len(not_matched_words))
    failRatio = round(float(len(not_matched_words)) / float(word_length) * 100, 0)
    print(failRatio)
#    print(not_matched_words)
#   failRatio = 4
'''