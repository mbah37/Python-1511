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

def print_word_frequency(word_count):
    for word, count in sorted(word_count.items()):
        print(f"{word}: {count}")


def main():
    while True:
        filename = input("Enter the filename: ")
   
        try:
            filepath = Path(filename)
    
        except FileNotFoundError:
            print("File not found. Please check the filename and try again.")
            continue
        else:
            with filepath.open('r') as fptr:
                word_count = count_word_frequency(fptr)
                print_word_frequency(word_count)
            break
            
    
        













    

    



