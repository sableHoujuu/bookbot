def get_book_text(
    book_path,
):  # Takes a filepath as input and returns contents as string
    with open(book_path) as book:
        book_contents = book.read()
        return book_contents


def main():
    book_contents = get_book_text("./books/frankenstein.txt")
    print(book_contents)


main()
