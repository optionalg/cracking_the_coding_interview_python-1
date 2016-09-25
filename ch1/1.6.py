# [1:6]. String Compression: Implement a method to perform basic string
# compression using the counts of repeated characters. For example,
# the string aabcccccaaa would become a2b1c5a3. If the "compressed"
# string would not become smaller than the original string, your method
# should return the original string. You can assume the string has only
# uppercase and lowercase letters (a-z)
 
# Time complexity: O(n)
# Space complexity: O(c) for distinct chars
 
import unittest
 
def compress(s):
    if not s:
        return None
    elif len(s) < 3:
        return s
 
    counter = [1]
    compressed = [s[0]]
 
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            counter[-1] += 1
        else:
            counter.append(1)
            compressed.append(s[i])
 
    encrypted = encrypt(counter, compressed)
 
    if len(encrypted) < len(s):
        return encrypted
    return s
 
def encrypt(counter, keys):
    result = []
    for i in range(0, len(keys)):
        result = result + [keys[i] + str(counter[i])]
    return ''.join(result)
 
 
 
class Test(unittest.TestCase):
    def test_compress(self):
        self.assertEqual(compress('aaabbb'), 'a3b3')
        self.assertEqual(compress('aaaaccccbaa'), 'a4c4b1a2')
        self.assertEqual(compress('ababa'), 'ababa')
         
if __name__ == "__main__":
    unittest.main()