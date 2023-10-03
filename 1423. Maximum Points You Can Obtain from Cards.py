"""

1423. Maximum Points You Can Obtain from Cards
Solved
Medium
Topics
Companies
Hint
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.

"""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ls = []
        rs = []
        sumi = 0
        nums = cardPoints.copy()
        for x in  nums:
            sumi+=x
            ls.append(sumi)
        sumi = 0
        for x in nums[::-1]:
            sumi+=x
            rs.append(sumi)
        rs = rs[::-1]
        #print(ls,rs)
        n = len(nums)
        i,j = k-1, n
        ans = 0
        while(i>=-1):
            sumi = 0
            sumi+=(ls[i] if i>=0 else 0)
            sumi+=(rs[j] if j<n else 0)
            ans = max(ans,sumi)
            i-=1
            j-=1
        return ans
