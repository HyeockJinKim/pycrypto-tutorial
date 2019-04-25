import getpass

from aes.ctr import encrypt_message, decrypt_message
from utils.io import get_filename_of_iv, get_filename_of_enc, get_filename_of_dec, read_file_all, read_binary_file_all


def encrypt(filename):
    """
    Encrypt string
    :param string:
    :return:
    """
    string = read_file_all(filename)
    key = getpass.getpass('Please input password: ')

    iv, enc = encrypt_message(key, string)
    print('Encrypted message : ', enc)
    with open(get_filename_of_iv(filename), 'wb') as f:
        f.write(iv)
    with open(get_filename_of_enc(filename), 'wb') as f:
        f.write(enc)


def decrypt(filename):
    """
    Decrypt cipher text
    :return:
    """
    iv = read_binary_file_all(get_filename_of_iv(filename))
    enc = read_binary_file_all(get_filename_of_enc(filename))

    key = getpass.getpass('Please input password: ')

    dec = decrypt_message(key, iv, enc)
    print('Decrypted message : ', dec)
    with open(get_filename_of_dec(filename), 'w') as f:
        f.write(dec)
