class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
                
        letter_word = {}
        word_letter = {}
        
        wordList = s.split(" ")
        if len(wordList) != len(pattern): return False
        
        for idx, char in enumerate(pattern):
            word = wordList[idx]
            if char in letter_word:
                if letter_word[char] != word: return False
            else:
                letter_word[char] = word
                
            if word in word_letter:
                if word_letter[word] != char: return False
            else:
                word_letter[word] = char
                
        return True
        
        