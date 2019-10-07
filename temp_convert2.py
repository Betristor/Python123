tempstr = input()
length = len(tempstr)
if tempstr[0] == 'C':
    F = 1.8*eval(tempstr[1:length])+32
    print("F{:.2f}".format(F))
elif tempstr[0] == 'F':
    C = (eval(tempstr[1:length])-32)/1.8
    print("C{:.2f}".format(C))