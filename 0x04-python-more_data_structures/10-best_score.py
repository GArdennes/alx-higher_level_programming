#!/usr/bin/python3
def best_score(a_dictionary):
    sorted_dic = sorted(a_dictionary.items(), key=lambda x: x[1], reverse=True)
    if sorted_dic:
        return sorted_dic[0][0]
    else:
        return None
