def bmi(weight, height):
	return round((weight / ((height/100)**2)), 2)

print(bmi(83, 178))
print(bmi(51, 158))
print(bmi(30, 144))