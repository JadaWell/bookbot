def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = split_text(text)
    # print(text)
    print(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def split_text(stg):
    words = stg.split()
    return words







main()
