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
            word_count[tmp] = word_count.get(tmp, 0) + 1
        line = fptr.readline()
    return word_count

def print_word_frequency(word_count):
    for word, count in sorted(word_count.keys()):
        print(f"{word}: {count}")


def main():
    file_name = input("Enter the filename: ")
   
    try:
        with open(file_name,'r') as fptr:
            pass
    except FileNotFoundError:
        print(f" Error: The file '{file_name}' was not found.")
        
    else:
        word_count = count_word_frequency(fptr)
        print_word_frequency(word_count)


if __name__ == "__main__":
    main()
    
        













    

    



