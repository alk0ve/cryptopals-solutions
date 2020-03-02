# doesn't sum exactly to 1 because floating point ¯\_(ツ)_/¯
ENGLISH_LETTER_FREQUENCY = {'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253,
    'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966,
    'j': 0.00153, 'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749,
    'o': 0.07507, 'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327,
    't': 0.09056, 'u': 0.02758, 'v': 0.00978, 'w': 0.0236, 'x': 0.0015,
    'y': 0.01974, 'z': 0.00074}

# maximum possible distance from the ideal frequency
MAX_DISTANCE = sum([(frequency ** 2)
    for frequency in ENGLISH_LETTER_FREQUENCY.values()]) ** 0.5 

# copy this
EMPTY_LETTER_COUNT_DICT = dict([(letter, 0) for letter in ENGLISH_LETTER_FREQUENCY])


def score_letter_frequency(text):
    letter_count = dict(EMPTY_LETTER_COUNT_DICT) # copy
    for c in text:
        c = chr(c).lower()
        if c in letter_count:
            letter_count[c] += 1
    
    total_letter_count = float(sum(letter_count.values())) # float for division later

    if total_letter_count == 0:
        return MAX_DISTANCE

    # convert to frequency
    for letter in letter_count:
        letter_count[letter] /= total_letter_count

    letter_frequency = letter_count
    total = 0

    for letter in ENGLISH_LETTER_FREQUENCY:
        total += ((letter_frequency[letter]
        - ENGLISH_LETTER_FREQUENCY[letter]) ** 2)

    return total ** 0.5
