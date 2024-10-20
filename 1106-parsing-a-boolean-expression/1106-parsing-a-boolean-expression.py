class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        exp = expression.replace(',','')
        st = []
        def isop(c):
            return (c=='|' or c=='&' or c=='!')
        def pand(l):
            return False not in l
        def por(l):
            return True  in l
        for i in expression:
            if i=='(':
                st.append(i)
            elif isop(i):
                st.append(i)
            elif i=='f':
                st.append(False)
            elif i=='t':
                st.append(True)
            elif i==')':
                l = []
                while(st[-1]!='('):
                    l.append(st.pop())
                st.pop()
                op = st.pop()
                if op=='&':
                    st.append(pand(l))
                elif op=='|':
                    st.append(por(l))
                else:
                    st.append(not l[0])
        return st[0]
        