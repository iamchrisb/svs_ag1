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

def is_matching(word, candidate, success_rate):
    correct = 0
    for x in xrange(len(word)):
        if word[x] == candidate[x]:
            correct += 1
    if correct == 0:
        return False
    rate =  float(correct) / float(len(word))
    print(word)
    print(candidate)
    print(correct)
    print(rate)
    
    if len(word) == 2:
        return rate >= 0.49
    
    return rate >= success_rate


def get_closest_word(word, candidates):
    if word in candidates:
        return word
    
    candidate = word
    
    for possible_candidate in candidates:
        if is_matching(word, possible_candidate, 0.60):
            return possible_candidate
    
    return candidate

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
    for k in keys:
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
    try:
        candidates = heuristic_word_dict[word_pattern]
    except KeyError:
        return old_mapping
    
    for cipher_letter in ciphered_word:
        index = ciphered_word.index(cipher_letter)
        for candidate in candidates:
            potential_letter = candidate[index]
            if not potential_letter in ignore_list:
                if not potential_letter in current_mapping[cipher_letter]:
                    current_mapping[cipher_letter].append(potential_letter)
    
    is_first = True
    for key,value in old_mapping.iteritems():
        if len(value) > 0:
            is_first = False
            break;
    
    if is_first:
        return current_mapping

    temp_mapping = initialize_cipher_mapping(analysisKey)
    for key, value in old_mapping.iteritems():
        cur_val = current_mapping[key]
        if len(value) == 0:
            temp_mapping[key] = cur_val
        else:
            temp_mapping[key] = intersect(value, current_mapping[key])
    return temp_mapping

######
#
#   BEGINNING OF CODE
#
######

#plain_text = open('moby_dick.txt').read().lower()
plain_text = open('text2.txt').read().lower()

alphabetStr = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabet = alphabetStr.split(" ")

tupleList = dict(zip(alphabet, sample(alphabet,len(alphabet))))

text_as_array = stringAsArray(plain_text)

ignore_list = ['\t','@','{','}','\xb1','[',']','+','$','/','\\','=','|','_','*','<','>','#','.', ',', ':',';','\x97','\x92','\x93','\x94','\'','!','-','&','(',')','%','"','?','0','1','2','3','4','5','6','7','8','9', '\n', ' ', '\r', '\xe2', '\x80', '\x9c', '\x99', '\x9d', '?', '!']

cipher_text = get_text_cipher(text_as_array)

print(cipher_text)

######
##
##  AFTER TEXT WAS CIPHERED
##
######

# heuristic ordering for english language
analysisKey = ["e", "t", "a", "o", "i", "n", "s", "r", "h", "l", "d", "c", "u", "m", "f", "p", "g", "w", "y", "b", "v", "k", "x", "j" , "q", "z" ]

heuristic_word_dict = getWordDictionary("big_dic.txt")

with open('heuristic_pattern.dict.json', 'w') as fp:
    json.dump(heuristic_word_dict, fp)

words = splitIntoWordsAndMarks(cipher_text, ignore_list)
cipher_mapping = initialize_cipher_mapping(analysisKey)

count = 0

for word in words:
    if not word in ignore_list:
        word_pattern = get_pattern(word)
        cipher_mapping = intersect_mapping(cipher_mapping, heuristic_word_dict, word_pattern, word)
    count += 1

deciphered_text = ""


def intersect(b1,b2):
    return list(set(b1).difference(b2))

pp = pprint.PrettyPrinter()
pp.pprint(cipher_mapping)

solvedCiphers = []

for key,value in cipher_mapping.iteritems():
    if len(value) == 1:
        solvedCiphers.append(key)

unsolvedCiphers = []

for key,value in cipher_mapping.iteritems():
    if(len(value)>1):
        unsolvedCiphers.append(key)

#sort unsolvedCiphers
print(unsolvedCiphers)
print("")
def reversedBubbleSort(cipherDict, unsolvedCiphers):
    for passnum in range(len(unsolvedCiphers)-1,0,-1):
        for i in range(passnum):
            currentUnsolvedCipherList = cipherDict[unsolvedCiphers[i]]
            currentUnsolvedCipherListNext = cipherDict[unsolvedCiphers[i+1]]
            if len(currentUnsolvedCipherList)<len(currentUnsolvedCipherListNext):
                temp = unsolvedCiphers[i]
                unsolvedCiphers[i] = unsolvedCiphers[i+1]
                unsolvedCiphers[i+1] = temp

