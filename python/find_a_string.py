import re


def count_substring(string, sub_string):
    find = '(?=' + sub_string + ')'

    count = len(re.findall(find, string))
    return count