class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = [0]*26
        max_count = 0
        window_start = 0
        max_length = 0
        
        for window_end in range(len(s)):
            current_letter_index = ord(s[window_end]) - ord('A')
            char_counts[current_letter_index] += 1
            
            max_count = max(max_count, char_counts[current_letter_index])
            while(window_end - window_start - max_count + 1 > k):
                char_counts[ord(s[window_start]) - ord('A')] -= 1
                window_start +=1
            
            max_length = max(max_length, window_end - window_start + 1)
            
        return max_length