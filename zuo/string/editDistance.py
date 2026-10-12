# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        num_deletion = max(0, len1-len2)
        num_insertion = max(0, len2-len1)
        # substring_lengths
        idex2 = len2 - 1
        idex1 = len1 - 1
        stack = []
        mapping = {}
        while idex1 >= 0 and idex2 >= 0:
            if word1[idex1] == word2[idex2]:
                stack.append(word2[idex2]) # what if they only have match in the middle? The idex2 will never move
                idex2 -= 1
            else:
                stack.clear()
            mapping[idex1] = len(stack)
            idex1 -= 1
                
            
            
