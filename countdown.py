from itertools import combinations
from random import choice
import time

start = (r"""
 ____  ____  ____  ____  ____  ____  ____  ____
||K ||||E ||||Y ||||B ||||O ||||A ||||R ||||D ||
||__||||__||||__||||__||||__||||__||||__||||__||
|/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|
 ____  ____  ____  ____  ____  ____  ____  ____  ____
||C ||||O ||||U ||||N ||||T ||||D ||||O ||||W ||||N ||
||__||||__||||__||||__||||__||||__||||__||||__||||__||
|/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|

""")



def select_characters():
    sample_const ='bbcccddddddffggghhjklllllmmmmnnnnnnnnppppqrrrrrrrrrssssssssstttttttttvwxyz' # letter frequency of
    sample_vowel ='aaaaaaaaaaaaaaaeeeeeeeeeeeeeeeeeeeeeiiiiiiiiiiiiiooooooooooooouuuuu'        # consonants and vowels
    consonant =[] # empty lists i will adding the above consonant and vowels to
    vowel = []

    for i, in sample_const:    #iterate for each letter in the string
        consonant.append(i)    #add the string to the list
    for j in sample_vowel:
        vowel.append(j)


    # I'm doing this because I want to store my letters as a list (which has mutability), so I can remove them
    # off the 'stack' like Rachel does during the word game. Removing the occurrence of that given letter
    # increasing probabilities of others, this is a simple way of distributing probability distribution without
    # setting probability values in random.


    word = '' # An empty string variable to add my user given string onto.

    while len(word) < 9: # While the length of my work string is less than  nine letters loop.
        print('You have', (9-len(word)), 'Choices.') #displays letters left to pick
        x = str(input('''Please type 'c' for a consonant, or 'v' for a vowel        ''')) 
        if x in ['c', 'C', 'v', 'V']:   
            if x == 'v' or x == 'V':    
                letter = choice(vowel)  
                vowel.remove(letter)    
                word = word + letter    
                print(letter)          
                print('\n')
            else:
                letter = choice(consonant)
                consonant.remove(letter)
                word = word + letter
                print(letter)
                print('\n')

    alpha_word = ''.join(sorted(word))  
    print('Your letters are - ', word)     
    print('You have 30 seconds to think of an answer!')
    return word, alpha_word             


def dictionary_reader(filename):
    with open(filename) as f:             
        diction = f.readlines()            
                                           
    diction = [x.strip() for x in diction] 
    diction = [x.lower() for x in diction] 
    diction = list(dict.fromkeys(diction)) 

    return diction

def alpha_dictionary(dictionaryinput):
    alph_dict = []                       
    for word in dictionaryinput:          
        x = ''.join(sorted(word))         
        alph_dict.append(x)
    return alph_dict


def word_lookup(test_string, just_longest=True):
    output = []
    sorted_word = "".join(sorted(test_string))      # sorts word
    for i in range(len(sorted_word), 0, -1): # Reiterate for number of letters in word
        for substring_letters_list in combinations(sorted_word, i): # for combination of word
            substring_letters = "".join(substring_letters_list)     # create a list of combinations
            substring_letters = substring_letters.lower()           # lower case
            flag = 0
            while flag == 0:                     # the time costly solution
                if substring_letters in alpha_dictionary:
                    x = alpha_dictionary.index(substring_letters)
                    output.append(dictionary[x]) # add  found word to output
                    alpha_dictionary[x]=' '      # replace found word so substring can research
                                                 # ensures it iterates through the dictionary with every version.
                else:
                    flag -= 1
    if just_longest:
        output.sort(key=len, reverse=True)
        x = len(str(output[1]))
        most = []
        for word in output:
            if len(word) == x:
                most.append(word)
        return most

    return(output)

def user_Guess():

    guess = str(input('Enter the highest character word you can see.'))
    guess = guess.lower()   

    if guess in words_found: 
        score = len(guess)  
        print('Well done, your score is:', score)
    else:
        print('Sorry that is incorrect, better luck next time!')
    
    
    words_found.sort(key=len, reverse=True) 
    x = len(str(words_found[1]))
    most = []
    for word in words_found: 
        if len(word) == x:
            most.append(word)
    most_words = ', '.join(sorted(most))
    
    print('The largest words have', x, 'letters. These words are', most_words)
    

def countdownTimer():

    for i in reversed(range(0,31)):
        if i%5 == 0:
            print(i)
        time.sleep(1)

    
finish = (r"""

 ____  ____  ____  ____  ____  ____  ____  ____ 
||G ||||o ||||o ||||d ||||b ||||y ||||e ||||! ||
||__||||__||||__||||__||||__||||__||||__||||__||
|/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|

                    """)

if __name__ ==  "__main__":
    print(start)
    word, alpha_word = select_characters()
    countdownTimer()
    dictionary = dictionary_reader('words.txt')
    alpha_dictionary = alpha_dictionary(dictionary)
    words_found = word_lookup(word, just_longest=False)
    user_Guess()
    print (finish)
