def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 400 == 0 and year % 3200 != 0:
        return True
        
print(is_leap(2008))
print(is_leap(2018))
print(is_leap(2000))