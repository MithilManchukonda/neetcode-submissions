class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        e=[]
        f=[]
        g=[]
        for i in nums:
            if i==0:
                e.append(i)
            elif i==1:
                f.append(i)
            else:
                g.append(i)
        nums[:]=e+f+g

        