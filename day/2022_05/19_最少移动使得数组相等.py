class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()

        iRet = 0
        iLeft, iRight = 0, len(nums) - 1
        while iLeft < iRight:
            if nums[iLeft] == nums[iRight]:
                break

            iRet += (nums[iRight] - nums[iLeft])
            iLeft += 1
            iRight -= 1

        return iRet