__author__ = 'Shawn Roche'
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--msg', help='the text to encode or decode')
    parser.add_argument('--decode', help='Flag to control decoding vs encoding', action='store_true', default=False)
    parser.add_argument('--cipher', help='number of steps in the cipher', default=15)

    return parser.parse_args()


def cipher_ordinally(msg, cipher_num, decode=False):
    """
    Take a given message, cipher, and mode and transform the message. The default action will be to encode the message
    to obfuscate it's meaning, but you can also decode an obfuscated message provided you know it's cipher.

    :param msg: The message that you would like to either encode or decode
    :param cipher_num: The number of jumps to use in the cipher
    :param decode: a boolean to control if the function encodes or decodes the message you pass
    :return:
    """
    # Create the base variables. ciphered_code will be the end result encoded/decoded string.
    # operators is the operations to perform for the specifed mode
    ciphered_code = ''
    operators = ['-', '>', '+']

    # If decoding, invert the operators values
    if decode:
        operators = ['+', '<', '-']

    # loop through each letter or digit in the message and change the values
    for char in msg:
        # Get the ordinal value of the ciphered value, adding or subtracting the cipher_num depending on the mode
        ordinal = eval('{}{}{}'.format(ord(char), operators[2], cipher_num))

        # For each data type check if the new ordinal is outside the range of that data type and if so, loop it back
        # around to the beginning of the range for that data type
        if char.isupper() and not 65 <= ordinal <= 91:
            ordinal = eval('{}{}25'.format(ordinal, operators[0]))
        elif char.islower() and not 97 <= ordinal <= 122:
            ordinal = eval('{}{}25'.format(ordinal, operators[0]))
        elif char.isdigit() and not 48 <= ordinal <= 57:
            ordinal = eval('{}{}9'.format(ordinal, operators[0]))

        # Add the transformed letter or digit to the ciphered_code var which will contain the full transformed string
        ciphered_code += chr(ordinal)
    print('Ciphered message: {}'.format(ciphered_code))


def cipher_by_list(msg, cipher_num, decode=False):
    """
    Take a given message, cipher, and mode and transform the message. The default action will be to encode the message
    to obfuscate it's meaning, but you can also decode an obfuscated message provided you know it's cipher.

    :param msg: The message that you would like to either encode or decode
    :param cipher_num: The number of jumps to use in the cipher
    :param decode: a boolean to control if the function encodes or decodes the message you pass
    :return:
    """
    # Create the base variables. ciphered_code will be the end result encoded/decoded string.
    # alphanum_list is the list containing all the cipherable characters
    alphanum_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                     'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '0', '1', '2', '3', '4', '5', '6',
                     '7', '8', '9']
    ciphered_code = ''

    # Iterate through the passed message transforming every character
    for char in msg:
        # Catch if the user passed a character we weren't expecting and gracefully quit
        try:
            pos = alphanum_list.index(char)
        except ValueError:
            print('ERROR. This program can only cipher or decipher alphanumeric characters and spaces.')
            print('Remove any special or unicode characters and try again')
            exit('Quitting...')

        # Get the ciphered character by adding/subtracting the cipher number from the current index (pos)
        if decode:
            pos = pos - cipher_num
        else:
            pos = pos + cipher_num
            if pos >= len(alphanum_list):
                # if the index is greater than the len of the list, subtract the list len() to loop back around to the
                # beginning of the list
                pos -= len(alphanum_list)

        # Store the characters value to ciphered_code to be printed later
        ciphered_code += alphanum_list[pos]

    print('Ciphered message: {}'.format(ciphered_code))


if __name__ == '__main__':
    args = get_args()
    if args.decode:
        cipher_by_list(args.msg, int(args.cipher), decode=True)
    else:
        cipher_by_list(args.msg, int(args.cipher))
