class Solution:
    def minSwaps(self, s: str) -> int:
        st = []
        mis = 0
        for i in s:
            if i == '[':
                st.append(i)
            else:
                if st:
                    st.pop()
                else:
                    mis += 1
        return ceil(mis+1)//2
        
        
        