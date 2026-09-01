class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for number in nums:
            if number not in counts:
                counts[number] = 1
            else:
                return True
        return False
            