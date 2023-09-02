class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.stream = sorted(nums)

    def add(self, val: int) -> int:
        if not self.stream or val >= self.stream[-1]:
            self.stream.append(val)
        else:
            i = 0
            while self.stream[i] < val:
                i += 1
            self.stream.insert(i, val)
        return self.stream[-self.k]

if __name__ == "__main__":
    input = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    k, nums = input[0][0], input[0][1]
    add = [input[i][0] for i in range(1, len(input[1:]) + 1)]
    kthLargest = KthLargest(k, nums)
    for val in add:
        print(val, kthLargest.add(val))