class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        #arr.append(-1)
        for i in range(n):
            if i == n-1:
                arr[i] = -1
            else:
                arr[i] = max(arr[i+1:n])
        return arr
        