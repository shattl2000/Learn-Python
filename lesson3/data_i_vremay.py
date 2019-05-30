from datetime import datetime
dt_now = datetime.now()
print(dt_now)

dt2 = datetime(2015, 5, 16, 8, 3, 44)
print(dt2)

delta = dt_now - dt2
print(delta)

dt3 = dt2 + delta
print(dt3)