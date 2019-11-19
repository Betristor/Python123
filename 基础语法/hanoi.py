count = 0
def hanoi(n,start,end,via):
    global count
    if n == 1:
        print("{}:{}->{}".format(1,start,end))
        count += 1
    else:
        hanoi(n-1,start,via,end)
        print("{}:{}->{}".format(n,start,end))
        count += 1
        hanoi(n-1,via,end,start)
hanoi(3,'a','b','c')
print(count)