#!/usrs/bin/python3
def number_keys(a_dictionary):
    key_list = []
    for key in a_dictionary.keys():
        key_list.append(key)
    return len(key_list)
