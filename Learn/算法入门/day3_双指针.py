# L283 移动零
def moveZeroes(nums: list) -> None:
    iZero = -1
    for index in range(0, len(nums)):
        v = nums[index]
        if v != 0 and iZero != -1:
            nums[index], nums[iZero] = nums[iZero], nums[index]
            iZero += 1
        if v == 0 and iZero == -1:
            iZero = index
    return nums


# L167 两数之和,输入有序数组
def twoSum(numbers, target):
    iLow, iHigh = 0, len(numbers) - 1
    while iLow < iHigh:
        iSum = numbers[iLow] + numbers[iHigh]
        if iSum == target:
            return [iLow + 1, iHigh + 1]
        if iSum > target:
            iHigh -= 1
        else:
            iLow += 1
    return [0, 0]


if __name__ == '__main__':
    print(moveZeroes([0, 1, 0, 3, 12]))
    print(twoSum([2, 7, 11, 15], 18))