filename = "test.txt"
f = open(filename,'rt')
lines = f.readlines()
f.close()
sline = 0
s = 0
for line in lines:
    if line != '':
        sline += 1
        for c in line:
            if c != ' ':
                s += 1
print(round(s/sline))