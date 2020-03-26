# using pycrypto, built with Visual Studio Build Tools 19, 
# and using this: https://www.dariawan.com/tutorials/python/python-3-install-pycrypto-windows/
from Crypto.Cipher import AES
import sys
import base64
import binascii

AES_BLOCK_SIZE = 16

def main():
    assert len(sys.argv) == 2
    with open(sys.argv[1], 'r') as f:
        encrypted_lines = [binascii.unhexlify(line) for line in f.read().split()]
    for line_num, line in enumerate(encrypted_lines):
        encrypted_blocks = set()
        for offset in range(0, len(line), AES_BLOCK_SIZE):
            block = line[offset: offset + AES_BLOCK_SIZE]
            if block in encrypted_blocks:
                # bingo
                print("Found a repeat in line %d: %s" % (line_num, binascii.hexlify(block)))
                return
            encrypted_blocks.add(block)
            

if __name__ == "__main__":
    main()

