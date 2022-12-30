str1 = input()
str2 = input()
def compare(str1, str2):
    for i in range(len(str1)):
        if str1[i].upper() > str2[i].upper():
            return 1
        elif str1[i].upper() < str2[i].upper():
            return -1
    return 0
print(compare(str1, str2))
