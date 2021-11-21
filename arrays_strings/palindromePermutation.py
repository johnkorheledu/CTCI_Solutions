# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.)


# o(n) space, o(n) time
class Solution:
    def palindromePermutation(s):
        s2 = s.lower().replace(" ", "")
        letters = {}

        for c in s2:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1

        oddCount = 0

        for k in letters:
            if letters[k] % 2 == 0:
                pass
            else:
                oddCount += 1
        print(letters)
        print(oddCount)
        if oddCount == 1:
            return True

        return False

    print(palindromePermutation("Tact Coa"))
