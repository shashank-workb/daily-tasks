def maxSlidingWindow(nums, k):
    i, j, m, maxi, temp = 0, k, -9999, 0, {}
    b = 1
    while b:
        if i >= len(nums):
            break
        if j >= len(nums) - 1:
            j = len(nums)
            b = 0

        for x in range(i, j):
            if nums[x] > m:
                m, maxi = nums[x], x

        temp[j - 1] = maxi
        i += k
        j += k
        m,maxi = -9999, i
        if not b:
            break
    print(temp)


a = maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
print(a)
