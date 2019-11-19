def getnum():
    nums = []
    inumstr = input("请输入数字(按回车退出):")
    while inumstr != "":
        nums.append(eval(inumstr))
        inumstr = input("请输入数字(按回车退出):")
    return nums

def mean(nums):
    s = 0.0
    for num in nums:
        s += num
    return s/len(nums)

def dev(nums,mean):
    #计算方差
    sdev = 0.0
    for num in nums:
        sdev += (num - mean)**2
    return pow(sdev / len(nums),0.5)

def median(nums):
    #计算中位数
    sorted(nums)
    size = len(nums)
    if size % 2 == 0:
        median = (nums[size // 2 - 1] + nums[size // 2]) / 2
    else:
        median = nums[size // 2]
    return median

n = getnum()
mean = mean(n)
print("数据的平均值为{},数据的方差为{},数据的中位数为{}.".format(mean,dev(n,mean),median(n)))