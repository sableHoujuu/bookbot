import sys

from stats import get_character_count, get_sorted_count, get_word_count


def get_book_text(
    book_path,
):  # Takes a filepath as input and returns contents as string
    with open(book_path) as book:
        book_contents = book.read()
        return book_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}...")
    book_contents = get_book_text(path)
    num_words = get_word_count(book_contents)
    chars = get_character_count(book_contents)
    sorted_chars = get_sorted_count(chars)

    # We have everything we need, time to print the report
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_chars:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")


main()
