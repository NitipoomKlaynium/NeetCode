import re
import math
import copy

def containsDuplicate(nums: list[int]) -> bool:
    nums.sort()
    for i in range(len(nums) - 1) :
        if (nums[i] == nums[i + 1]) :
            return True
    return False

def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)) :
        if (nums[i] <= target) :
            for j in range(i + 1, len(nums)) :
                print(nums[i], nums[j])
                if (nums[i] + nums[j] == target) :
                    return [i, j]
                
def isPalindrome(s: str) -> bool:
    return s == s[::-1]
    
def isValid(s: str) -> bool:
    def check(l: str, r: str) :
        return (l == "(" and r == ")") or (l == "{" and r == "}") or (l == "[" and r == "]")
        
    stack = ""
    for i in range(len(s)) :
        print(stack)
        if stack == "" and s[i] in ")}]" :
            return False
        elif (s[i] in "({[") :
            stack += s[i]
        elif check(stack[-1], s[i]) :
            stack = stack[:-1]
        else :
            return False
    if stack != "" :
        return False
    return True

def search(self, nums: list[int], target: int) -> int:
    center = len(nums) // 2

    if nums[center] == target :
        return center
    elif nums[center] < target :
        return search(nums[:center], target)
    else :
        return search(nums[center + 1:], target)

def find_duplicates(data):
    duplicates = []
    data_set = set()
    for num in data:
        if num in data_set:
            duplicates.append(num)
        else:
            data_set.add(num)
    return duplicates


class MyArray:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, indices):
        print(type(indices))
        print(indices)
        if isinstance(indices, tuple) and len(indices) == 2:
            row_indices, col_indices = indices
            if isinstance(row_indices, slice) and isinstance(col_indices, slice):
                # Extract start, stop, and step from slice objects
                row_start, row_stop, row_step = row_indices.indices(len(self.data))
                col_start, col_stop, col_step = col_indices.indices(len(self.data[0]))
                # Use built-in list slicing to get a 2D sub-array
                return [row[col_start:col_stop:col_step] for row in self.data[row_start:row_stop:row_step]]

        else:
            raise IndexError('Invalid index')

def waterContainer(walls: list) -> list:
    indices = list(range(0, len(walls)))
    
    walls_order = sorted(indices, key=lambda x: walls[x], reverse=True)
    waters = [-1] * (len(walls) - 1)
    remaining = len(walls)
    
    for i in range(1, len(walls_order)):
        a = walls_order[i - 1]
        b = walls_order[i]
        start = min(a, b)
        stop = max(a, b)
        for j in range(start, stop):
            if waters[j] == -1:
                waters[j] = walls[b]
                remaining -= 1
                
    for i in range(len(waters)):
        if waters[i] == -1:
            waters[i] = 0
    
    return waters

def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # Into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def _decorator(f):
    
    def w(*arg, **kwargs):
        print("Start decorator")
        result = f(*arg, **kwargs)
        print("End decorator")
        return result
    
    return w

@_decorator
def greet():
    print("Hello")

def fibonacci(n):
    result = [0, 1]
    
    if n < 2:
        return result[n]
    
    i = 2
    while i < n:
        result.append(result[-1] + result[-2])
        i += 1
    return result[-1]

def allParen(n):
    pass

def count_pairs(number_list: list, power: int, distance: int) -> int:
    pairs = 0
    
    for i in range(len(number_list)):
        a = number_list[i] ** power
         
        if number_list[i] % power == 0:
            for j in range(i + 1, len(number_list)):
                if abs(a - number_list[j] ** power) <= distance:
                    pairs += 1
        else:
            for j in range(i + 1, len(number_list)):
                if number_list[j] % power == 0 and abs(a - number_list[j] ** power) <= distance:
                    pairs += 1
                    
    return pairs

# class Solution:
#     def wordBreak(self, s: str, wordDict: list[str]) -> bool:
#         n = len(s)
#         m = len(max(wordDict, key=lambda x: len(x)))
#         # temp = [0] * n
#         # itr = 0
#         stack = [(0, [])]
#         warning = 0
#         while stack:
#             itr, used = stack[-1]
#             print(itr, s[itr:])
#             for i, wd in enumerate(wordDict):
#                 if wd not in used:
#                     ld = len(wd)
#                     used.append(wd)
#                     print('compare', s[itr:itr + ld], '|', wd)
#                     if s[itr:itr + ld] == wd:
#                         if itr + ld >= n:
#                             return True
#                         stack.append((itr + ld, []))
#                         print("Cut!", itr, n)
#                         break
#             else:
#                 stack.pop()

#         return False

import collections

