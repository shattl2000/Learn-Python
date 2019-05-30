#  Пример функции деления пирога с импользованием try: except:
def cut_cake(parts):
	try:
		return 1/int(parts)
	except (ZeroDivisionError, TypeError, ValueError):
		return 'Проверьте введеные данные'

cake = cut_cake(input())
print(cake)