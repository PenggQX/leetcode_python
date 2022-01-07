from unittest import TestCase

# 移除元素 要求O(1)空间复杂度
# 双指针 L26


def removeElement(nums, val: int) -> int:
    """
    双指针，将val和非val数交换位置
    :param nums:
    :param val:
    :return:
    """
    iSlow, iQuick = 0, 0
    for iQuick in range(0, len(nums)):
        if nums[iQuick] != val:
            # nums[iSlow], nums[iQuick] = nums[iQuick], nums[iSlow]
            nums[iSlow] = nums[iQuick]
            iSlow += 1
        iQuick += 1
    return iSlow + 1