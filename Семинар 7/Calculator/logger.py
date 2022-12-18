from datetime import datetime as dt
from time import time


def numbers_logger(data):
    a, b, c, d = data
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a') as file:
        file.write(f'{time}; {a} {c} {b} = {d}\n')
