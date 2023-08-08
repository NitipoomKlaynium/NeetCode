import re

def isPalindrome(s: str) -> bool:
    s = "".join(re.split("[^a-zA-Z0-9]", s)).lower()
    l = len(s)
    hl = len(s) // 2
    return s[:hl] == s[:hl - (1 if l % 2 == 0 else 0):-1]

if __name__ == "__main__" :
    print(isPalindrome("AA2B@@@2AA"))