def get_num_words(book_txt):
    book_words = len(book_txt.split())
    return book_words

def get_num_characters(book_text):
    dict_num_characters = {}
    for character in book_text:
        character = character.lower()
        if character in dict_num_characters:
            dict_num_characters[character] += 1
        else:
            dict_num_characters[character] = 1
    return dict_num_characters

def sort_on(dict):
    return dict["num"]

def get_sorted_list(char_dict):
    sorted_character_list = []
    for char in char_dict:
        new_dict = {"char": char, "num" : char_dict[char]}
        sorted_character_list.append(new_dict)
    sorted_character_list.sort(reverse=True, key=sort_on)
        
    return(sorted_character_list)

#get_sorted_list({'t': 29493, 'h': 19176, 'e': 44538, ' ': 70480, 'p': 5952, 'r': 20079, 'o': 24494, 'j': 497, 'c': 9011, 'g': 5795, 'u': 10111, 'n': 23643, 'b': 4868, 'k': 1661, 'f': 8451, 'a': 25894, 's': 20360, 'i': 23927, ';': 1350, ',': 5962, 'm': 10206, 'd': 16318, '\n': 7629, 'y': 7756, 'w': 7450, 'l': 12306, 'v': 3737, '.': 3121, '-': 173, ':': 211, '2': 19, '3': 15, '0': 18, '1': 91, '[': 2, '#': 1, '4': 12, '5': 12, ']': 2, '&': 5, '8': 24, '/': 8, '*': 97, '’': 144, 'x': 691, '_': 124, 'q': 325, '?': 208, '—': 123, '6': 9, 'z': 235, '(': 35, ')': 35, '7': 18, 'æ': 28, '!': 201, '“': 506, '”': 316, '9': 9, 'ë': 2, '‘': 43, 'â': 8, 'ê': 7, 'ô': 1, '™': 57, '•': 4, '%': 1, '$': 2})