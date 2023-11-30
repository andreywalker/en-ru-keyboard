import re
import sys
import pyperclip



key_cl={
    "й": "q",
    "ц": "w",
    "у": "e",
    "к": "r",
    "е": "t",
    "н": "y",
    "г": "u",
    "ш": "i",
    "щ": "o",
    "з": "p",
    "х": "[",
    "ъ": "]",
    "ф": "a",
    "ы": "s",
    "в": "d",
    "а": "f",
    "п": "g",
    "р": "h",
    "о": "j",
    "л": "k",
    "д": "l",
    "ж": ";",
    "э": "'",
    "я": "z",
    "ч": "x",
    "с": "c",
    "м": "v",
    "и": "b",
    "т": "n",
    "ь": "m",
    "б": ",",
    "ю": ".",
    ".": "/",
    "ё": "`",

    "Й": "Q",
    "Ц": "W",
    "У": "E",
    "К": "R",
    "Е": "T",
    "Н": "Y",
    "Г": "U",
    "Ш": "I",
    "Щ": "O",
    "З": "P",
    "Х": "{",
    "Ъ": "}",
    "Ф": "A",
    "Ы": "S",
    "В": "D",
    "А": "F",
    "П": "G",
    "Р": "H",
    "О": "J",
    "Л": "K",
    "Д": "L",
    "Ж": ":",
    "Э": '"',
    "Я": "Z",
    "Ч": "X",
    "С": "C",
    "М": "V",
    "И": "B",
    "Т": "N",
    "Ь": "M",
    "Б": "<",
    "Ю": ">",
    ",": "?",
    "Ё": "~",
    
    "!": "!",
    '"': "@",
    "№": "#",
    ";": "$",
    "%": "%",
    ":": "^",
    "?": "&"
  
}

key_lc={
    'q': 'й',
    'w': 'ц', 
    'e': 'у', 
    'r': 'к', 
    't': 'е', 
    'y': 'н', 
    'u': 'г', 
    'i': 'ш', 
    'o': 'щ', 
    'p': 'з', 
    '[': 'х', 
    ']': 'ъ', 
    'a': 'ф', 
    's': 'ы', 
    'd': 'в', 
    'f': 'а', 
    'g': 'п', 
    'h': 'р', 
    'j': 'о', 
    'k': 'л', 
    'l': 'д', 
    ';': 'ж', 
    "'": 'э', 
    'z': 'я', 
    'x': 'ч', 
    'c': 'с', 
    'v': 'м', 
    'b': 'и', 
    'n': 'т', 
    'm': 'ь', 
    ',': 'б', 
    '.': 'ю', 
    '/': '.', 
    '`': 'ё', 


    'Q': 'Й', 
    'W': 'Ц', 
    'E': 'У', 
    'R': 'К', 
    'T': 'Е', 
    'Y': 'Н', 
    'U': 'Г', 
    'I': 'Ш', 
    'O': 'Щ', 
    'P': 'З', 
    '{': 'Х', 
    '}': 'Ъ', 
    'A': 'Ф', 
    'S': 'Ы', 
    'D': 'В', 
    'F': 'А', 
    'G': 'П', 
    'H': 'Р', 
    'J': 'О', 
    'K': 'Л', 
    'L': 'Д', 
    ':': 'Ж', 
    '"': 'Э', 
    'Z': 'Я', 
    'X': 'Ч', 
    'C': 'С', 
    'V': 'М', 
    'B': 'И', 
    'N': 'Т', 
    'M': 'Ь', 
    
    
    '<': 'Б', 
    '>': 'Ю', 
    '?': ',', 
    '~': 'Ё', 
    '!': '!', 
    '@': '"', 
    '#': '№', 
    '$': ';', 
    '%': '%', 
    '^': ':', 
    '&': '?'
    }




def transliterate_latin_to_cyrillic(text):
    # Replace Latin letters with Cyrillic counterparts
    text2=""
    j=0
    while (text[j] in key_cl.keys()) and (text[j] in key_lc.keys()):
        j+=1
        if j==len(text):
            j=0
            break

    if text[j] in key_cl.keys() :
        for i in range(0,len(text)):
            if text[i] in key_cl.keys():
                text2=text2+str(key_cl[text[i]])
            else:
                text2=text2+str(text[i])
            
    else:
        for i in range(0,len(text)):
            if text[i] in key_lc.keys():
                text2=text2+str(key_lc[text[i]])
            else:
                text2=text2+str(text[i])
    '''
    if text[0] in key_cl.keys() :
        for latin, cyrillic in key_cl.items():
            text = text.replace(latin, cyrillic)
    else:
        for cyrillic, latin in key_cl.items():
            text = text.replace(latin, cyrillic)
    '''
    return text2

def clean_text(input_text):
    # Initialize an empty list to store cleaned lines
    cleaned_lines = []

    # Split the input text into lines
    lines = input_text.split('\n')

    for line in lines:
    

        # Check if the cleaned line is not empty
        if line:
            # Append the cleaned line to the list
            cleaned_lines.append(line)

    # Join the cleaned lines back into a multiline string
    cleaned_text = '\n'.join(cleaned_lines)

    # Transliterate Latin letters to Cyrillic
    cleaned_text = transliterate_latin_to_cyrillic(cleaned_text)

    return cleaned_text

# Example usage:

user_input = pyperclip.paste()

cleaned_text = clean_text(user_input)
print()
print(cleaned_text)
pyperclip.copy(cleaned_text)
pyperclip.paste(cleaned_text)