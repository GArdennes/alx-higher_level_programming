#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:., ? and :
    Args:
        text: The text to be indented
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = text[:]
    for d in ".?:":
        list_t = s.split(d)
        s = ""
        for i in list_t:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d
    print(s[:-3], end="")