def isSub(a, b):
    s = collections.Counter(a)
    t = collections.Counter(b)
    return all(s[char] >= t[char] for char in t)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        tl = 0
        min_len = 0xFFFFFFFF
        # print(isSub("cwae", t))
        for i in range(m - n + 1):
            # print(s[i:])
            for j in range(i + n, min(m + 1, i + min_len)):
                # print(f'Check:    i: {i}, j: {j}, m: {m}, min_len: {min_len}')
                # print(f'\t{s[i:j]}')
                check_s = s[i:j]
                if isSub(check_s, t):
                    print("PASSED -> ", check_s, t)
                    new_len = j - i
                    if new_len < min_len:
                        min_len = new_len
                        tl = i
                        break
            # print("======================================")
            if min_len == n:
                break
        if min_len == 0xFFFFFFFF:
            return ""
        return s[tl:tl + min_len]

if __name__ == '__main__':
    # w = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # d = ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]

    s = "obzcopzocynyrsgsarijyxnkpnukkrvzuwdjldxndmnvevpgmxrmvfwkutwekrffnloyqnntbdohyfqndhzyoykiripdzwiojyoznbtogjyfpouuxvumtewmmnqnkadvzrvouqfbbdiqremqzgevkbhyoznacqwbhtrcjwfkzpdstpjswnpiqxjhywjanhdwavajrhwtwzlrqwmombxcaijzevbtcfsdcuovckoalcseaesmhrrizcjgxkbartdtotpsefsrjmvksqyahpijsrppdqpvmuocofuunonybjivbjviyftsyiicbzxnwnrmvlgkzticetyfcvqcbjvbufdxgcmesdqnowzpshuwcseenwjqhgsdlxatamysrohfnixfprdsljyyfhrnnjsagtuihuczilgvtfcjwgdhpbixlzmakebszxbhrdibpoxiwztshwczamwnninzmqrmpsviydkptjzpktksrortapgpxwojofxeasoyvyprjoguhqobehugwdvtzlenrcttuitsiijswpogicjolfxhiscjggzzissfcnxnvgftxvbfzkukqrtalvktdjsodmtgzqtuyaqvvrbuexgwqzwduixzrpnvegddyyywaquxjxrnuzlmyipuqotkghfkpknqinoidifnfyczzonxydtqroazxhjnrxfbmtlqcsfhshjrxwqvblovaouxwempdrrplefnxmwrwfjtebrfnfanvvmtbzjesctdgbsfnpxlwihalyiafincfcwgdfkvhebphtxukwgjgplrntsuchyjjuqozakiglangxkttsczhnswjksnuqwflmumpexxrznzwxurrysaokwxxqkrggytvsgkyfjrewrcvntomnoazmzycjrjrqemimyhriyxgrzcfuqtjhvjtuhwfzhwpljzajitrhryaqchnuawbxhxrpvyqcvhpggrpplhychyulijhkglinibedauhvdydkqszdbzfkzbvhldstocgydnbfjkcnkfxcyyfbzmmyojgzmasccaahpdnzproaxnexnkamwmkmwslksfpwirexxtymkmojztgmfhydvlqtddewjvsrmyqjrpycbmndhupmdqqabiuelacuvxnhxgtpvrtwfgzpcrbhhtikbcqpctlxszgpfbgcsbaaiapmtsucocmpecgixshrrnhyrpalralbccnxvjzjllarqhznzghswqsnfuyywmzbopyjyauknxddgdthlabjqtwxpxwljvoxkpjjpfvccyikbbrpdsyvlxscuoofkecwtnfkvcnzbxkeabtdusyhrqklhaqreupakxkfzxgawqfwsaboszvlshwzhosojjotgyagygguzntrouhiweuomqptfjjqsxlbylhwtpssdlltgubczxslqjgxuqnmpynnlwjgmebrpokxjnbiltvbebyytnnjlcwyzignmhedwqbfdepqakrelrdfesqrumptwwgifmmbepiktxavhuavlfaqxqhreznbvvlakzeoomykkzftthoemqwliednfsqcnbexbimrvkdhllcesrlhhjsspvfupxwdybablotibypmjutclgjurbmhztboqatrdwsomnxnmocvixxvfiqwmednahdqhxjkvcyhpxxdmzzuyyqdjibvmfkmonfxmohhshpkhmntnoplphqyprveyfsmsxjfosmicdsjrieeytpnbhlsziwxnpmgoxneqbnufhfwrjbqcsdfarybzwaplmxckkgclvwqdbpumsmqkswmjwnkuqbicykoisqwoootrdpdvcuiuswfqmrkctsgrevcxnyncmivsxbpbxzxpwchiwtkroqisnmrbmefbmatmdknaklpgpyqlsccgunaibsloyqpnsibwuowebomrmcegejozypjzjunjmeygozcjqbnrpakdermjcckartbcppmbtkhkmmtcngteigjnxxyzaibtdcwutkvpwezisskfaeljmxyjwykwglqlnofhycwuivdbnpintuyhtyqpwaoelgpbuwiuyeqhbvkqlsfgmeoheexbhnhutxvnvfjwlzfmvpcghiowocdsjcvqrdmkcizxnivbianfpsnzabxqecinhgfyjrjlbikrrgsbgfgyxtzzwwpayapfgueroncpxogouyrdgzdfucfrywtywjeefkvtzxlwmrniselyeodysirqflpduvibfdvedgcrzpzrunpadvawfsmmddqzaaahfxlifobffbyzqqbtlcpquedzjvykvarayfldvmkapjcfzfbmhscdwhciecsbdledspgpdtsteuafzbrjuvmsfrajtulwirzagiqjdiehefmfifocadxfuxrpsemavncdxuoaetjkavqicgndjkkfhbvbhjdcygfwcwyhpirrfjziqonbyxhibelinpllxsjzoiifscwzlyjdmwhnuovvugfhvquuleuzmehggdfubpzolgbhwyeqekzccuypaspozwuhbzbdqdtejuniuuyagackubauvriwneeqfhtwkocuipcelcfrcjcymcuktegiikyosumeioatfcxrheklookaqekljtvtdwhxsteajevpjviqzudnjnqbucnfvkybggaybebljwcstmktgnipdyrxbgewqczzkaxmeazpzbjsntltjwlmuclxirwytvxgvxscztryubtjweehapvxrguzzsatozzjytnamfyiitreyxmanhzeqwgpoikcjlokebksgkaqetverjegqgkicsyqcktmwjwakivtsxjwrgakphqincqrxqhzbcnxljzwturmsaklhnvyungjrxaonjqomdnxpnvihmwzphkyuhwqwdboabepmwgyatyrgtboiypxfavbjtrgwswyvcqhzwibpisydtmltbkydhznbsvxktyfxopwkxzbftzknnwipghuoijrbgqnzovxckvojvsqqraffwowfvqvfcmiicwitrhxdeombgesxexedlakitfovtydxunqnwqqdeeekiwjnwoshqcsljiicgobbbuqakjdonjawgjlezdnqhfdqnmsuavxdpnfzwipmspiabveaarshzwxmirgkmfncvtdrdvfxkpxlkdokxgtwcskmjryyymcthfnkasinihaunohkxaibtsqelockaefjmsuolebtnepauwmrxutspjwaxbmahsjtkfkxlnszribmeofbkyvbjscjtqjakuwvcgunvnonvqbbggfshauqsyznokqbhowjusypfnecffenojfvlblgzntqzlrgzprvhqnpfrrkzxznieiuivajivzijsqijigtatifmbplzqahuidegfoobpymkputzamzvweiyvvzlwihgmmmrcburbgbsdxrfjsbiylitghgcpqjbevvgypxcybubyoijijrhuzcdijfybqbfowlookqmlnplbxvjjosfqviygqyhgamuwzjklbyzopkrnhbywtfoqomweldmlrhjqswctubiknzzvcztyehouvnyiqnvkufaobehxhrjvtisxjlxoumipzjarwvbsaegdkpbsjmpevjbewzuqnfhoohhmdjgfpmjzdmtmykqvtucptwfidpwtwffzolffzqfdearclkyeecuzabjeqhxpmfodsvisnpxrqowdawheydfyhoexvcmihdlzavtqlshdhdgjzpozvvackebhgqppvcrvymljfvooauxcjnbejdivikcoaugxwzsulgfqdtefpehbrlhaoqxwcancuvbqutnfbuygoemditeagmcveatgaikwflozgdhkyfqmjcruyyuemwbqwxyyfiwnvlmbovlmccaoguieu"
    t = "cjgamyzjwxrgwedhsexosmswogckohesskteksqgrjonnrwhywxqkqmywqjlxnfrayykqotkzhxmbwvzstrcjfchvluvbaobymlrcgbbqaprwlsqglsrqvynitklvzmvlamqipryqjpmwhdcsxtkutyfoiqljfhxftnnjgmbpdplnuphuksoestuckgopnlwiyltezuwdmhsgzzajtrpnkkswsglhrjprxlvwftbtdtacvclotdcepuahcootzfkwqhtydwrgqrilwvbpadvpzwybmowluikmsfkvbebrxletigjjlealczoqnnejvowptikumnokysfjyoskvsxztnqhcwsamopfzablnrxokdxktrwqjvqfjimneenqvdxufahsshiemfofwlyiionrybfchuucxtyctixlpfrbngiltgtbwivujcyrwutwnuajcxwtfowuuefpnzqljnitpgkobfkqzkzdkwwpksjgzqvoplbzzjuqqgetlojnblslhpatjlzkbuathcuilqzdwfyhwkwxvpicgkxrxweaqevziriwhjzdqanmkljfatjifgaccefukavvsfrbqshhswtchfjkausgaukeapanswimbznstubmswqadckewemzbwdbogogcysfxhzreafwxxwczigwpuvqtathgkpkijqiqrzwugtr"
    solution = Solution()
    print(solution.minWindow(s, t))