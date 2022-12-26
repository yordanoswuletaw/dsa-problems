def swap_case(s):
    new_s = ''
    for ltr in s:
        if ltr == (ltr.upper()):
            new_s += ltr.lower()
        else:
            new_s += ltr.upper()
    return new_s

if __name__ == '__main__':
