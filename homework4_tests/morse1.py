ALPHABET_TO_MORSE = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
}

LETTER_TO_MORSE = {letter: code + ' ' for letter, code in ALPHABET_TO_MORSE.items()}

def encode(message: str) -> str:
    """
    Кодирует строку в соответсвии с таблицей азбуки Морзе

    >>> encode('SOS')
    '... --- ...'

    >>> encode('')
    ''

    >>> encode('Hello, world!')
    '.... . .-.. .-.. ---                              .-- --- .-. .-.. -..'
    >>> encode('$$$$$$$')
    Traceback (most recent call last):
        ...
    ValueError: Invalid Morse code
    """
    encoded_signs = [
        LETTER_TO_MORSE.get(letter.upper(), '') for letter in message
    ]

    return ''.join(encoded_signs).strip()


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS)