def JumpGame(arr):
    goal = len(arr)- 1  # setting the goal post at the end
    for i in range(len(arr)-1,-1,-1):   # reverse array to set new goal post 
        if i + arr[i] >= goal:
            goal = i 
    return True if goal == 0 else False
arr = [2,3,1,1,4]
print(JumpGame(arr))
