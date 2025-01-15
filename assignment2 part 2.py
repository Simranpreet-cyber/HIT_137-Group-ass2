import glob
import os 
import pandas as pd 

path="C:\\Users\\mehak\\OneDrive\\Desktop\\my documents\\temperature_data"
all_files = glob.glob(os.path.join(path,"*.csv"))

for file in all_files:
    file_name=os.path.splitext(os.path.basename(file))[0]
    df=pd.read_csv(file)
    df['ADELAIDE-KENT-TOWN']= df['STATION_NAME']+ str(df['STN_ID'])
    df.to_csv(file_name)
    print(df.to_string())


def get_season(month):
    if month in ["December", "January", "February"]:
        return "Summer"
    if month in ["March", "April", "May"]:
        return "Autumn"
    if month in ["June", "July", "August"]:
        return "Winter"
    if month in ["September", "October", "November"]:
        return "Spring"
      

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

data_frame=[]

for month in months:
    temporary_df = df[['STATION_NAME', 'STN_ID', 'LAT', 'LON']].copy()
    temporary_df['Month'] = month
    temporary_df['Temperature'] = df[month]
    temporary_df['Season'] = get_season(month)

    data_frame.append(temporary_df)

df_all=pd.concat(data_frame, ignore_index=True)

monthly_avg_temp = df_all.groupby('Month')['Temperature'].mean()
seasonal_avg_temp = df_all.groupby('Season')['Temperature'].mean()

print("Monthly Average Temperatures:")
print(monthly_avg_temp)
print("\nSeasonal Average Temperatures:")
print(seasonal_avg_temp)

df_range = df_all.groupby(['STATION_NAME', 'STN_ID'])['Temperature'].agg(['max', 'min'])
df_range['Temperature_Range'] = df_range['max'] - df_range['min']
largest_temp_range_station = df_range[df_range['Temperature_Range'] == df_range['Temperature_Range'].max()]

print("Station(s) with the largest temperature range:\n")
print(largest_temp_range_station.to_string())

with open("largest_temp_range_station.txt", "w") as f:
    f.write("Station(s) with the largest temperature range:\n")
    f.write(largest_temp_range_station.to_string())

df_avg_temp = df_all.groupby(['STATION_NAME', 'STN_ID'])['Temperature'].mean()
warmest_station = df_avg_temp[df_avg_temp == df_avg_temp.max()]
coolest_station = df_avg_temp[df_avg_temp == df_avg_temp.min()]

print("Warmest station(s):\n")
print(warmest_station.to_string())
print("\n\nCoolest station(s):\n")
print(coolest_station.to_string())

         
with open("warmest_and_coolest_station.txt", "w") as f:
    f.write("Warmest station(s):\n")
    f.write(warmest_station.to_string())
    f.write("\n\nCoolest station(s):\n")
    f.write(coolest_station.to_string())

with open("average_temprature.txt", "w") as f:
    f.write("Monthly Average Temperatures:")
    f.write(monthly_avg_temp.to_string())
    f.write("\nSeasonal Average Temperatures:")
    f.write(seasonal_avg_temp.to_string())