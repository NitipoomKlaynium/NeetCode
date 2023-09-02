# def count_rectangles (coordinates, min_area):
#     #Write your code here
#     n = len(coordinates)
#     result = 0
    
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             x1, y1 = coordinates[i][0], coordinates[j][1]
#             x2, y2 = coordinates[j][0], coordinates[i][1]
#             if [x1, y1] in coordinates and [x2, y2] in coordinates:
#                 if abs(x1 - x2) * abs(y1 - y2) >= min_area:
#                     result += 1

#     return result // 2

def count_rectangles (coordinates, min_area):
    
    def isRectangle(c1, c2, c3, c4):
        all = [c1, c2, c3, c4]
        lst1 = [c1]
        for i in range(1, 4):
            if c1[0] != all[i][0] and c1[1] != all[i][1]:
                lst1.append(all[i])
                break
            
        if [lst1[0][0], lst1[1][1]] in all and [lst1[1][0], lst1[0][1]] in all:
            return (True, abs(lst1[0][0] - lst1[1][0]) * abs(lst1[0][1] - lst1[1][1]))
        else:
            return (False, 0)
    
    n = len(coordinates)
    if n < 4:
        return False
    
    result = 0
    
    for i1 in range(n - 3):
        for i2 in range(i1 + 1, n - 2):
            for i3 in range(i2 + 1, n - 1):
                for i4 in range(i3 + 1, n):
                    check, area = isRectangle(coordinates[i1], coordinates[i2], coordinates[i3], coordinates[i4])
                    if check == True and area >= min_area:
                        result += 1

    return result

def segment (text, dictionary):
    if text == "":
        return 1
    if dictionary == []:
        return 
    n = len(text)
    maxDicLen = len(max(dictionary, key=lambda x: len(x)))
    temp = [False] *  (n + 1)
    temp[0] = True
    for i in range(1, n + 1):
        for j in range(max(0, i - maxDicLen), i + 1):
            check_text = text[j:i]
            if check_text in dictionary:
                if temp[i - len(check_text)] == True:
                    temp[i] = True
                    break
    return 1 if temp[-1] else 0

if __name__ == "__main__":
    # coordinates = [[0,0], [0, 3], [5, 3], [5, 0], [9, 9]]
    # min_area = 15
    coordinates = [[8,7], [8,2], [5,5], [3,7], [3,2], [1,1], [1,5], [5,1]]
    min_area = 15
    print(count_rectangles(coordinates, min_area))