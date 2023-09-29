class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # casts number arg into type string and stores it in string_num variable
        string_num = str(x)
        # slicies  string num in reverse and stores it in reversed_num var
        reversed_num = string_num[::-1]
        # compares string_num to reversed_num and returns True if num is a palindrome and False if it isn't
        if string_num == reversed_num:
            return True
        else:
            return False
