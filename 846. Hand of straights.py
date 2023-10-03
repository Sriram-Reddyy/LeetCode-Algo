"""
846. Hand of Straights - GOOGLE
https://leetcode.com/problems/hand-of-straights/description/
Solved
Medium
Topics
Companies
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.
"""

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for x in hand:
            d1[x]+=1
        hand.sort()
        i, n = 0, len(hand)

        while(i<n):
            req = hand[i]
            count = groupSize
            while(i<n and count>0):
                if(d1[req]):
                    d1[req]-=1
                else:
                    return False
                d2[req]+=1 #Generic to remove elements in future
                if(req == hand[i]):
                    while(i<n and d2[hand[i]]):
                        d2[hand[i]]-=1
                        i+=1
                req = req + 1
                count-=1
        if(count):
            return False
        return True