# based on: https://web.archive.org/web/20170918020907/http://www.data-compression.com/english.html
# a to z
LETTER_FREQUENCY = [0.0651738, 0.0124248, 0.0217339, 0.0349835, 0.1041442, 0.0197881, 0.0158610, 0.0492888, 0.0558094, 0.0009033, 0.0050529, 0.0331490, 0.0202124, 0.0564513, 0.0596302, 0.0137645, 0.0008606, 0.0497563, 0.0515760, 0.0729357, 0.0225134, 0.0082903, 0.0171272, 0.0013692, 0.0145984, 0.0007836]
SPACE_FREQUENCY = 0.1918182

# clone this
EMPTY_CHAR_COUNT_DICT = dict([(b, 0) for b in range(0x100)])

ENGLISH_CHARACTER_FREQUENCY = dict(EMPTY_CHAR_COUNT_DICT)
for letter_index, freq in enumerate(LETTER_FREQUENCY):
    ENGLISH_CHARACTER_FREQUENCY[ord('a') + letter_index] = freq
ENGLISH_CHARACTER_FREQUENCY[ord(' ')] = SPACE_FREQUENCY


def score_letter_frequency(text):
    assert len(text) > 0
    char_count = dict(EMPTY_CHAR_COUNT_DICT) # clone
    for c in text:
        # normalize to lower case
        c = ord(chr(c).lower())
        char_count[c] += 1
    
    total_char_count = float(sum(char_count.values())) # float for division later

    # convert to frequency
    for char in char_count:
        char_count[char] /= total_char_count

    char_frequency = char_count
    distance = 0

    for b in range(0x100):
        distance += ((char_frequency[b]
        - ENGLISH_CHARACTER_FREQUENCY[b]) ** 2)

    return distance ** 0.5
