#!../svs-vm/bin/python
#!../svs-vm/Scripts/python
from random import shuffle
import copy
import pprint, json
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

plain_text = open('moby_dick.txt').read().lower()

alphabetStr = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabet = alphabetStr.split(" ")

tupleList = dict(zip(alphabet, sample(alphabet,len(alphabet))))

text_as_array = stringAsArray(plain_text)

ignore_list = [",", ".", "?", "!" ,"\"" ,"\'", ":" ,"\t", "\n", "\x08", " ", "(", ")", "-", ";", "'", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "&", "[", "]"]

cipher_text = get_text_cipher(text_as_array)

######
##
##  AFTER TEXT WAS CIPHERED
##
######

#cipher_frequency = giveSortedFrequencyList(cipher_text, ignore_list)

#
# heuristic ordering
#
analysisKey = ["e", "t", "a", "o", "i", "n", "s", "r", "h", "l", "d", "c", "u", "m", "f", "p", "g", "w", "y", "b", "v", "k", "x", "j" , "q", "z" ]

heuristic_word_dict = getWordDictionary("big_dic.txt")

with open('heuristic_pattern.dict.json', 'w') as fp:
    json.dump(heuristic_word_dict, fp)

#print(compareTwoTexts(plain_text, text, ignore_list))

words = splitIntoWordsAndMarks(cipher_text, ignore_list)

#print(words)

#print(heuristic_word_dict[get_pattern("hello")])

def intersect(a, b):
    if len(b) == 0:
        return a
    return list(set(a) & set(b))

def initialize_cipher_mapping(alphabet):
    mapping_dict = {}
    for letter in alphabet:
        mapping_dict[letter] = []
    return mapping_dict

def intersect_mapping(old_mapping, heuristic_word_dict, word_pattern, ciphered_word):
    current_mapping = initialize_cipher_mapping(analysisKey)
    candidates = []
    print("old mapping: " + str(old_mapping))
    try:
       candidates = heuristic_word_dict[word_pattern]
    except KeyError:
        print("error occured")
        return old_mapping

    for cipher_letter in ciphered_word:
        index = ciphered_word.index(cipher_letter)
        for candidate in candidates:
            #print(candidate)
            potential_letter = candidate[index]
            if not potential_letter in ignore_list:
                if not potential_letter in current_mapping[cipher_letter]:
                    #print("potential letter to add: " + potential_letter + " word: " + candidate)
                    current_mapping[cipher_letter].append(potential_letter)

    print("analyzed ciphered letters: " + str(current_mapping))

    is_first = True
    for key,value in old_mapping.iteritems():
        if len(value) > 0:
            print("this isn't the first round: " + str(value))
            is_first = False
            break;

    if is_first:
        print("return the current mapping: " + str(current_mapping) + " because its the first time")
        return current_mapping

    #intersect both mappings
    print("intersecting mappings")
    temp_mapping = initialize_cipher_mapping(analysisKey)
    for key, value in old_mapping.iteritems():
        cur_val = current_mapping[key]
        print("length of value: " + str(len(value)))
        if len(value) == 0:
            print("key: " + str(key) + " | current value: " + str(cur_val))
            temp_mapping[key] = cur_val
            print(temp_mapping[key])
        else:
            print("key: " + str(key) + " | value: " + str(value))
            print("current mapping: " + str(current_mapping[key]))
            temp_mapping[key] = intersect(value, current_mapping[key])
            print("temp mapping: " + str(temp_mapping[key]))
    return temp_mapping


cipher_mapping = initialize_cipher_mapping(analysisKey)

count = 0

for word in words:
    print("current word: " + word)
    if not word in ignore_list:
        word_pattern = get_pattern(word)
        print("word : " + word + " | pattern: " + word_pattern)
        print("count: " + str(count))
        cipher_mapping = intersect_mapping(cipher_mapping, heuristic_word_dict, word_pattern, word)
        print("latest ciphers: " + str(cipher_mapping))
    count += 1

#print(cipher_mapping)

deciphered_text = ""

for letter in cipher_text:
    if not letter in ignore_list:
        if len(cipher_mapping[letter]) > 0:
            deciphered_text = deciphered_text + cipher_mapping[letter][0]
        else:
            deciphered_text = deciphered_text + letter
    else:
        deciphered_text = deciphered_text + letter

print(deciphered_text)

def is_matching(word, candidate, success_rate):
    correct = 0
    print(word)
    print(candidate)
    for x in xrange(len(word)):
        print("letter word: " + word[x])
        print("letter candidate: " + candidate[x])
        if word[x] == candidate[x]:
            correct += 1
    if correct == 0:
        return False
    rate =  float(correct) / float(len(word))
    print(rate)
    return rate >= success_rate


def get_closest_word(word, candidates):
    if word in candidates:
        return word

    candidate = word

    for possible_candidate in candidates:
        if is_matching(word, possible_candidate, 0.6):
            return possible_candidate

    return candidate

#words = splitIntoWordsAndMarks(cipher_text, ignore_list)
latest_words = splitIntoWordsAndMarks(deciphered_text, ignore_list)

mostly_used_words_dict = getWordDictionary("words_english.txt")

deciphered_last_version = ""
for y in xrange(len(words)):
    latest_word = latest_words[y]
    word = words[y]
    print(words[y])
    print(latest_word)
    if not latest_word in ignore_list:
        pattern = get_pattern(word)
        print(pattern)
        if pattern in mostly_used_words_dict:
            candidates = mostly_used_words_dict[pattern]
            word = get_closest_word(latest_words[y], candidates)
    deciphered_last_version = deciphered_last_version + word + " "

print(deciphered_last_version)