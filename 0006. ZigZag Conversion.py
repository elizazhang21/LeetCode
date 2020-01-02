# 6. ZigZag Conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        
        if n == 0:
            return ""
        if numRows == 1:
            return s
        
        k = (n//(2*numRows -2)+1) 
        string = ""
        for i in range(numRows):
            for j in range(k):
                if i ==0 or i == numRows-1:
                    try:
                        string += s[(2*numRows -2)*j + i]
                    except:
                        pass
                else:
                    try:
                        string += s[(2*numRows -2)*j + i]
                        string += s[(2*numRows -2)*(j+1) - i]
                    except:
                        pass
        return string
