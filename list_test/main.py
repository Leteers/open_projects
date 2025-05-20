import pandas as pd
from datetime import datetime, timezone

def time_conv(time):
    date_str_fixed = time.replace("+00", "+0000")

    # Parse and convert to timestamp
    dt = datetime.strptime(date_str_fixed, "%Y/%m/%d %H:%M:%S%z")
    timestamp = int(dt.timestamp())
    return timestamp

# df = pd.read_csv('/Users/leteers/Desktop/development/db/Т512КВ05_r.xlsx')
from io import BytesIO


df = pd.read_excel('/Users/leteers/Desktop/development/db/Т512КВ05_r.xlsx', skiprows=2)

df = df.rename(columns={
    "Время пакета (GMT)": "timestamp",
    "Широта": "lat",
    "Долгота": "lon"
})


df["timestamp"] = pd.to_datetime(df["timestamp"], format="%d.%m.%Y %H:%M:%S", errors='coerce')
df["timestamp"] = df["timestamp"].astype("int64") // 10 ** 9
df = df[(df["lat"] >= -90) & (df["lat"] <= 90) & (df["lon"] >= -180) & (df["lon"] <= 180)]
df.to_csv('/Users/leteers/Desktop/development/db/Perfect_circle.csv')



# df = pd.read_csv('track_points.csv')
# df['timestamp'] = df['timestamp'].apply(lambda x: time_conv(x))
# df.to_csv('track_points.csv')
# print(df['timestamp'])
# # Convert to timestamp
