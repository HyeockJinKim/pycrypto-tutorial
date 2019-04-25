from utils.api import encrypt, decrypt
from sys import argv


def parse_arg():
    """
    Parse arguments
    :return: None
    """
    print(argv)
    filename = None
    func = encrypt
    for index in range(1, len(argv)):
        arg = argv[index]
        if arg == '--enc':
            func = encrypt
        elif arg == '--dec':
            func = decrypt
        else:
            filename = arg
    func(filename)
