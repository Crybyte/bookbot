from stats import get_num_words

def get_book_text(fpath):
    txt = None

    with open(fpath) as f:
        txt = f.read()
    return txt

def main():
    text = None
    path = "./books/frankenstein.txt"

    text = get_book_text(path)

    num_words = get_num_words(text)

    print(f"{num_words} words found in the document")

    return

main()
