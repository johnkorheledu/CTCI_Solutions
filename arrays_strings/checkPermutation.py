# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.
class Solution:
    # sorting solution. o(n) space, o(nlogn) time
    def checkPermutations(s1, s2):
        return sorted(s1) == sorted(s2)

    # map solution. o(n) space, o(n) time
    def checkPermutations2(s1, s2):
        hashM = {}
        for n in s1:
            if n in hashM:
                hashM[n] += 1
            else:
                hashM[n] = 1

        for n in s2:
            if n in hashM:
                hashM[n] -= 1

        for c in hashM:
            if hashM[c] > 0:
                return False
        return True

    print(checkPermutations2("racecar", "carrace"))
