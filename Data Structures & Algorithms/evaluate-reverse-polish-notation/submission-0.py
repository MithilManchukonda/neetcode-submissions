class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=[]
        for ch in tokens:
            if ch in "+-*/":
                res=0
                second=a.pop()
                first=a.pop()
                if ch=="+":
                    res=int(first)+int(second)
                elif ch=="-":
                    res=int(first)-int(second)
                elif ch=="*":
                    res=int(first)*int(second)
                else:
                    res=int(first)/int(second)
                a.append(res)
            else:
                a.append(ch)
        return int(a[0])


        
            
        