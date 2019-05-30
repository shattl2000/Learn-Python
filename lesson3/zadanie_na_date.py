# Вывести дату сегодня, вчера, месяц назад

from datetime import datetime, timedelta
dt_today = datetime.now()
delta_day = timedelta(days=1)
delta_month = timedelta(days=30)
dt_yesterday = dt_today - delta_day
dt_month_ago = dt_today - delta_month
print('Сегодня:', dt_today, 'Вчера:', dt_yesterday, 'Месяц назад:', dt_month_ago)

# Превратить строку "01/01/2017 12:10:03.234567" в объект datetime
from datetime import datetime
date_string = '01/01/2017 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%m/%d/%Y %H:%M:%S.%f')
print(date_dt)