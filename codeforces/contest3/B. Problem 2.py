string1 = input()
string2 = input()

def compare(string1, string2):
    for i in range(len(string1)):
        if string1[i] > string2[i]:
            return 1
        if string1[i] < string2[i]:
            return - 1
    return 0

print(compare(string1.lower(), string2.lower()))
