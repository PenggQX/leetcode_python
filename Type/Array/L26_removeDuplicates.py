from unittest import TestCase

# 删除有序数组中的重复项 要求O(1)空间复杂度
# 双指针


def removeDuplicates(nums) -> int:
    """
    原地操作，快慢两个索引往后移，直到快针遍历完列表 时间复杂度O(1)
    :param nums:list
    :return: int
    """
    iSlow, iQuick = 0, 0
    for iQuick in range(1, len(nums)):
        if nums[iQuick] != nums[iSlow]:
            iSlow += 1
            # if iSlow == iQuick:
            #     continue
            nums[iSlow], nums[iQuick] = nums[iQuick], nums[iSlow]
        iQuick += 1
    return iSlow + 1


class Test(TestCase):

    def test_1(self):
        print(removeDuplicates([0, 0, 1, 2, 2, 3, 4]))