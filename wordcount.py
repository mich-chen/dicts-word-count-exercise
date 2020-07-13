 # counts how many times each space-separated word occurs in that file
# print counts to the screen " word count"

def wordcount(filename):
    """ prints how many times each space-separated word occurs in a file """

    file = open(filename)
    # open filename and store object in file (contains each line)

    word_count = {}
    punctuation = (',', '.', '?', '!')

    for line in file:
        words = line.rstrip().split(' ')
        for word in words:
            word = word.lower()
            if word.endswith(punctuation):
                word_letters = []
                for letter in word:
                    if letter not in punctuation:
                        word_letters.append(letter)
                word = ''.join(word_letters)
                        
            word_count[word] = word_count.get(word, 0) + 1

    for key, value in word_count.items():
        print(key, value)

wordcount('test.txt')

