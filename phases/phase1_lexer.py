"""
PHASE 1: Lexical Analyzer (Token Recognition)
Reads a string and identifies valid integer literals
"""

import re


def lexer(text):
    """
    Tokenizes input string into integer literals.
    Returns list of tuples: (token_type, token_value)
    """
    tokens = []
    i = 0
    
    while i < len(text):
        # Skip whitespace
        if text[i].isspace():
            i += 1
            continue
        
        # Try hex literal: 0x or 0X followed by hex digits
        if text[i:i+2].lower() == "0x":
            j = i + 2
            while j < len(text) and text[j] in "0123456789abcdefABCDEF":
                j += 1
            if j > i + 2:  # at least one hex digit
                tokens.append(("INT_HEX", text[i:j]))
            else:
                tokens.append(("INVALID", text[i:j]))
            i = j
        elif text[i].isdigit():
            j = i
            while j < len(text) and text[j].isdigit():
                j += 1
            if j < len(text) and text[j].isalpha():  # trailing letters
                tokens.append(("INVALID", text[i:j+1]))
                i = j + 1
            else:
                tokens.append(("INT", text[i:j]))
                i = j
        else:
            tokens.append(("INVALID", text[i]))
            i += 1
    
    return tokens


if __name__ == "__main__":
    source = input("Enter integer literals: ")
    print("\nTokens:")
    for tok in lexer(source):
        print(f"  TOKEN: {tok[0]:<12} Value: {tok[1]}")
