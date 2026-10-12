# https://leetcode.com/problems/validate-ip-address/description/
import re

class Solution:
#0 ms Beats 100.00%
    def validIPAddress(self, queryIP: str) -> str:
        # Remove overall length checks
        query_len = len(queryIP)
        if query_len < 7:
            return "Neither"
        if query_len > 39:
            return "Neither"
        if not re.fullmatch(r'[0-9a-fA-F.:]+', queryIP):
            return "Neither"


        if "." in queryIP:
            result = queryIP.split(".")
            # Return early when the part count is wrong
            if len(result) == 4:
                for address in result:
                    if not address or not address.isdigit():
                        return "Neither"
                    if int(address) > 255:
                        return "Neither"
                    if len(address) > 1 and address[0]=="0":
                        return "Neither"
                return "IPv4"
        else:
            result = queryIP.split(":")
            if len(result) == 8:
                for address in result:
                    if not 1 <= len(address) <= 4:
                        return "Neither"
                return "IPv6"

        return "Neither"


s = Solution()
print(s.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
print(s.validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334"))
print(s.validIPAddress("2001:0db8:85a3::8A2E:037j:7334"))
print(s.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334:"))
print(s.validIPAddress("2001:0db8:85a3:00000:0:8A2E:0370:7334"))
print(s.validIPAddress("f:f:f:f:f:f:f:f"))
print(s.validIPAddress("1.1.1.1"))
print(s.validIPAddress("192.168.01.1"))
print(s.validIPAddress("192.168.1.00"))
print(s.validIPAddress("192.168@1.1"))
print(s.validIPAddress("192.168.1.0"))