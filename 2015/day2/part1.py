with open("./2015/day2/data.txt", "r") as f:
    paper = 0
    for line in f:
        nums = line.split('x')
        nums[-1] = nums[-1].split('\n')[0]
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        nums.sort()
        paper += ((2 * nums[0] * nums[1]) + 
                (2 * nums[0] * nums[2]) + 
                (2 * nums[1] * nums[2])) + (nums[0] * nums[1])


    print(paper)

# answer: 1588178