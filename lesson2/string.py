# Функция сравнения строк, если аргументы не являются строками выводится 0,
# Если строки одинкаовые 1, если разные и первая длиннее 2, если разные и вторая строка learn 3

def func_string(str1, str2):
	if type (str1) != type ('str') and type (str2) != type ('str'):
		return "0"
	elif str1 == str2:
		return "1"
	elif len(str1) > len(str2):
		return "2"
	elif str2 == 'learn':
		return "3"
	else:
		return str1 + ' ' + str2
input_string = func_string('learn', 'python')
print (input_string)