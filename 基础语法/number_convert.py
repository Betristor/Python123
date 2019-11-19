number = input()
number_list = []
number = eval(number)
message=''
dic = {'0':'零','1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九'}
while number > 0:
    number_list.append(number%10)
    number = int(number/10)
for n in range(0,len(number_list)):
    message+=dic[str(number_list[len(number_list)-1-n])]
print(message)