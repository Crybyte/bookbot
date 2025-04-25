from stats import get_num_words
from stats import get_char_stats
from stats import sort_stats

def get_book_text(fpath):
    txt = None

    with open(fpath) as f:
        txt = f.read()
    return txt

def main():
    text = None
    path = "books/frankenstein.txt"

    text = get_book_text(path)

    num_words = get_num_words(text)
    txt_stats = get_char_stats(text)
    ranked_stats = sort_stats(txt_stats)

    # print(f"{num_words} words found in the document")
    # print(txt_stats)
    # print(ranked_stats)

    print(f'''
============ BOOKBOT ============
Analyzing book found at {path}
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------''')
    for pair in ranked_stats:
        if pair["char"].isalpha():
            print(f"{pair["char"]}: {pair["num"]}")

    print("============= END ===============")
    
    return

main()
