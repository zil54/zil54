#Given a string s, find the length of the longest without duplicate characters.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        set_of_chars = set()  # Set to track unique characters in the current window
        max_length = 0  # To store the length of the longest substring found
        removal_from_set_index = 0  # removal from set tracker

        # Iterate over the string with the right pointer (index)
        for index, char in enumerate(s):
            # If the current character is already in the set,
            # remove characters from the left of the window (and update start)
            while char in set_of_chars:
                set_of_chars.remove(s[removal_from_set_index])
                removal_from_set_index += 1

            # Add the current character to the set
            set_of_chars.add(char)

            # Update the maximum length if the current window is larger
            max_length = max(max_length, len(set_of_chars))

        return max_length


# Example usage:
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
