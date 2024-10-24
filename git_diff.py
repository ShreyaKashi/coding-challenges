# Compares two strings and returns the longest common subsequence between them
def longest_common_substring(text1, text2):
    cache = {}
    def dp(i, j):
        if (i,j) in cache:
            return cache[(i, j)]
        
        if i == -1 or j == -1:
            cache[(i, j)] = ""
            return ""
        
        if text1[i] == text2[j]:
            cache[(i, j)] = dp(i-1, j-1) + text1[i]
            return cache[(i, j)]
        
        else: 
            option1 = dp(i-1, j)
            option2 = dp(i, j-1)
            if len(option1) > len(option2):
                cache[(i, j)] = option1
            else:
                cache[(i, j)] = option2
            return cache[(i, j)]
        
    out = dp(len(text1)-1, len(text2)-1)

    return out

# Compares two lists of strings and returns the longest common subsequence between them
def longest_common_subsequence_lines(lines1, lines2):
    cache = {}
    def dp(i, j):

        if (i,j) in cache:
            return cache[(i, j)]
        
        if i == -1 or j == -1:
            cache[(i, j)] = []
            return []
        
        if lines1[i] == lines2[j]:
            cache[(i, j)] = dp(i-1, j-1) + [lines1[i]]
            return cache[(i, j)]
        
        else: 
            option1 = dp(i-1, j)
            option2 = dp(i, j-1)
            if len(option1) > len(option2):
                cache[(i, j)] = option1
            else:
                cache[(i, j)] = option2
            return cache[(i, j)]

    return dp(len(lines1)-1, len(lines2)-1)


