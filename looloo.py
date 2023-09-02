def count_pairs (number_list, divisor, distance):
    
    n = len(number_list)
    result = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if number_list[i] % divisor == number_list[j] % divisor and abs(number_list[i] // 10 % 10 - number_list[j] // 10 % 10) <= distance:
                result += 1
    return result

def find_most_frequent_substring(text, length):
    n = len(text)
    if n < length:
        return ""
    
    counter = {}
    for i in range(n - length + 1):
        key = text[i:i + length]
        counter[key] = counter.get(key, 0) + 1
    
    max_value = max(counter.values())
    result = max(counter, key=counter.get)
    for k, v in counter.items():
        if v == max_value:
            result = min(result, k)
    return result

def check_perfect_list (numbers, distance):
    
    n = len(numbers)
    
    for i in range(n // 2):
        a = 2 * i + 1
        b = 2 * i + 2
        if abs(numbers[i] - numbers[a]) > distance or (b < n and abs(numbers[i] - numbers[b]) > distance):
            return False
        
    return True

def segment (text, dictionary):
    memo = [text]
    max_key_length = len(max(dictionary, key = lambda x: len(x)))
    # print(f'{text} {dictionary} {max_key_length}')
    while memo:
        s = memo.pop()
        # print(s)
        for i in range(min(len(s), max_key_length) + 1):
            # print(i, s[:i])
            if s[:i] in dictionary:
                if s[i:] == "":
                    return 1
                else:
                    # print(s[i:])
                    memo.append(s[i:])

    return 0

def count_perfect_square(numbers):
    n = len(numbers)
    square = 1
    temp = 1
    nums = sorted(numbers)
    result = 0
    # print(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            print(nums[i], nums[j], square)
            num = nums[i] + nums[j]
            if num > square:
                while num > square:
                    square += temp + temp + 1
                    temp += 1
            elif num < square:
                while num < square:
                    square -= temp + temp - 1
                    temp -= 1
                    
            if num == square:
                result += 1
                

    return result

def count_unique_ascending_numbers (stream):
    n = len(stream)
    result = 0
    temp_lst = []
    i = 0
    while i < n:
        if stream[i].isnumeric() :
            check = True
            start = i
            i += 1
            while i < n:
                if stream[i].isnumeric():
                    check = check & (stream[i] > stream[i - 1])
                else:
                    temp = stream[start:i]
                    if check and temp not in temp_lst:
                        temp_lst.append(temp)
                        result += 1
                    break
                i += 1
            else:
                temp = stream[start:i]
                if check and temp not in temp_lst:
                    temp_lst.append(temp)
                    result += 1
        else:
            i += 1


    return result


if __name__ == "__main__":
    
    # print(count_pairs([], 3, 2))
    # print(5 // 2)
    # print(min("", "ab"))
    # print(find_most_frequent_substring("k%abxc/d*dk%abcd*dk", 4))
    # print(find_most_frequent_substring("abba", 1))
    
    # print(check_perfect_list([5, 6, 13, 15, 7, 10, 40], 10))
    # print(check_perfect_list([], 10))
    # print(check_perfect_list([1], 1))
    # print(check_perfect_list([1, 2], 1))
    # print(check_perfect_list([1, 2, 3], 1))
    # print(check_perfect_list([1, 4, 3, 2 ,3], 1))
    
    # print(segment('thisisgood', ['this','is','good']))
    # print(segment('thisisbad', ['this','is','good']))
    # print(segment('aabbcc', ['a','b','c']))
    # print(segment('abcdef', ['abc','dex']))
    # print(segment('abcdef', ['abc','dex','abcd','ef']))
    # print(segment('test1 test*?', ['test','1 ','*?']))
    
    # print(count_perfect_square([10, 20, 44, 54, 128, 2]))

    print(count_unique_ascending_numbers('321ab45z'))
    print(True + True)
    # print(count_unique_ascending_numbers('4689'))
    
        