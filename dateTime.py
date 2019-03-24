import datetime as dt
dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)
answer_1 = dt_2 - dt_1
answer_2 = dt_3 + dt.timedelta(56)
answer_3 = dt_4 - dt.timedelta(seconds=3600)