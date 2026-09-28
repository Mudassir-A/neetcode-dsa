class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for x in strs:
            s += x + "~"
        return s

    def decode(self, s: str) -> List[str]:
        n = []
        c = ""
        for x in s:
            if "~" == x:
                n.append(c)
                c = ""
            else:
                c += x
        return n
