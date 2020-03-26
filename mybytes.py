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


def xor_bin_rolling_key(binary, key):
    result = bytearray(binary)

    for i in range(len(binary)):
        result[i] = binary[i] ^ key[i % len(key)]

    return result
