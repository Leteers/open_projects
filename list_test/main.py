# import pandas as pd
# from datetime import datetime, timezone

# def time_conv(time):
#     date_str_fixed = time.replace("+00", "+0000")

#     # Parse and convert to timestamp
#     dt = datetime.strptime(date_str_fixed, "%Y/%m/%d %H:%M:%S%z")
#     timestamp = int(dt.timestamp())
#     return timestamp

# # df = pd.read_csv('/Users/leteers/Desktop/development/db/Т512КВ05_r.xlsx')
# from io import BytesIO


# df = pd.read_excel('/Users/leteers/Desktop/development/db/Т512КВ05_r.xlsx', skiprows=2)

# df = df.rename(columns={
#     "Время пакета (GMT)": "timestamp",
#     "Широта": "lat",
#     "Долгота": "lon"
# })


# df["timestamp"] = pd.to_datetime(df["timestamp"], format="%d.%m.%Y %H:%M:%S", errors='coerce')
# df["timestamp"] = df["timestamp"].astype("int64") // 10 ** 9
# df = df[(df["lat"] >= -90) & (df["lat"] <= 90) & (df["lon"] >= -180) & (df["lon"] <= 180)]
# df.to_csv('/Users/leteers/Desktop/development/db/Perfect_circle.csv')


a = ['a','b','c']

print(a.index('a'))

a = 'slosa_salsa'

ans = ' '.join([str.upper(_[0]) + _[1:len(_)] for _ in a.split('_')])

print(ans)
# a = {'a': 1, 'b': 2}
# print(a.keys())
# print(a:=dict(reversed(sorted(a.items(),key = lambda item: item[1]))))
# print(a.keys())
# a = ['asd','123']
# str.join()
# str.upper()
# # len(s.keys())

# from typing import List, Dict
# def solution(s1: str, s2: str) -> bool:
#     dic = {}
#     if len(s1) !=len(s2):
#         return False 
#     else:
#         for i in range(len(s1)):
#             dic[s1[i]] = dic[s2[i]]
#     if len(dic. keys ()) == len(set (s1)):
#         return True 
#     else:
#         return False
    
# print(solution('paper','tittle'))
# # use stdout to debug

# df = pd.read_csv('track_points.csv')
# df['timestamp'] = df['timestamp'].apply(lambda x: time_conv(x))
# df.to_csv('track_points.csv')
# print(df['timestamp'])
# # Convert to timestamp
