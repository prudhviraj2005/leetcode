"""
You are given an array of distinct integers arr.

Your task is to find all pairs of elements with the minimum absolute difference
between any two elements in the array.

Return the result as a list of pairs [a, b] such that:
- a < b
- b - a is the minimum possible absolute difference

The result should be returned in ascending order.
"""
arr = [4,2,1,3]
sorted = [1,2,3,4]

Differences:
2-1 = 1
3-2 = 1
4-3 = 1

Answer = [[1,2],[2,3],[3,4]]

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Step 1: Sort the array
        arr.sort()

        # Step 2: Find the minimum absolute difference
        min_diff = float('inf')
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i - 1])

        # Step 3: Collect all pairs with min_diff
        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])

        return result

