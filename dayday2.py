#workday
dayup = 1
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup*(1 - dayfactor)
    else:
        dayup = dayup*(1 + dayfactor)
print(round(dayup,2))