# https://leetcode.com/problems/strong-password-checker/
# Youtube: https://www.youtube.com/watch?v=9CxpKVR14ps

class Solution:

    def strongPasswordChecker(self, password: str) -> int:
        length_total = len(password)
        # 1. num_deletion
        num_deletion = max(0, length_total-20)
        # 2. num_insertion
        num_insertion = max(0, 6-length_total)
        # 3. missing_type
        no_digits = True
        no_lowercase = True
        no_uppercase = True
        for ch in password:
            if ch.isupper(): no_uppercase = False
            elif ch.islower(): no_lowercase = False
            elif ch.isdigit(): no_digits = False
        missing_type = no_lowercase + no_digits + no_uppercase
        # 4. repeating substrings
        substring_lengths = self.get_substring_lengths(password)
        # 5. break string with deletion
        self.break_string_with_deletion(num_deletion, substring_lengths)
        # 6. break string with replacement
        num_replacement = sum(length // 3 for length in substring_lengths if length >= 3)

        return num_deletion + max(missing_type, num_insertion, num_replacement)

    def get_substring_lengths(self, s:str) -> list[int]:
        substring_lengths = []
        count = 0
        last_ch = s[0]
        for ch in s:
            if ch == last_ch:
                count+=1
            else:
                substring_lengths.append(count)
                last_ch = ch
                count = 1
        if count != 0: substring_lengths.append(count)
        return substring_lengths

    def break_string_with_deletion(self, num_deletion: int, substring_lengths: list[int]):
        while num_deletion > 0:
            # (1, 15)
            best_tuple_to_delete = min(
                enumerate(substring_lengths), # [2, 15, 6]
                key=lambda pair: pair[1] % 3 if pair[1] >= 3 else float("inf")
            )
            # 1
            best_idx_to_delete = best_tuple_to_delete[0]
            substring_lengths[best_idx_to_delete] -= 1
            num_deletion -= 1

s = Solution()

# print(s.get_substring_lengths("aaabbc"))
# print(s.get_substring_lengths("1111111111"))
# 0
print(s.strongPasswordChecker("1337C0d3"))
# 0
print(s.strongPasswordChecker("aaAA11"))
# 1
print(s.strongPasswordChecker("aaa123"))
# 2
print(s.strongPasswordChecker("aaa111"))
# 3
print(s.strongPasswordChecker("1111111111"))
# 3
print(s.strongPasswordChecker("aA1"))
# 5
print(s.strongPasswordChecker("a"))
# 8
print(s.strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc"))



# def strongPasswordChecker_first_try(self, password: str) -> int:
#     length_int = len(password)
#     # For "aaaaa", the minmum steps are 2, not 1
#
#     steps = 0
#     stack=[]
#     no_digits = True
#     no_lowercase = True
#     no_uppercase = True
#
#     for ch in password:
#         if ch.isdigit(): no_digits = False
#         if ch.islower(): no_lowercase = False
#         if ch.isupper(): no_uppercase = False
#     missing = no_uppercase + no_lowercase + no_digits
#
#     if length_int  < 6:
#         return max(6-length_int, missing)
#
#     for ch in password:
#         if stack and stack[-1] == ch:
#             stack.append(ch)
#             if len(stack) == 3:
#                 if no_digits:
#                     no_digits = False
#                     stack.clear()
#                 elif no_lowercase:
#                     no_lowercase = False
#                     stack.clear()
#                 elif no_uppercase:
#                     no_uppercase = False
#                     stack.clear()
#                 else: length_int -= 1
#                 steps += 1
#             else:
#                 stack.clear()
#                 stack.append(ch)
#         else:
#             stack.append(ch)
#
#     if length_int > 20:
#         steps += length_int -20
#     if no_digits: steps += 1
#     if no_lowercase: steps += 1
#     if no_uppercase: steps += 1
#
#     return steps

