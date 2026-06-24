class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            # Use the absolute value of the current number to get the index.
            # This handles cases where the current number has already been marked negative.
            index = abs(num) - 1

            # If the number at this index is negative, it's a duplicate.
            # The duplicate number is the absolute value of the current number.
            if nums[index] < 0:
                return abs(num)
            
            # Otherwise, mark the number at this index as visited by making it negative.
            nums[index] *= -1

        # The problem guarantees a duplicate, so this part is technically unreachable.
        return -1 