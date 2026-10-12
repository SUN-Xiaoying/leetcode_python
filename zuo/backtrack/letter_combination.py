from typing import List



class Solution:
    # Your runtime beats 100.00 % of python3 submissions.
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "": return []
        digits_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result=[]

        def backtrack(index: int, path: str):
            if index == len(digits):
                return result.append(path)

            for char in digits_to_char[digits[index]]:
                backtrack(index+1, path+char)

        backtrack(0, "")
        return result

    # Your runtime beats 100.00 % of python3 submissions.
    def letterCombinations_mine(self, digits: str) -> List[str]:
        if digits == "": return []
        all_lists = []
        digits_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(lists):
            if not lists:
                return [[]]

            first = lists[0]
            result = []
            rest_combination = backtrack(lists[1:])

            for item in first:
                for combination in rest_combination:
                    result.append([item] + combination)

            return result

        for digit in digits:
            all_lists.append(list(digits_to_char[digit]))

        combinations = backtrack(all_lists)

        return ["".join(combo) for combo in combinations]

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))