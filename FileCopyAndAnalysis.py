#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Sidrah Hashmi #100915053

def main():
    with open("inp_file.txt", "w") as file:
        file.write("Python is an interpreted, high-level, and general-purpose programming language.")

    input_file_name = input("Enter the input file name: ")
    output_file_name = input("Enter the output file name: ")

    try:
        with open(output_file_name, "r"):
            pass
    except FileNotFoundError:
        print(f"The file {output_file_name} does not exist.")

    with open(input_file_name, "r") as input_file, open(output_file_name, "w") as output_file:
        line_count = 0
        char_count = 0

        for line in input_file:
            output_file.write(line)
            line_count += 1
            char_count += len(line)

        print(f"Number of lines copied: {line_count}")
        print(f"Number of characters copied: {char_count}")

    with open(output_file_name, "a") as output_file_append:
        output_file_append.write("\nIt was created by Guido van Rossum and first released in 1991.")

    with open(output_file_name, "r") as output_file_read:
        updated_line_count = 0
        updated_char_count = 0

        for line in output_file_read:
            updated_line_count += 1
            updated_char_count += len(line)

        print(f"\nUpdated number of lines in the output file: {updated_line_count}")
        print(f"Updated number of characters in the output file: {updated_char_count}")

        output_file_read.seek(0)  
        output_contents = output_file_read.read()
        print("\nContents of the output file:")
        print(output_contents)

        
if __name__ == "__main__":
    main()


# In[ ]:




