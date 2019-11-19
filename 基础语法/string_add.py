string = input()
message = ''
for i in range(0,len(string)):
    if string[i]!='-':
        message += string[i]
    else:
        break
i = -1
while string[i]!='-':
    i-=1
message+='+'
message+=string[i+1:-1]
message+=string[-1]
print(message)