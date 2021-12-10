#! python3
# rövarSpråk.py - Swedish (or any language) to Rövarspråk translator
# Developed as a further project from Chapter 6 of ATBS (Pig Latin)
import sys

def rövarSpråkTranslator(message):
    VOWELS = ('a','e','i','o','u','y','å','ä','ö') # Vowels (Swedish)
    translatedWords = [] # List for all translated words

    for word in message.split():
        if not word.isalpha(): # If the word is not alphabetical, skip it
            continue

        translatedWord = '' # Holds the translated word

        while len(word) > 0: # Loops through each character in word
            if word[0].lower() not in VOWELS:
                if word[0].lower() == 'x': #Exception case according to Wikipedia page
                    word = 'k' 
                    word = 's' + word
                if word[0].isupper():
                    translatedWord += word[0]
                else:
                    translatedWord += word[0].lower()
                translatedWord += 'o' + word[0].lower()
            else: 
                if word[0].isupper:
                    translatedWord += word[0]
                else: 
                    translatedWord += word[0].lower()
            word = word[1:] # Removes the first character of word

        translatedWords.append(translatedWord) # Appends the translated word to list

    return ' '.join(translatedWords) # Joins together all words into one string

if len(sys.argv) == 2: # If an argument exists, translate it
    print(rövarSpråkTranslator(sys.argv[1]))
    sys.exit()
elif len(sys.argv) > 2: # If there are more than 2 arguments, return usage instructions
    print("Usage: python rövarSpråk.py [str]")
else: # ELse, run main program
    message = input('Enter message to be translated into Rövarspråk: ') 
    translatedMessage = rövarSpråkTranslator(message)
    print(translatedMessage)
