def get_num_words(txt):
    words = None

    words = txt.split()
    
    return len(words)

def get_char_stats(txt):
    # we start with a whole string
    
    # we can split that into "words"
    words = None
    words = txt.split()

    # for each word we work through "letters" 
    letters = {}

    for word in words:
        #print(f"debug: word in words = {word}")
        # each character gets it's key added to dictionary
        for letter in word:
            letter = letter.lower()
            #print(f"debug: letter in word = {letter}")

            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 0
                letters[letter] += 1
    # after checking if added, increment
    # after all done, return dictionary
    return letters

def get_num(kv_set):
    # print(f"DEBUG: sort_second kv_set is {kv_set}, return is {kv_set["num"]}")
    return kv_set["num"]

def sort_stats(raw_dict):
    sorted_list = []
    # each entry should be coverted
    for char_key in raw_dict:
        kv_pair = {"char": char_key, "num": raw_dict[char_key]}
        sorted_list.append(kv_pair)
    # into: {"char": "b", "num": 123}
    # use .sort() to sort by 2nd key in reverse
    # print(f"debug: non sorted_list is {sorted_list}")
    sorted_list.sort(key=get_num, reverse=True)
    # print(f"debug: sorted_list is {sorted_list}")
    return sorted_list
