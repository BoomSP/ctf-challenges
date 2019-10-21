import base64
import sys
from Crypto.Cipher import AES

text = sys.argv[1]
key2 = "seccon2019"

# get base64 out
b64_dec = base64.b64decode(text)
ord
cipher = AES.new(key2 + chr(0x00) * (16 - (len(key2) % 16)), AES.MODE_ECB)
p = 8

enc1 = cipher.decrypt(b64_dec)
# print(enc1)
# print(type(enc1))

for i in range(len(enc1)):
    print(ord(enc1[i]))
    


# flag: length = 32 to 47 characters
# FyRyZNBO2MG6ncd3hEkC/yeYKUseI/CxYoZiIeV2fe/Jmtwx+WbWmU1gtMX9m905
# 'jff~|Ox9'34G9#g52F?489>B%|)173~)%8.'jff~|Q

# a
# d4I2tOp/QoBIwNrVKVXvOg==

# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# print(len("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))