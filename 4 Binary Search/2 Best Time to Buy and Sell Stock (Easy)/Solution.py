def maxProfit(prices: list[int]) -> int:
    maxProfit = 0
    minBuy = prices[0]
    for i in range(1, len(prices)) :
        if prices[i] < minBuy :
            minBuy = prices[i]      
        elif prices[i] - minBuy > maxProfit :
            maxProfit = prices[i] - minBuy
    return maxProfit
    
if __name__ == "__main__" :
    print(maxProfit([7,6,4,3,1]))