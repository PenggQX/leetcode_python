from unittest import TestCase

# 四数之和
# 对撞指针


def fourSum(nums, target):
    """
    两遍for循环加对撞指针 时间复杂度O(n**3)
    :param nums:
    :param target:
    :return:
    """
    if len(nums) < 4:
        return []
    nums.sort()     # 先排序
    iLen = len(nums)
    resSet = set()  # 去重
    for iA in range(0, iLen - 3):
        if sum([nums[i] for i in range(iA, iA + 4)]) > target:  # 剪枝操作
            break
        if sum([nums[i] for i in (iA, -1, -2, -3)]) < target:
            continue
        for iB in range(iA + 1, iLen - 2):  # 双重for循环
            iLow, iHigh = iB + 1, iLen - 1
            while iLow < iHigh:
                t = tuple((nums[i] for i in (iA, iB, iLow, iHigh)))
                fSum = sum(t)
                if fSum == target:
                    resSet.add(t)
                    iLow += 1
                    iHigh -= 1
                elif fSum > target:
                    iHigh -= 1
                else:
                    iLow += 1
    return [list(tRes) for tRes in resSet]


class Test(TestCase):

    def test_1(self):
        self.assertEqual(fourSum([1, 0, -1, 0, -2, 2], 0), [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])

    def test_2(self):
        self.assertEqual(fourSum([2, 2, 2, 2, 2], 8), [[2, 2, 2, 2]])

    def test_3(self):
        self.assertEqual(fourSum([0, 0, 0, 0], 0), [[0, 0, 0, 0]])