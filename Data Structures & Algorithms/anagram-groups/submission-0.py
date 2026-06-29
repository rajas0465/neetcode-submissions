class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for i in strs:
            t = "".join(sorted(i))
            #print(t)
            if t in d.keys():
                d[t].append(i)
            else:
                d[t] = [i]
        return list(d.values())