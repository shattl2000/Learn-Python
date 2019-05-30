# Функция приводит два аргумента к целому числу  и считает их сумму, с импользованием try: except:
def get_summ(num_one, num_two):
	try:
		num_one = int(num_one)
		num_two = int(num_two)
		result = num_one + num_two
		return result
	except ValueError:
		return 'Проверте вводимые данные'

print(get_summ('dfsf',2))
