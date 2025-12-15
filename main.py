from stats import get_character_count, get_word_count


def get_book_text(
    book_path,
):  # Takes a filepath as input and returns contents as string
    with open(book_path) as book:
        book_contents = book.read()
        return book_contents


def main():
    book_contents = get_book_text("./books/frankenstein.txt")
    num_words = get_word_count(book_contents)
    print(f"Found {num_words} total words")
    chars = get_character_count(book_contents)
    print(chars)


main()
