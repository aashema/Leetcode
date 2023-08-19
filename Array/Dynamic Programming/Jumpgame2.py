def jumpgame2(arr, n):
    res =0 
    l = r = 0 
    for i in range(0,n):
        r = max(r, i+arr[i])
        if i == l:
            l = r
            res+=1
            if r>=n-1:
                return res
    return -1
n=5
arr = [2,3,1,1,4]
print(jumpgame2(arr,n))