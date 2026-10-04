from morse import morse

def to_morse(text):
    words = text.split(' ')
    morse_words = []
    for word in words:
        morse_letters = []
        for char in word:
            if char in morse:
                morse_letters.append(morse[char])
        morse_words.append(' '.join(morse_letters))
    return ' / '.join(morse_words)

def from_morse(code):
    reverse_morse = {v: k for k, v in morse.items()}
    words = code.split(' / ')
    decoded_words = []
    for word in words:
        letters = word.split(' ')
        decoded_letters = []
        for letter in letters:
            if letter in reverse_morse:
                decoded_letters.append(reverse_morse[letter])
        decoded_words.append(''.join(decoded_letters))
    return ' '.join(decoded_words)

if __name__ == "__main__":
    print(to_morse("PYTHON 3"))
    print(to_morse("SOS"))
    print(from_morse(".--. -.-- - .... --- -. / ...--"))
    print(from_morse("... --- ..."))