with open("./2015/day2/data.txt", "r") as f:
    ribbon = 0
    for line in f:
        nums = line.split('x')
        nums[-1] = nums[-1].split('\n')[0]
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        nums.sort()
        ribbon += (2 * (nums[0] + nums[1])) + (nums[0] * nums[1] * nums[2])


    print(ribbon)

# answer: 3783758