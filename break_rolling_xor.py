import hamming
import char_freq
import sys
import base64

# size limits from the exercise
MIN_KEY_LENGTH = 2
MAX_KEY_LENGTH = 40


def possible_key_sizes(encoded_content):
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
    assert len(sys.argv) in (2,3)
    with open(sys.argv[1], 'r') as f:
        encoded_content = bytearray(base64.b64decode(f.read().replace('\r\n', '').replace(' ', '')))
    
    if len(sys.argv) == 2:
        # analyze likelihood of key sizes
        possible_key_sizes(encoded_content)
    else:
        # break rolling XOR given a key size
        key_size = int(sys.argv[2])
        raise NotImplementedError()


if __name__ == "__main__":
    main()