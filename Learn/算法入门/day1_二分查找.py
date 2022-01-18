# L704_二分查找

def search(nums: list, target: int) -> int:
    iLow, iHigh = 0, len(nums) - 1
    while iLow <= iHigh:
        iMid = (iHigh - iLow) // 2 + iLow  # 防止溢出
        # print(iMid, iHigh, iLow)
        if nums[iMid] == target:
            return iMid
        if nums[iMid] < target:
            iLow = iMid + 1
        else:
            iHigh = iMid - 1
    return -1


# 278 第一个错误的版本
def firstBadVersion(n):
    iLow, iHigh = 1, n

    def isBadVersion(iVer):
        return iVer >= max(n-4, 1)

    # 注意这里的<= 和 26行 的 = iMid 或者iMid-1的区别
    while iLow < iHigh:
        iMid = iLow + (iHigh - iLow) // 2
        if isBadVersion(iMid):
            iHigh = iMid
        else:
            iLow = iMid + 1
    return iHigh


# L35 搜索插入位置 右边减小要谨慎(对应43行不要减一)
def searchInsert(nums: list, target: int) -> int:
    # 注意这里没有减一
    iLow, iHigh = 0, len(nums)
    while iLow < iHigh:
        iMid = iLow + (iHigh - iLow) // 2
        if nums[iMid] == target:
            return iMid
        elif nums[iMid] > target:
            iHigh = iMid
        else:
            iLow = iMid + 1
    return iHigh


if __name__ == '__main__':
    print(search([-1, 0, 3, 5, 9, 12], 13))
    print(firstBadVersion(10))
    print(searchInsert([1, 3, 5, 6], 7))
