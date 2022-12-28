def swap_case(s):
    #easy solution
    #return s.swapcase()

    # this one works too
    new_s = ''
    for ltr in s:
        if ltr == (ltr.upper()):
            new_s += ltr.lower()
        else:
            new_s += ltr.upper()
    return new_s

if __name__ == '__main__':
