SET_BIT_COUNT = dict([(b, bin(b).count('1')) for b in range(2**8)])


def hamming_distance(b1, b2):
    assert len(b1) == len(b2)
    total_distance = 0

    for i in range(len(b1)):
        # XOR the two bytes, and count how much bits are set
        # (after XORing a bit is set if-and-only-if it was different
        # in b1 and b2)
        xored_byte = b1[i] ^ b2[i]
        total_distance += SET_BIT_COUNT[xored_byte]

    return total_distance