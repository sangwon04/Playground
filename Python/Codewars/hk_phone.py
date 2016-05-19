#!/usr/bin/python
'''
Valid HK Phone Number

Overview
In Hong Kong, a valid phone number has the format xxxx xxxx where x is a decimal digit (0-9). For example:

"1234 5678" // is valid
"2359 1478" // is valid
"85748475" // invalid, as there are no spaces separating the first 4 and last 4 digits
"3857  4756" // invalid; there should be exactly 1 whitespace separating the first 4 and last 4 digits respectively
"sklfjsdklfjsf" // clearly invalid
"1234 5678" // is NOT a valid phone number but CONTAINS a valid phone number
"skldfjs287389274329dklfj84239029043820942904823480924293042904820482409209438dslfdjs9345 8234sdklfjsdkfjskl28394723987jsfss2343242kldjf23423423SDLKFJSLKsdklf" // also contains a valid HK phone number (9345 8234)

Task
Define two functions, isValidHKPhoneNumber and hasValidHKPhoneNumber, that returns whether a given string is a valid HK phone number
and contains a valid HK phone number respectively (i.e. true/false values).
'''
import re

def isValidHKPhoneNumber(number):
    if not number or number[0] == " ":
        return False
    else:
        if number[5] == " ":
            return False
        else:
            number = number.split()
            for x in number:
                if len(x) != 4:
                    return False
                try:
                    int(x)
                except ValueError:
                    return False
            return True

def hasValidHKPhoneNumber(number):
    hkNumRegex = re.compile(r'\d\d\d\d \d\d\d\d')
    match = hkNumRegex.search(number)
    if match:
        return True
    else:
        return False


    num_list = []
    if len(number.split()) < 2:
        return False
    else:
        number = number.split()
        for x in number:
            try:
                int(x)
                num_list.append(x)
            except ValueError:
                continue
        if len(num_list) > 0:
            for numbers in num_list:
                try:
                    int(numbers)
                    if len(numbers) != 4:
                        return False
                except ValueError:
                    return False
            return True
        else:
            return False

def main():
    if isValidHKPhoneNumber("8400 84999"):
        print "True"
    else:
        print "False"

main()
