class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # innitiates the variable total = 0
        total = 0

        # itterates through our string s using the len of s -1 since range is start inclusice and end exclusive
        for i in range(len(s)):
            # first checks if the current index of s is the last index by comparing it to length of s -1 since we are comparing index
            # after the and we check to see if the current index of s in roman_numerals map is lass than the next index of s.
            # if so we subtract the current roman_numeral value from total
            if i < len(s) - 1 and roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
                total -= roman_numerals[s[i]]
            # if not we add
            else:
                total += roman_numerals[s[i]]
        # this returns value of total after the interation is over
        return total
