import win32api
import win32con
import time

def update_time():
current_time = time.strftime('%H:%M:%S')
current_date = time.strftime('%m/%d/%Y')

win32api.SetSystemTime(int(current_date.split('/')[2]), int(current_date.split('/')[0]), 0, int(current_date.split('/')[1]), int(current_time.split(':')[2]), int(current_time.split(':')[1]), int(current_time.split(':')[0]), 0)

update_time()
