#!/usr/bin/python3
'''Define text_indentation()'''

def text_indentation(text): 
    '''
        function prints text with space when either(.,? or :( occure 
    '''
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    while i < (len(text)):
        if text[i] =='.' or  text[i] == '?' or text[i] == ':':
            print(text[i], end="")
            i += 1
            print()
            if text[i] == ' ':
                i += 1
                print()
            continue
        print(text[i], end="")
        i += 1
