import os
import sys
from time import time
import hashlib
from hmac import HMAC as hmac
import base64
from base64 import b32decode
from struct import pack, unpack
import qrcode
import webbrowser

current_unix_time = int(time())

def generateTOTP(key, time, crypto = hashlib.sha512):
    secret = b32decode(key.encode('ascii'))
    bytetime= pack(">q", time) #packing an integer
    #https://docs.python.org/2/library/struct.html
    h = hmac(secret, bytetime, crypto).digest() #Security up in here.
    offset = h[-1] & 0x0F
    shreyhash = h[offset:offset+4] #It was original called short hash
    # I decided to be funny and call it shreyhash
    # Cause I'm short.
    # Laugh at my joke.
    QCode = unpack('>L', shreyhash)[0]
    QCode &= 0x7FFFFFFF
    QCode %= 1000000
    QCode = '{0:06d}'.format(QCode)
    return QCode

def generateQR(text_string):
    img = qrcode.make(text_string)
    img.show()


'''
class HotpTest(unittest.TestCase):
    """
    a very simple test case for HOTP.
    Based on test vectors from http://www.ietf.org/rfc/rfc4226.txt
                          and  http://tools.ietf.org/html/rfc6238
    """
    def setUp(self):
        self.key_string = b'12345678901234567890'
        self.key_string_256 = b'12345678901234567890123456789012'
        self.key_string_512 = b'123456789012345678901234567890' + \
                              b'1234567890123456789012345678901234'

    def test_hotp_vectors(self):
        hotp_result_vector = ['755224', '287082', '359152',
                              '969429', '338314', '254676',
                              '287922', '162583', '399871',
                              '520489']
        for i, r in enumerate(hotp_result_vector):
            self.assertEqual(HOTP(self.key_string, i), r)

    def test_totp_vectors_rfc6238(self):
        totp_result_vector = [
            (self.key_string, 59, '94287082', hashlib.sha1),
            (self.key_string_256, 59, '46119246', hashlib.sha256),
            (self.key_string_512, 59, '90693936', hashlib.sha512),
            (self.key_string, 1111111109, '07081804', hashlib.sha1),
            (self.key_string_256, 1111111109, '68084774', hashlib.sha256),
            (self.key_string_512, 1111111109, '25091201', hashlib.sha512),
            (self.key_string, 1111111111, '14050471', hashlib.sha1),
            (self.key_string_256, 1111111111, '67062674', hashlib.sha256),
            (self.key_string_512, 1111111111, '99943326', hashlib.sha512),
            (self.key_string, 1234567890, '89005924', hashlib.sha1),
            (self.key_string_256, 1234567890, '91819424', hashlib.sha256),
            (self.key_string_512, 1234567890, '93441116', hashlib.sha512),
        ]
        for (key, clock, result, digestmod) in totp_result_vector:
            self.assertEqual(result, TOTP(key,
            digits=8,
            window=30,
            clock=clock,
            digestmod=digestmod))
            
        encoded_str = base64.b32encode(result)
        print("Below is the secret encoded base 32 string")
        print(encoded_str)
        print("Below is also the unencoded value")
        print(result)
'''


def main():
    print("Welcome to assignment 3!")
    key = "SHREYANS"

    TOTPinput = "otpauth://totp/CS370:khuntets@oregonstate.edu?secret=" + key + "&issuer=ShreyansAssignment3"

    cur_time = int(time() /30) # To fulfill 30 second requirement.

    if len(sys.argv) == 2:
        if sys.argv[1] == "--generate-qr":
            generateQR(TOTPinput)
        elif sys.argv[1] == "--get-otp":
            print(generateTOTP(key, cur_time))
        else:
            print("Thank you for using the program and have a great summer!")

    else:
        print("Thank you for using the program and have a great summer!")

if  __name__ =='__main__':
    main()