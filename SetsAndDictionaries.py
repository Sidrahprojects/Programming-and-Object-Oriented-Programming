#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Sidrah Hashmi #100915053

######################################Program 1: Sets##############################################

def checkvowelsConsonants(sentence):
    vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
    num_vowels = 0
    num_consonants = 0

    for char in sentence:
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1

    return num_vowels, num_consonants

while True:
    print("Options:")
    print("1. Print the number of vowels and consonants")
    print("2. Exit the program")
    choice = input("Enter your choice: ")

    if choice == '1':
        sentence = input("Enter a sentence with special characters: ")
        sentence_list = list(sentence)

        num_vowels, num_consonants = checkvowelsConsonants(sentence_list)

        print(f"The number of vowels is {num_vowels} and consonants is {num_consonants}")
    elif choice == '2':
        break
    else:
        print("Invalid choice. Please select a valid option (1 or 2).")
        
#################end#######################################

############################Program 2: Dictionary###########################

def main():
    # b) Create a list of 20 Python keywords with duplicates
    keywordsList = [
        'and', 'del', 'global', 'while', 'for', 'in', 'else', 'print', 'return', 'import',
        'if', 'elif', 'break', 'continue', 'and', 'del', 'global', 'while', 'for', 'in'
    ]

    # c) Create an empty dictionary
    keyword_dict = {}

    # d) Iterate through the list and count the occurrence of each keyword
    for keyword in keywordsList:
        if keyword in keyword_dict:
            keyword_dict[keyword] += 1
        else:
            keyword_dict[keyword] = 1

    # e) Sort the dictionary based on the count of occurrence in descending order
    sorted_dict = dict(sorted(keyword_dict.items(), key=lambda item: item[1], reverse=True))

    # f) Print the sorted dictionary
    print("Keyword_name".ljust(10), "Count")
    for keyword, count in sorted_dict.items():
        print(f"{keyword.ljust(10)} {count}")

if __name__ == "__main__":
    main()
    
###############################End###############################

