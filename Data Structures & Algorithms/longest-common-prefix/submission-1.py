class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallstr = strs[0]
        for i in range(len(strs)):
            if len(strs[i]) < len(smallstr):
                smallstr = strs[i]
        c = 0
        #print(smallstr)
        for i in smallstr:
            for j in strs:
                if i != j[c]:
                    return smallstr[:c] if c != 0 else ""
            c += 1
        return smallstr

        