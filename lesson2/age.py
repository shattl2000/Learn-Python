# Функция определяет по возрасту чем должен заниматься человек

print("Введите ваш возраст")
age = int(input())

def user_age(age):
	if age < 0:
		return "Не родился"
	elif age <= 6:
		return "Ходит в сад"
	elif age <= 16:
		return "Ходит в школу"
	elif age <= 23:
		return "Ходит в универ"
	elif age <= 65:
		return "Работает"
	else:
		return "Не известно, что делает"
result = user_age(age)
print(result)