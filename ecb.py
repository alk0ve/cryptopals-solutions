# using pycrypto, built with Visual Studio Build Tools 19, 
# and using this: https://www.dariawan.com/tutorials/python/python-3-install-pycrypto-windows/
from Crypto.Cipher import AES
import sys
import base64


def main():
    assert len(sys.argv) == 2
    with open(sys.argv[1], 'r') as f:
        encrypted = base64.b64decode(f.read().replace('\n',''))
    
    aes_ecb = AES.new("YELLOW SUBMARINE", AES.MODE_ECB)
    print(aes_ecb.decrypt(encrypted))

if __name__ == "__main__":
    main()

