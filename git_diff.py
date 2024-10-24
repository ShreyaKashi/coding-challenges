# 
def longest_common_substring(text1, text2):

    def dp(i, j):
        if i == -1 or j == -1:
            return ""
        
        if text1[i] == text2[j]:
            return dp(i-1, j-1) + text1[i]
        
        else: 
            option1 = dp(i-1, j)
            option2 = dp(i, j-1)
            return option1 if len(option1) > len(option2) else option2
        
    out = dp(len(text1)-1, len(text2)-1)

    return out

# 
def longest_common_subsequence_lines(lines1, lines2):

    def dp(i, j):
        if i == -1 or j == -1:
            return []
        
        if lines1[i] == lines2[j]:
            return dp(i-1, j-1) + [lines1[i]]
        
        else: 
            option1 = dp(i-1, j)
            option2 = dp(i, j-1)
            return option1 if len(option1) > len(option2) else option2

    return dp(len(lines1)-1, len(lines2)-1)


# print(longest_common_substring("abcde", "ace"))

lines1 = ["This is a test which contains:", "this is the lcs"]
lines2 = ["this is the lcs", "we're testing"]
print(longest_common_subsequence_lines(lines1, lines2))