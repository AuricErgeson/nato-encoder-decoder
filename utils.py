from natoPhonetic import Nato
from humre import*
import re

def nato_reverse(Nato_dict:dict)->dict:
    Nato_reverse = {}
    for key,value in Nato_dict.items():
        Nato_reverse[value] = key
    return Nato_reverse

def encoder(text):
    text_splitted = text.split(' ')
    new_text = [ ]
    for word in text_splitted:
        word_result = ''
        for char in word.upper():
            if char in Nato.keys():
                word_result += Nato.get(char,'')
        new_text.append(word_result)
    encoded_message = ''.join(new_text)
    print(f"The original version: {text} \nThe encoded version: {encoded_message}")
    #return encoded_message

def decoder(text):

    encoded_message = text.split(' ')
    decoded_words = []
    pattern = chars('A-Z') +zero_or_more(chars('a-z'))

    for chunk in encoded_message:
        parts = re.compile(pattern).findall(chunk)
        letters =''
        for part in parts:
            letters += nato_reverse(Nato).get(part,'')
        decoded_words.append(letters)

    decoded_message = ' '.join(decoded_words)

    print(f"The encoded version: {text} \nThe the decoded version: {decoded_message}")


