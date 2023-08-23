
def count_duplicates(input_string):
    d = {}
    no_of_duplicates = 0
    for str in input_string:
        if str in d.keys():
            d[str] = d[str] + 1
            if d[str] >1:
                no_of_duplicates = no_of_duplicates+1
        else:
            d[str] = 1
    return no_of_duplicates
def remove_duplicate_characters(new_statement):
    unique_chars = []
    for char in new_statement:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)
def reverse_string(input_string):
    reverse_str = ''
    i = len(input_string)-1
    while i>=0:
        reverse_str = reverse_str + input_string[i]
        i = i -1
    return reverse_str
def reverse_words(input_string):
    reverse_words_list = []
    for word in input_string.split():
        reverse_words_list.append(word[::-1])
    return " ".join(reverse_words_list)

def main():
    while True:
        try:
            input_string = input("Enter a statement: ")
            # count the no.of characters present in the string
            char_count = 0
            for char in input_string:
                char_count = char_count + 1
            print(f"Total no.of characters present in a string are {char_count}")
            #print(len(input_string))
            # count the no.of duplicate characters present in a given string
            print(count_duplicates(input_string))

            # count no.of words in a given string
            word_count = 0
            for word in input_string.split():
                word_count = word_count+1
            print(f'Total no.of words present in a given string are {word_count}') 

            # count the no.of duplicate words presenr in a given string
            print(count_duplicates(input_string.split()))  

            # reverse the given string
            print(reverse_string(input_string)) 

            # reverse the words present in the given string
            reverse_words_list = reverse_words(input_string)
            print("reversed words", reverse_words_list)
            new_statement = reverse_words_list
            print(f"new statement is: {new_statement}")
            latest_statement = remove_duplicate_characters(new_statement)
            print(latest_statement)
            another_statement = input("Do you want to continue with another statement?(Yes/NO):")
            if another_statement.lower() == 'yes':
                continue
            else:
                break
        except KeyboardInterrupt:
            print("Program interrupted by user.")
        # except ValueError as ve:
        #     print(f"ValueError: {ve}")
        # except KeyError as ke:
        #     print(f"KeyError: {ke}")
        # except IndexError as ie:
        #     print(f"IndexError: {ie}")
        # except TypeError as te:
        #     print(f"TypeError: {te}")
        # except (IOError, OSError) as ioe:
        #     print(f"IOError or OSError: {ioe}")
        # except MemoryError:
        #     print("MemoryError: Insufficient memory.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()






