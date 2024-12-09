def palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    n = len(s)
    
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False

    return True
print(palindrome('barabashka'))
