import sys
from stats import get_num_words
from stats import get_num_char
from stats import grouping_dict_to_list
from stats import sort_on

def get_book_text(path):
    with open(path) as f:
        file_conttents = f.read()

    return file_conttents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]

    book_text = get_book_text(path_to_book)

    char_dict = get_num_char(book_text)

    char_list = grouping_dict_to_list(char_dict)

    char_list.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    for i in char_list:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()