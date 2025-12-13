def get_book_text(
    book_path,
):  # Takes a filepath as input and returns contents as string
    with open(book_path) as book:
        book_contents = book.read()
        return book_contents


def get_word_count(text):
    words = text.split()
    return len(words)


def main():
    book_contents = get_book_text("./books/frankenstein.txt")
    num_words = get_word_count(book_contents)
    print(f"Found {num_words} total words")


main()
