# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, pIe -> true
# pales. pale -> true
# pale. bale -> true
# pale. bake -> false


class Solution:
    def oneAway(s1, s2):
        letters = {}

        for c in s1:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1

        for c in s2:
            if c in letters:
                letters[c] -= 1

        gZeroCount = 0
        for k in letters:
            if letters[k] > 0:
                gZeroCount += 1

        return gZeroCount == 1

    print(oneAway("pale", "bae"))
