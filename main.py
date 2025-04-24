def get_book_text(fpath):
    txt = None

    with open(fpath) as f:
        txt = f.read()
    return txt

def main():
    text = None
    path = "./books/frankenstein.txt"

    text = get_book_text(path)

    words = None
    words = text.split()

    count = 0
    for word in words:
        count += 1

    print(f"{count} words found in the document")

    return

main()
