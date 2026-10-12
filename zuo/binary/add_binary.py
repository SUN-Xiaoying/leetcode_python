# https://leetcode.com/problems/add-binary/description/

class Solution:

    # bin(e) converts an integer to a binary string with a "0b" prefix.
    # TODO: Best Solution
    def addBinary(self, a: str, b: str) -> str:
        c = int(a, 2)
        d = int(b, 2)

        return bin(c+d)[2:]

    # 3ms Beats 44.68%
    def addBinary_mine(self, a: str, b: str) -> str:
        bytes_a = [int(c) for c in a][::-1]
        bytes_b = [int(c) for c in b][::-1]
        len_a = len(a)
        len_b = len(b)
        result=[]
        i=0
        carry=0

        while i < len_a or i < len_b:
            bit_a = bytes_a[i] if i < len_a else 0
            bit_b = bytes_b[i] if i < len_b else 0
            total = bit_a + bit_b + carry
            result.append(total % 2)
            carry = total // 2
            i += 1
        if carry==1: result.append(1)
        return ''.join(str(bit) for bit in result[::-1])

    # def get_byte_list(self, binary_string: str) -> list[int]:
    #     bytes_list = [int(c) for c in binary_string]  # each bit as integer
    #     bytes_list.reverse()  # reverse to add LSB first
    #     return bytes_list

# Input: a = "1010", b = "1011"
# Output: "10101"
s = Solution()
print(s.addBinary("1010", "1011"))