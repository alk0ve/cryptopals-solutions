import sys
import base64
import binascii


def hex2base64(h):
    return base64.b64encode(bytearray.fromhex(h))


def xor_bin_equal_len(b1, b2):
    assert len(b1) == len(b2)
    result = bytearray(b1)
    for i in range(len(result)):
        result[i] = b1[i] ^ b2[i]
    return result


def xor_hex_equal_len(h1, h2):
    assert len(h1) == len(h2)
    return xor_bin_equal_len(bytearray.fromhex(h1),
        bytearray.fromhex(h2))


def main():
    assert len(sys.argv) == 3
    print(binascii.hexlify(xor_hex_equal_len(sys.argv[1],
        sys.argv[2])))


if __name__ == "__main__":
    main()