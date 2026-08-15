# Last updated: 8/15/2026, 10:36:38 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq={}
        l=0
        max_len=0

        for i in range(len(s)):
            
            
                
            while s[i] in freq:
                    
                del freq[s[l]]
                l+=1
            freq[s[i]]=freq.get(s[i],0)+1
            
            max_len=max(max_len,i-l+1)
            
                 
            
        return max_len            

        