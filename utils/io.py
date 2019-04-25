from pathlib import Path


def read_file_all(file_name):
    """
    Read All string of file
    :param file_name:
    :return:
    """
    with open(file_name, 'r') as f:
        string = ''.join(f.readlines())
    return string


def read_binary_file_all(file_name):
    """
    Read All byte of file
    :param file_name:
    :return:
    """
    return Path(file_name).read_bytes()


def get_filename_of_iv(file_name):
    """
    Get filename of initial vector
    :param file_name: filename of plain text
    :return: filename of initial vector
    """
    return file_name.split('.')[0]+'.iv'


def get_filename_of_enc(file_name):
    """
    Get filename of Encrypted message
    :param file_name: filename of plain text
    :return: filename of encrypted message
    """
    return file_name.split('.')[0]+'.enc'


def get_filename_of_dec(file_name):
    """
    Get filename of Decrypted message
    :param file_name: filename of plain text
    :return: filename of decrypted message
    """
    return file_name.split('.')[0]+'.dec'
