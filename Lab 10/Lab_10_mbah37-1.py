# Moustapha Bah
# 10/28/2025
# Couting the frequency of words in a text file

from pathlib import Path

# Function to count the frequency of each word in the file
def count_word_frequency(fptr):
    
    word_count = {}
    
    '''Reads the first line from the file'''
    line = fptr.readline()
    
    ''' List of punctuation characters to be removed from the text'''
    punctChars = ('.', ',', '!', '?', ';', ':', '(', ')', '[', ']', '{', '}', '-', '_', '\n', '\r')
    
    ''' Process each line until the end of the file'''
    while line:
        
        ''' Replace each punctuation character with a space'''
        for c in punctChars:
            line = line.replace(c, ' ')
        
        words = line.split()
        contractions = []

        
        ''' Counting the frequency of each word'''
        for word in words:
           
            ''' if the word contains an apostrophe, it is considered a contraction'''
            word = word.strip('\'"')  # Removes leading/trailing quotes
            word = word.lower() 
            
            ''' Add the word to the contractions list if it is not empty'''
            if word:
                contractions.append(word)
        
            for tmp in contractions:   
                word_count[tmp] = word_count.get(tmp, 0) + 1
       
        ''' Read the next line from the file until the end of the file'''
        line = fptr.readline()
    
    return word_count

def print_word_frequency(word_count):
    
    ''' Print the word frequency in alphabetical order'''
    for word, count in sorted(word_count.items()):
        print(f"{word}: {count}")


'''' Main function to handle user input and file processing'''
def main():
    
    ''' Loop until a valid file is provided'''
    while True:
        file_name = input("Enter the filename: ")
   
        try:
            ''' Open the file for reading'''
            fptr = open(file_name,'r', encoding='utf-8')
        

            ''' Prints if file is not found '''
        except FileNotFoundError:
            print(f" Error: The file '{file_name}' was not found. Try again.")

            ''' Prints if file format is not correct/cannot be read '''
        except ValueError:
            print(f" Error: Could not read the file '{file_name}'.Please check the file format(.txt).")
        
            ''' If file is opened successfully, process the file '''
        else:
            word_count = count_word_frequency(fptr)
            print_word_frequency(word_count)
            fptr.close()
            break



if __name__ == "__main__":
    main()
    
        













    

    



