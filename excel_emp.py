import pandas as pd
from datetime import datetime, timedelta

def read_attendance_data(file_path):

    df = pd.read_excel(file_path)
    print(df)
    return df

def count_attendance_today(df):
    current_date = datetime.now().strftime('%b %d')
    wfh_count = df[df[current_date] == 'WFH']['Emp ID'].count()
    wfo_count = df[df[current_date] == 'WFO']['Emp ID'].count()
    abt_count_current = df[current_date].isna().sum()
    return wfh_count, wfo_count, abt_count_current

def count_attendance_previous_days(df):
    previous_5_dates = [(datetime.now() - timedelta(days=i)).strftime('%b %d') for i in range(1, 6)]
    wfh_count_prev = 0
    wfo_count_prev = 0
    abt_count_prev = 0
    for prev_date in previous_5_dates:
        if prev_date in df.columns:
            wfh_count_prev += df[df[prev_date] == 'WFH']['Emp ID'].count()
            wfo_count_prev += df[df[prev_date] == 'WFO']['Emp ID'].count()
            abt_count_prev += df[prev_date].isna().sum()
    return wfh_count_prev, wfo_count_prev, abt_count_prev

file_path = 'excel_data.xlsx'
df = read_attendance_data(file_path)

wfh_today, wfo_today, nan_today = count_attendance_today(df)
print(f"WFH Count for today: {wfh_today}")
print(f"WFO Count for today: {wfo_today}")
print(f"Employee IDs who are absent on the current day: {nan_today}")

wfh_prev, wfo_prev, abt_prev = count_attendance_previous_days(df)
print(f"WFH Count for the previous 5 days: {wfh_prev}")
print(f"WFO Count for the previous 5 days: {wfo_prev}")
print(f"Employee IDs who haven't filled attendance in the previous 5 days: {abt_prev}")




































































































