# counts how many times each space-separated word occurs in that file
# print counts to the screen " word count"

# import sys


# def wordcount():
#     """ prints how many times each space-separated word occurs in a file """

#     filename = sys.argv[1]

#     # open filename and store object in file (contains each line)

#     word_count = {}
#     punctuation = (',', '.', '?', '!')

#     def unpunctuate(word):
        
#         word_letters = []
#         if word.endswith(punctuation):
#             word_letters = []
#             for letter in word:
#                 if letter not in punctuation:
#                     word_letters.append(letter)
#             word = ''.join(word_letters)
#         return word

#     for line in open(filename):
#         words = line.rstrip().split(' ')
#         for word in words:
#             word = word.lower()
#             word = unpunctuate(word)
                        
#             word_count[word] = word_count.get(word, 0) + 1

#     for key, value in word_count.items():
#         print(key, value)

# wordcount()

from collections import Counter
import sys

filename = sys.argv[1]

def wordcount(filename):
    """ prints how many times each space-separated word occurs in a file """

    punctuation = (',', '.', '?', '!')

    def unpunctuate(word):
        """ removes punctuation from word """

        if word.endswith(punctuation):
            word = word[:-1]
        return word
    
    file_object = open(filename)
    words = file_object.read().lower().rstrip("\n").split()
    # cleaned_words = [unpunctuate(word) for word in words]
    
    for key, value in Counter([unpunctuate(word) for word in words]).items():
        print(key, value)
        

wordcount(filename)

