from datetime import date, timedelta #импротрируем модуль
dt = date(2000, 1, 1) #задали дату в переменную dt
#print (dt)
delta = timedelta(days=1)  #задали переменную delta, которая равна изменению на 1 день
#print(delta)
dt2 = dt - delta #задали переменную dt2, которая меньше заданной даты на delta(1 день)
print(dt2)
dt3 = dt + delta #задали переменную dt3, которая больше заданной даты на delta(1 день)
print(dt3)
