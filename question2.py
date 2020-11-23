"""
Exercise 2
Please write a program that can take in a string as input and print out the result by applying the
following string compression algorithm:
● If a character, ch , occurs N(> 1) times in a row, then it will be represented by {ch}{n }. For
example, if the substring is a sequence of 'a' ("aaaa"), it will be represented as "a4".
● If a character, ch , occurs exactly one time in a row, then it will be simply represented as ch . For
example, if the substring is "a", then it will be represented as "a".
The input string will contain at least one character, and will be lowercase English characters ( a-z ) only.
Examples:
Input -> Output
● abcaaabbb -> abca3b3
● abcd -> abcd
● aaabaaaaccaaaaba -> a3ba4c2a4ba
"""

import argparse


class StringCompression:
    @staticmethod
    def compress( s):
        if len(s) < 1:
            return -1

        result = ""
        count = 1
        prev = s[0]

        for i in range(1, len(s)):
            curr = s[i]
            if prev == curr:
                count += 1

            else:
                result += prev
                if count != 1:
                    result += str(count)
                prev = curr
                count = 1

        result += prev
        if count != 1:
            result += str(count)

        if len(s) < len(result):
            return s
        else:
            return result


if __name__ == '__main__':
    assert StringCompression.compress("abcaaabbb") == "abca3b3", "This Should Pass"
    assert StringCompression.compress("aaabaaaaccaaaaba") == "a3ba4c2a4ba", "This Should Pass"
    assert StringCompression.compress("abcd") == "abcd", "This Should Pass"

    parser = argparse.ArgumentParser(description='Enter a directory path string')
    # parser.add_argument('path', metavar='p', type=str, help='relative or full directory path')
    parser.add_argument('--path', dest='path')
    while True:
        input_string = input("Enter a string for compression: (Press Enter to exit)  \n")
        if input_string == "" or input_string == "\r" or input_string == '\n':
            break

        print("Answer: ", StringCompression.compress(input_string))


