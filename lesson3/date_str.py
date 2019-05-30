from datetime import datetime
date_string = '12/23/2010'
date_dt = datetime.strptime(date_string, '%m/%d/%Y')
print(date_dt)