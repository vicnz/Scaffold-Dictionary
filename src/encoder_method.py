# Encode Accented Characters
def encodeAccentLetters (string):
    array = bytearray(map(ord, string))
    return array.decode('utf8')