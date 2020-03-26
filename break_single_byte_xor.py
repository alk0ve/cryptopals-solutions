import char_freq
import sys
import base64
import binascii
import mybytes


def main():
    assert len(sys.argv) == 3
    with open(sys.argv[1], 'r') as f:
        encrypted_lines = [binascii.unhexlify(line) for line in f.read().split()]
    cutoff = float(sys.argv[2])

    results = []

    for i, encrypted_line in enumerate(encrypted_lines):
        for xor_byte in range(0x100):
            guess = mybytes.xor_bin_single_char(encrypted_line, xor_byte)
            score = char_freq.score_letter_frequency(guess)
            if score < cutoff:
                results.append((xor_byte, score, i, guess))
        
    for result in sorted(results, key=lambda k:k[1]):
        print("%0.2f: Line %d XORed with 0x%x (%s): %s" % (result[1], result[2], result[0], chr(result[0]), bytes(result[3])))


if __name__ == "__main__":
    main()