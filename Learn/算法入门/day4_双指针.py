

# L344 反转字符串
def reverseString(s):
    iLow, iHigh = 0, len(s) - 1
    while iLow < iHigh:
        s[iLow], s[iHigh] = s[iHigh], s[iLow]
        iLow += 1
        iHigh -= 1
    return s


# L557 反转字符串中的单词III
def reverseWords(s):
    l = s.split()
    l = [s[::-1] for s in l]
    return " ".join(l)


if __name__ == '__main__':
    print(reverseString(['h', 'e', 'i']))
    print(reverseWords("'hello world's"))