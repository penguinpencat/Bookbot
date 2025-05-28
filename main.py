from stats import get_num_words, get_num_characters, get_sorted_list
from reporting import print_report
from filesystem import get_book_text
import sys

def main():
    if len(sys.argv) != 2:
        print("You haven't given the path to the book")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    num_words = get_num_words(book)
    individual_num_char = get_num_characters(book)
    sorted_list = get_sorted_list(individual_num_char)
    print_report(book_path, num_words, sorted_list)

main()
