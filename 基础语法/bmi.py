height,weight = eval(input("请输入身高(米)和体重(公斤)[用逗号隔开]："))
bmi = weight/pow(height,2)
print("BMI指数为：{:.2f}".format(bmi))
international,domestic = "",""
if bmi < 18.5:
    international = "偏瘦"
    domestic = "偏瘦"
elif 18.5 <= bmi <24:
    international = "正常"
    domestic = "正常"
elif 24 <= bmi <25:
    international = "正常"
    domestic = "偏胖"
elif 25 <= bmi <28:
    international = "偏胖"
    domestic = "偏胖"
elif 28 <= bmi <30:
    international = "偏胖"
    demostic = "偏胖"
elif bmi >= 30:
    international = "肥胖"
    demostic = "肥胖"
print("BMI指标为:国际'{0}',国内'{1}'".format(international,domestic))