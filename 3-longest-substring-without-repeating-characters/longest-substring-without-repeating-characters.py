class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        n = len(s)
        arr=[]

        for i in range(n):
            if s[i] in arr:
                arr=arr[arr.index(s[i])+1:]
            arr.append(s[i])
            longest=max(longest,len(arr))
        return longest
        