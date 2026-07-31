class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            #this goes through and updates the count based on the occurence of each key
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            #this checks each key and makes sure the counts for each are the same in both hashmaps
            #we use the c, 0 again because if that key dosent exist we will get an error
            #so we default to a value of 0
            if countS[c] != countT.get(c, 0):
                return False
        
        return True
        