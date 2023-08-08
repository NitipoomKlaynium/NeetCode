def isAnagram(s: str, t: str) -> bool:
    return True if sorted(s) == sorted(t) else False

if __name__ == "__main__" :
    print(isAnagram("asd", "sad"))