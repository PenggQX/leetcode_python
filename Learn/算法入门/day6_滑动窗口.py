# L3: 无重复字符的最长子串
# 优化 用散列表存值
def lengthOfLongestSubstring(sSource):
    if len(sSource) <= 1:
        return len(sSource)

    hmap = {}
    iLow = 0
    iMax = 1
    for i in range(0, len(sSource)):
        if hmap.get(sSource[i], -1) < iLow:
            iMax = max(iMax, i - iLow + 1)
            hmap[sSource[i]] = i
        else:
            iLow = hmap.get(sSource[i]) + 1
            hmap[sSource[i]] = i
    return iMax


if __name__ == '__main__':
    print(lengthOfLongestSubstring("aab"))