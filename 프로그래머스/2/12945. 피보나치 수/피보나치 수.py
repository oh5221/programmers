def solution(n):
    dp = [0 for i in range(n+1)]
    dp[1] = 1
    
    for j in range(2, n+1):
        dp[j] = dp[j-1]+dp[j-2]
    
    return dp[n] % 1234567