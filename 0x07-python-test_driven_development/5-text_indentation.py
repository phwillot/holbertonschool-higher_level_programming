#!/usr/bin/python3
"""
Module for text_indentation function
"""


def text_indentation(text):
    """text_indentation -
    Prints a text with 2 newlines after each of these character
    "." "?" and ":"
    @text: string to format
    Return: None
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    separators = [".", "?", ":"]

    if text.isspace():
        return

    text = text.strip()

    for i in range(len(text)):
        if i != 0:
            if text[i - 1] in separators and text[i] in separators:
                print(text[i] + "\n")
            if text[i - 1] in separators and not text[i].isalpha():
                continue
        if text[i] not in separators:
            print(text[i], end="")
        else:
            print(text[i] + "\n")
