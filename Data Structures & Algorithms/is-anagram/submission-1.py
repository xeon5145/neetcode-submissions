class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check1 = False
        # check2 = False

        # # Check 1 : Length
        # if len(s) == len(t):
        #     check1 = True
        # else:
        #     check1 = False

        # # Check 2 : Characters
        # if sorted(s) == sorted(t):
        #     check2 = True
        # else:
        #     check2 = False

        # if check1 == True and check2 == True:
        #     return True
        # else:
        #     return False

        # Better one
        if (sorted(s) == sorted(t)) and (len(s) == len(t)):
            return True
        else:
            return False
        