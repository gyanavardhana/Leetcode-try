class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        return (z:={c:-1 for c in 'abc'}) and sum(1+min((z:=z|{c:i}).values()) for i,c in enumerate(s))
        