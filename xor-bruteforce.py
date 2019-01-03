#!/usr/bin/env python3
from itertools import cycle
import binascii
"""
    File name: xor-bruteforce.py
    Author: Rodney Olav C. Melby
    Date created: 3/1/2019
    Date last modified: 3/1/2019
    Python Version: 3.7
"""
####
# Program to brute force XOR with a single character or number as the key used for encryption and UTF-8 encoding,
# Created to solve CTF, decrypted CTF encrypted string, Requires user hard coded key e.g. 'R'
####


def xor_strings(message, key):
    """xor two strings together"""
    encryption: str = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(message, cycle(key)))
    '''print("Encrypted Message", encryption) # XOR twice gets the original'''
    return encryption


# Brute force string using XOR
def bruteforce(secret):
    ''' brute force provided string using XOR and given key R '''
    encrypted = binascii.unhexlify(secret)# convert secret from hex to binary, binary to asscii
    ''' xor every possible char 1-256 '''
    for xor_key in range(256):
        ''' for each xor match in the 'encoded' hex string '''
        decrypted = ''.join(chr(b ^ xor_key) for b in encrypted)
        ''' print if hex character is printable '''
        if decrypted.isprintable():
            print(xor_key, decrypted)


# Set and print clear text message
cleartext = 'Single Byte XOR encryption and decryption example python 3.7'
print('\nCleartext Message:', cleartext)

# Set and print encryption_key
encryption_key = "R"
print('Encryption Key:', encryption_key)

# XOR once to encrypt and print result
ciphertext = xor_strings(cleartext, encryption_key)
print('Encrypted Message:', ciphertext)
print('Encryption Success.')

# XOR once again to decrypt and print result
decryptedtext = xor_strings(ciphertext, encryption_key)
print('\nDecrypted Message:', decryptedtext)
print('Decryption Success.\n')

# Brute force all single characters, 0-9, a-z, and A-Z
print("Brute Force ASSCII chars and print valid results:\n")

# encode ciphertext with utf-8 (byte stream)
cipher_as_bytes = str.encode(ciphertext, 'utf-8')

# convert byte stream from hex to binary, and then binary to asscii
plaintexttohex: bytes = binascii.hexlify(cipher_as_bytes)

# brute force string using XOR with key 'R'
bruteforce(plaintexttohex)

# see iteration 82 for the original message decrypted

# TODO: Test every char and number against given key automatically.
# TODO: Strip all results containing non english characters or special characters - see: english language heuristics.
# TODO: Add user input and/or program command lines args to grab brute force string and/or key string.
# TODO; Allow for more than one character and supply a common word list - e.g. 4 characters as key, integers only.(pins)
