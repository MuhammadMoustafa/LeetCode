1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        start_index = 0
4        end_index = 0
5        max_length = 0
6
7        substring = {}
8
9        for idx, letter in enumerate(s):
10            if letter not in s[start_index: end_index]:
11                substring[letter] = idx
12                # print(f"not in ==> index = {idx}, letter = {letter}, substring = {substring}, start_index = {start_index}, end_index = {end_index}")
13            else:
14                new_length = end_index - start_index
15                if new_length > max_length:
16                    max_length = new_length
17                
18                if s[start_index] == letter:
19                    start_index += 1
20                else:
21                    start_index = substring[letter] + 1
22                
23                substring[letter] = idx
24                
25                # if start_index == end_index:
26                #     end_index += 1
27                # substring = s[start_index: end_index]
28                # print(f"in ==> index = {idx}, letter = {letter}, substring = {substring}, start_index = {start_index}, end_index = {end_index}")
29            end_index += 1
30
31        print(max(max_length, end_index - start_index))
32        return max(max_length, end_index - start_index)