reversedBubbleSort(cipher_mapping,unsolvedCiphers)

print(unsolvedCiphers)


run = 0
maxRuns = 20

while len(unsolvedCiphers) != 0:
    if run >= maxRuns:
        break
    
    run += 1

    print("solved: " + str(solvedCiphers))
    cipher = unsolvedCiphers.pop()

    unresolved = cipher_mapping[cipher]
    print("unresolved ciphers for " + cipher + " :::" + str(unresolved))
    
    k = intersect(unresolved,solvedCiphers)
    
    print("intersection: " + str(k))
    if len(k) == 1:
        cipher_mapping[cipher] = k
        solvedCiphers.append(cipher)
    else:
        unsolvedCiphers.insert(0,cipher);

pp.pprint(cipher_mapping)

# fuer jedes wort, ersetze entsprechenden buchstaben mit buchstaben aus dem key (wenn verfuegbar)
#   ueberpruefe mit einer heuristischer wortliste, welches wort die geringster fehlerquote hat
#       ueberpruefe ob es ein wort gibt und welches die geringste fehlerquote hat (min. weniger als x) -> return true/false
#       wenn true:
#           ueberpruefe ob mapped cipher solved is, if not set it
#   baue neuen key aus dem gewonnenen wort
#
#   gegebenfalls: zaehle haeufigkeiten des auftretens der buchstaben -> uebernehme den buchstaben mit der haechsten wahrscheinlichkeit

mostly_used_words_dict = getWordDictionary("words_english.txt")

def getNewWord(key,word):
    newWord = ""
    for letter in word:
        if len(key[letter]) > 0:
            newWord = newWord + key[letter][0]
        else:
            newWord = newWord + letter
    return newWord

def getWordWithLowestErrorRate(word, possibleWords):
    bestMatch = ""
    oldMatchRate = 0
    matches = 0
    for currentWord in possibleWords:
        for x in xrange(len(word)):
            if word[x] == currentWord[x]:
                matches += 1
        matchRate = float(matches) / float(len(word))
        if matchRate > oldMatchRate:
            oldMatchRate = matchRate
            bestMatch = currentWord
        matches = 0
    return bestMatch

def keyContainsLetter(cipher_mapping,letter):
    keys = cipher_mapping.keys()
    for x in xrange(len(keys)):
        value = cipher_mapping[keys[x]]
        if len(value) == 1:
            if value[0] == letter:
                return letter
    return None

def replaceLetter(cipher_mapping,heuristicWord,word):
    for x in xrange(len(word)):
        
        letter = word[x]
        values = cipher_mapping[letter]
        
        if len(values) == 1:
            continue
    
        containsLetter = False
        for key,value in cipher_mapping.iteritems():
            if len(value) == 1:
                print(heuristicWord[x])
                if value[0] == heuristicWord[x]:
                    containsLetter = True
                    break
        if not containsLetter:
            cipher_mapping[letter] = []
            cipher_mapping[letter].append(heuristicWord[x])


def keyIsComplete(cipher_mapping):
    keys = cipher_mapping.keys()
    
    for x in xrange(len(keys)):
        value = cipher_mapping[keys[x]]
        isNotComplete = (len(value) > 1) or (len(value) == 0 )
        if isNotComplete:
            return False
    return True


dict = {}
for letter in alphabet:
    dict[letter] = ""

pp.pprint(cipher_mapping)

for word in words:
    if word in ignore_list:
        continue
    
    if keyIsComplete(cipher_mapping):
        break

    currentNewWord = ""

    try:
        possible_words = mostly_used_words_dict[get_pattern(word)]
        newWord = getNewWord(cipher_mapping, word)
        heuristicWord = getWordWithLowestErrorRate(newWord, possible_words)
        replaceLetter(cipher_mapping,heuristicWord,word)
    except:
        print("pattern not found")


pp.pprint(cipher_mapping)

##########
#
#   decipher text with current mapping
#
##########

for letter in cipher_text:
    if not letter in ignore_list:
        if len(cipher_mapping[letter]) > 0:
            deciphered_text = deciphered_text + cipher_mapping[letter][0]
        else:
            deciphered_text = deciphered_text + letter
    else:
        deciphered_text = deciphered_text + letter

print(deciphered_text)
