import argparse

__author__ = 'Shawn Roche'


class goldbachChecker:
    def __init__(self, num):
        self.num = num
        self.primes = []
        self.goldbach_addends = []
        self.main()

    def get_primes(self):
        """
        Generate a list of all the prime numbers in the range specified by "number"
        :return: list of prime numbers
        """
        for prime in range(2, self.num + 1):
            # Test if the number can be divided by anything other than 1 and itself with no remainder.
            # If it can, break the loop and move to the next number in the range.
            for i in range(2, prime):
                if prime % i == 0:
                    break
            else:
                self.primes.append(prime),

    def test_for_goldbach(self):
        """
        Find the pairs of primes, if any, that can add up to the number provided
        :return:
        """
        # loop through each number in the list of primes and see if they add up to the goldbach_number under test
        # If a pair of primes is found, append it to the goldbach_addends list
        for x in self.primes:
            for y in self.primes:
                # This check is to save processing and time. If y < x it means we already tried this combination of
                # x and y and there's no need to recheck
                if y < x:
                    continue
                if x + y == self.num:
                    self.goldbach_addends.append((x, y))

    def main(self):
        """
        Use the other functions to actually run the test and return a list of goldbach addends
        :return:
        """
        # If a number wasn't passed as a runtime param, prompt the user for one
        even_integer = False
        while not even_integer:
            if not self.num:
                self.num = input('\nWhat even integer would you like to test? > ')
            try:
                # Check to make sure that the number is an even integer larger than 4
                self.num = int(self.num)
                if self.num % 2 != 0:
                    print("\"{}\" is not even. Goldbach's conjecture can only be applied to even integers.".format(
                        self.num))
                    self.num = False
                elif self.num < 4:
                    print("While it is an even integer, \"{}\" is not really a Goldbach number.".format(self.num))
                    print("Try again with a number larger than 4")
                    self.num = False
                else:
                    even_integer = True

            except ValueError:
                print("\"{}\" is not an integer. Goldbach's conjecture can only be applied to even integers".format(
                    self.num))
                self.num = False

        self.get_primes()
        self.test_for_goldbach()

        if self.goldbach_addends:
            print('There are {} pairs of primes that add up to {}:'.format(len(self.goldbach_addends), self.num))
            for pair in self.goldbach_addends:
                print('  {}, {}'.format(pair[0], pair[1]))
        else:
            # Arrogantly assume you've proven a famous math problem wrong, and not that your program had a bug in it
            print('\"{}\" does not seem to be a Goldbach number despite being an int and even.'.format(self.num))
            print('Maybe we should write a paper about it and win a Nobel?')


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--num', help="The number you would like to check goldbach's conjecture with",
                        default=False)

    return parser.parse_args()

if __name__ == '__main__':
    number = get_args().num
    goldbach_checker = goldbachChecker(number)