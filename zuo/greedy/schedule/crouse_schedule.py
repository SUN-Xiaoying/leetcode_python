# https://leetcode.com/problems/course-schedule/description/
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        head = ListNode(-1)
        for pre in prerequisites:




