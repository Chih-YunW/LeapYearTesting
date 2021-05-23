def leapYear(year):
	if (year%4) != 0:
		return "It is not a leap year"
	else:
		if(year%100) != 0:
			return "It is a leap year"
		else:
			if(year%400) == 0:
				return "It is a leap year"
			else:
				return "It is not a leap year"
