def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    text_to_lowercase = text.lower()

    lowercase_to_char = list(text_to_lowercase)

    char_to_dict = {}
    for char in lowercase_to_char:
        if char in char_to_dict:
            char_to_dict[char] += 1
        else:
            char_to_dict[char] = 1

    return char_to_dict

def grouping_dict_to_list(dict):
    grouped_list = []
    for i in dict:
        gropued_dict = {"char": i, "num": dict[i]}
        grouped_list.append(gropued_dict)

    return grouped_list

def sort_on(items):
    return items["num"]