def checkString(str1, str2):
    for i in range(len(str1)):
        if str1[i] < str2[i]:
            return -1
        elif str1[i] > str2[i]:
            return 1
    return 0

str1 = input()
str2 = input()
print(checkString(str1.lower(), str2.lower()))
