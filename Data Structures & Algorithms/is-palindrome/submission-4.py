class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n-1
        s = s.strip()
        #print(s)
        s = s.lower()
        #print(s)
        while i < j:
            left = s[i]
            right = s[j]
            l = False
            r = False
            if (left >= 'a' and left <= 'z') or (left >= '0' and left <= '9'):
                l = True
            if (right >= 'a' and right <= 'z') or (right >= '0' and right <= '9'):
                r = True
            print(i,j)
            if l and r:
                if left != right:
                    return False
                i += 1
                j -= 1
            elif l:
                j -= 1
            elif r:
                i += 1
            elif not l and not r:
                i += 1
                j -= 1
               
        return True
        