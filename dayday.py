#the strength of one year
dayup = pow(1.001,365)
daydown = pow(0.999,365)
print("向上：" + str(dayup) + "向下：" + str(daydown))
dayfactor = 0.005
dayup = pow(1+dayfactor,365)
daydown = pow(1-dayfactor,365)
print(round(dayup,2),round(daydown,2))
dayfactor = 0.01
dayup = pow(1+dayfactor,365)
daydown = pow(1-dayfactor,365)
print(round(dayup,2),round(daydown,2))