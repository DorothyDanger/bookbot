from stats import total_words
from stats import count_characters
from stats import sort_char_dictionary

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    total_words_count = total_words(text)
    character_count = count_characters(text)
    sorted_character_count = sort_char_dictionary(character_count)
    print("====== BOOKBOT ======")
    print(f"Analyzing book found at: {file_path}")
    print("------ Word Count ------")
    print(f"Found {total_words_count} total words.")
    print(" ------ Character Count ------")
    #for item in sorted_character_count:
        #print(f"{item['char']}: {item['num']}")
    for item in sorted_character_count:
        print(f"{item['char']}: {item['num']}")
    print("------ END ------")

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents

main()