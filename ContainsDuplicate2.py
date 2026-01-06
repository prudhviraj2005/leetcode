from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """Return True if there are two distinct indices i and j such that nums[i] == nums[j]
        and abs(i - j) <= k.
        Efficient O(n) solution using a dictionary to track the last index seen for each value.
        """
        last_index = {}
        for i, val in enumerate(nums):
            if val in last_index and i - last_index[val] <= k:
                return True
            last_index[val] = i
        return False


# Example quick tests (these won't run on LeetCode but are useful for local testing)
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate([1,2,3,1], 3))  # True
    print(sol.containsNearbyDuplicate([1,0,1,1], 1))  # True
    print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2))  # False
