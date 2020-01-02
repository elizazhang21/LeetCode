# 8. String to Integer (atoi).py
class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.strip(" ")
        out = ""
        sign = 1
        n = 0
        if s =="":
            return 0 
        if s[0] == "-":
            s = s[1:]
            sign = -1
            num = 1
        elif s[0] == "+":
            s = s[1:]
            num = 1
        
        if s =="":
            return 0   
        if s[0] in "+-" and num == 1:
            return 0
        if len(s) == 1 and s[0] in "1234567890":
            return int(s) * sign
        elif s[0] not in "-1234567890":
            return 0
        else:
            
            i = 1
            out = s[0]
            while i< len(s):
                if s[i] in "1234567890":
                    out += s[i]
                    i += 1
                else:
                    break
        out = int(out) * sign
        if out >= 2**31:
            return 2**31-1
        elif out <= -2**31:
            return -2**31
        else:
            return out
