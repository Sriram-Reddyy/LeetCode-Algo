"""
1296. Divide Array in Sets of K Consecutive Numbers - Google : 
https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
Solved
Medium
Topics
Companies
Hint
Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

Return true if it is possible. Otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11]."""
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for x in nums:
            d1[x]+=1
        nums.sort()
        i, n = 0, len(nums)

        while(i<n):
            req = nums[i]
            count = k
            while(i<n and count>0):
                if(d1[req]):
                    d1[req]-=1
                else:
                    return False
                d2[req]+=1 #Generic to remove elements in future
                if(req == nums[i]):
                    while(i<n and d2[nums[i]]):
                        d2[nums[i]]-=1
                        i+=1
                req = req + 1
                count-=1
        if(count):
            return False
        return True