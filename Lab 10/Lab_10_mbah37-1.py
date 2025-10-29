# Moustapha Bah
# 10/28/2025
# Couting the frequency of words in a text file

from pathlib import Path

def count_word_frequency(fptr):
    word_count = {}
    line = fptr.readline()
    punctChars = ('.', ',', '!', '?', ';', ':', '"', "'", '(', ')', '[', ']', '{', '}', '-', '_', '\n', '\r')

    while line:
        for c in punctChars:
            line = line.replace(c, ' ')
    
        words = line.split()
        for word in words:
            tmp = word.lower()
            word_count.get(tmp, 0) + 1
    return word_count












    

    



