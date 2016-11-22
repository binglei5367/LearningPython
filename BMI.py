
# -*- coding: utf-8 -*-

weight = float(input(输入你的体重（/kg）：))
height = float(input(输入你的身高（/cm）：))
BMI = weight/(height*height)

if BMI <= 18.5 :
	print('你的BMI值为%.1f，你tm怎么这么轻' %BMI)
elif 18.5 < BMI <= 25 :
	print('你的BMI值为%.1f，瘦鸡' %BMI)
elif 25 < BMI <=28 :
	print('你的BMI值为%.1f，肉肉' %BMI)
else :
	print('肥佬')