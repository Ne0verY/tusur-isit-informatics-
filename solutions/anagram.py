def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    def char_frequency(s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        return freq
    
    return char_frequency(s1) == char_frequency(s2)

if __name__ == "__main__":
    print(is_anagram("heart", "earth"))
    print(is_anagram("python", "typhon"))
    print(is_anagram("hello", "world"))
    print(is_anagram("ab", "abc"))