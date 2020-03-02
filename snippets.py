import sys
import base64
import binascii
import char_freq


def hex2base64(h):
    return base64.b64encode(bytearray.fromhex(h))


def xor_bin_equal_len(binary_left, binary_right):
    assert len(binary_left) == len(binary_right)
    result = bytearray(binary_left)
    for i in range(len(result)):
        result[i] = binary_left[i] ^ binary_right[i]
    return result


def xor_hex_equal_len(hex_left, hex_right):
    assert len(hex_left) == len(hex_right)
    return xor_bin_equal_len(bytearray.fromhex(hex_left), 
        bytearray.fromhex(hex_right))


def xor_bin_single_char(binary, character):
    result = bytearray(binary)
    for i in range(len(binary)):
        result[i] ^= character
    return result


def main():
    assert len(sys.argv) == 2
    encrypted = bytearray.fromhex(sys.argv[1])

    all_decrypted = []

    for xor_byte in range(256):
        current_encrypted = xor_bin_single_char(encrypted,
            xor_byte)
        score = char_freq.score_letter_frequency(current_encrypted)
        all_decrypted.append((current_encrypted, score))
    
    all_decrypted.sort(key=lambda k: k[1])

    for (decrypted, score) in all_decrypted:
        print("%0.3f: %s" % (score, bytes(decrypted)))


if __name__ == "__main__":
    main()