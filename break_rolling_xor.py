import hamming
import char_freq
import sys
import base64
import binascii
import mybytes

# size limits from the exercise
MIN_KEY_LENGTH = 2
MAX_KEY_LENGTH = 40


def break_single_byte_xor(encrypted, cutoff=char_freq.MAX_DISTANCE):
    results = []
    for xor_byte in range(0x100):
        unxored_guess = mybytes.xor_bin_single_char(encrypted, xor_byte)
        score = char_freq.score_letter_frequency(unxored_guess)
        if score < cutoff:
            results.append((xor_byte, score, unxored_guess))
    
    return sorted(results, key=lambda m: m[1])

def split_transpose(s, block_len):
    transposed = [bytearray() for _ in range(block_len)]

    for i in range(len(s)):
        transposed[i % block_len].append(s[i])

    return transposed


def print_possible_key_sizes(encoded_content):
    assert len(encoded_content) >= MAX_KEY_LENGTH * 4

    size2score = {}
    
    
    for key_size in range(MIN_KEY_LENGTH, MAX_KEY_LENGTH):
        dist1 = hamming.hamming_distance(encoded_content[:key_size],
            encoded_content[key_size: 2*key_size])
        dist2 = hamming.hamming_distance(encoded_content[2*key_size: 3*key_size],
            encoded_content[3*key_size: 4*key_size])
        # average and normalize by dividing by key length
        size2score[key_size] = (dist1 + dist2) / float((2 * key_size))
        
    for key_size, score in sorted(size2score.items(), key=lambda x: x[1]):
        print("%d: %.02f" % (key_size, score))


def main():
    assert len(sys.argv) in (2,3,4,5)
    with open(sys.argv[1], 'r') as f:
        encrypted = bytearray(base64.b64decode(f.read().replace('\n', '')))
    
    if len(sys.argv) == 2:
        # analyze likelihood of key sizes
        print_possible_key_sizes(encrypted)
    elif len(sys.argv) == 3:
        # test a guess of an entire key or a single byte (hex-byte,index,key-size)
        if ',' in sys.argv[2]:
            # test a single byte
            key_char, index, key_size = sys.argv[2].split(',')
            key_char, index, key_size = int(key_char, 16), int(index), int(key_size)
            assert (0 <= key_char < 0x100)

            encrypted_blocks_transposed = split_transpose(encrypted, key_size)
            guess = mybytes.xor_bin_single_char(encrypted_blocks_transposed[index], key_char)
            print(binascii.hexlify(guess))
            print(bytes(guess))
        else:
            key = binascii.unhexlify(sys.argv[2])

            print("For key %s (%s): " % (sys.argv[2], key))
            guess = mybytes.xor_bin_rolling_key(encrypted, key)
            print(binascii.hexlify(guess))
            print(bytes(guess))
    elif len(sys.argv) == 4:
        # break rolling XOR given a key size and score cutoff
        key_size = int(sys.argv[2])
        cutoff = float(sys.argv[3])

        # member n is all the nth bytes of each keysize block
        encrypted_blocks_transposed = split_transpose(encrypted, key_size)
        
        for i, encrypted_block in enumerate(encrypted_blocks_transposed):
            results = break_single_byte_xor(encrypted_block, cutoff)
            print("BYTE %d IN KEY:" % (i))
            for result in results:
                print("\t0x%x (%s): %0.2f" % (result[0], chr(result[0]), result[1]))
                print('\t\t%s' % bytes(result[2]))

if __name__ == "__main__":
    main()