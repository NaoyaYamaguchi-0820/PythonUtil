import os
import datetime

todayString = datetime.date.today()
todayString = todayString.strftime('%Y%m%d')

os.mkdir(todayString)
