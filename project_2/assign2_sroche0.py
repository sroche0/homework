import argparse

__author__ = 'Shawn Roche'


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--num', help="The number you would like to check goldbach's conjecture with", default=False)

    return parser.parse_args()


def get_primes(number):
    """
    Generate a list of all the prime numbers in the range specified by "number"
    :param number: The range to generate primes for
    :return: list of prime numbers
    """
    primes = []
    for prime in range(2, number + 1):
        # Test if the number can be divided by anything other than 1 and itself with no remainder.
        # If it can, break the loop and move to the next number in the range.
        for i in range(2, prime):
            if prime % i == 0:
                break
        else:
            primes.append(prime),
    return primes


def test_for_goldbach(goldbach_num, prime_list):
    """
    Find the pairs of primes, if any, that can add up to the number provided
    :param goldbach_num: the number we are trying to test as a Goldbach Number
    :param prime_list: a list of all prime numbers that are smaller than param number
    :return:
    """
    goldbach_addends = []
    # loop through each number in the list of primes and see if they add up to the goldbach_number under test
    # If a pair of primes is found, append it to the goldbach_addends list
    for x in prime_list:
        for y in prime_list:
            # This check is to save processing and time. If y < x it means we already tried this combination of x and y
            # and theres no need to recheck
            if y < x:
                continue
            if x + y == goldbach_num:
                goldbach_addends.append((x, y))

    return goldbach_addends


def main():
    """
    Use the other functions to actually run the test and return a list of goldbach addends
    :return:
    """

    num = get_args().num
    # If a number wasn't passed as a runtime param, prompt the user for one
    even_integer = False
    while not even_integer:
        if not num:
            num = input('\nWhat even number would you like to test? > ')
        try:
            # Check to make sure that the number is an even integer larger than 4
            num = int(num)
            if num % 2 != 0:
                print("\"{}\" is not even. Goldbach's conjecture can only be applied to even integers.".format(num))
                num = False
            elif num < 4:
                print("While it is an even integer, \"{}\" is not really a Goldbach number.".format(num))
                print("Try again with a number larger than 4")
                num = False
            else:
                even_integer = True

        except ValueError:
            print("\"{}\" is not an integer. Goldbach's conjecture can only be applied to even integers".format(num))
            num = False

    prime_numbers = get_primes(num)
    goldbachs = test_for_goldbach(num, prime_numbers)

    if goldbachs:
        print('There are {} pairs of primes that add up to {}:'.format(len(goldbachs), num))
        for pair in goldbachs:
            print('  {}'.format(pair))
    else:
        # Arrogantly assume you've proven a famous math problem wrong, and not that your program had a bug in it
        print('\"{}\" does not seem to be a Goldbach number despite being an int and even.'.format(num))
        print('Maybe we should write a paper about it and win a Nobel?')


if __name__ == '__main__':
    main()
