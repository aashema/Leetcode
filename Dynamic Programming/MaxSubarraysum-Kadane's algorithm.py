def maxSubArraySum(arr,N):
    maxsum = arr[0]
    sum = 0
    for i in range(N) :
        sum = sum +arr[i]
        maxsum = max(maxsum, sum)
        if sum<0:
            sum =0
    return maxsum
print(maxSubArraySum([1,2,3,-2,5], 5))