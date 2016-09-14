__author__ = 'Shawn Roche'
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--msg', help='the text to encode or decode')
    parser.add_argument('--decode', help='Flag to control decoding vs encoding', action='store_true', default=False)
    parser.add_argument('--cipher', help='number of ordinals to step in the cipher', default=15)

    return parser.parse_args()


def cipher(msg, cipher_num, decodify=False):
    """
    Take a given message, cipher, and mode and transform the message. The default action will be to encode the message
    to obfuscate it's meaning, but you can also decode an obfuscated message provided you know it's cipher.

    :param msg: The message that you would like to either encode or decode
    :param cipher_num: The number of jumps to use in the cipher
    :param decodify: a boolean to control if the function encodes or decodes the message you pass
    :return:
    """
    # Create the base variables. ciphered_code will be the end result encoded/decoded string.
    # operators is the operations to perform for the specifed mode
    ciphered_code = ''
    operators = ['-', '>', '+']

    # If decoding, invert the operators values
    if decodify:
        operators = ['+', '<', '-']

    # loop through each letter or digit in the message and change the values
    for i in msg:
        # Get the ordinal value of the ciphered value, adding or subtracting the cipher_num depending on the mode
        ordinal = eval('{}{}{}'.format(ord(i), operators[2], cipher_num))

        # For each data type check if the new ordinal is outside the range of that data type and if so, loop it back
        # around to the beginning of the range for that data type
        if i.isupper() and not 65 <= ordinal <= 91:
            ordinal = eval('{}{}25'.format(ordinal, operators[0]))
        elif i.islower() and not 97 <= ordinal <= 122:
            ordinal = eval('{}{}25'.format(ordinal, operators[0]))
        elif i.isdigit() and not 48 <= ordinal <= 57:
            ordinal = eval('{}{}9'.format(ordinal, operators[0]))

        # Add the transformed letter or digit to the ciphered_code var which will contain the full transformed string
        ciphered_code += chr(ordinal)
    print('Ciphered message: {}'.format(ciphered_code))


if __name__ == '__main__':
    args = get_args()
    if args.decode:
        cipher(args.msg, args.cipher, decodify=True)
    else:
        cipher(args.msg, args.cipher)
