# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.



from collections import Counter


def canConstruct(ransomNote, magazine):

    # magazine = list(magazine)

    # for char in ransomNote:

    #     if char in magazine:
    #         magazine.remove(char)

    #     else:
    #         return False
        
    # return True


    d = Counter(magazine)

    for char in ransomNote:
        d[char] -= 1

        if d[char] < 0:
            return False                         
        
    return True

print(canConstruct("a", "ba"))


