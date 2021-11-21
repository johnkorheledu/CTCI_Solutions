# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?


class Solution:
    # o(n) space, o(n) time
    def isUnique(s):
        hashM = {}
        for c in s:
            if c in hashM:
                return False
            else:
                hashM[c] = c
        return True

    print(isUnique("zippity"))
    print(isUnique("abcd"))
