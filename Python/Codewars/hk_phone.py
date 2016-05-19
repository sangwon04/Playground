#!/usr/bin/python`
#Valid HK Phone Number

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
