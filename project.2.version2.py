import requests
import csv
from time import sleep
import matplotlib.pyplot as plt


#Stage 1 :Download the dataset with Python:

data = requests.get('https://corgis-edu.github.io/corgis/datasets/csv/weather/weather.csv')


#Stage 2 :Write data to a file in your system:
with open('weather.csv','wb') as csvfile :
    csvfile.write(data.content)

#ُStage 3 :Read data from saved file:
with open('weather.csv','r') as csvfile:
    data_reader = csv.DictReader(csvfile)
    data_reader_list = list(data_reader)

#Stage 4 :Calculate average of fields:
total_avg_temp = 0
total_max_temp = 0 
total_min_temp = 0
total_wind_direction = 0
total_wind_speed = 0
count = len(data_reader_list)

for row in data_reader_list :
    total_avg_temp += float(row["Data.Temperature.Avg Temp"])
    total_max_temp += float(row["Data.Temperature.Max Temp"])
    total_min_temp += float(row["Data.Temperature.Min Temp"])
    total_wind_direction += float(row["Data.Wind.Direction"])
    total_wind_speed += float(row["Data.Wind.Speed"])

avg_avg_temp = total_avg_temp / count
avg_max_temp = total_max_temp / count
avg_min_temp = total_min_temp / count
avg_wind_direction = total_wind_direction / count
avg_wind_speed = total_wind_speed / count

#Stage 5 :Printing the results:
print("Average of Avg Temp:", avg_avg_temp)
print("Average of Max Temp:", avg_max_temp)
print("Average of Min Temp:", avg_min_temp)
print("Average of Wind Direction:", avg_wind_direction)
print("Average of Wind Speed:", avg_wind_speed)

#Stage 6 :Making plots :
dates = [row["Date.Full"] for row in data_reader_list]
avg_temps = [float(row["Data.Temperature.Avg Temp"]) for row in data_reader_list]
max_temps = [float(row["Data.Temperature.Max Temp"]) for row in data_reader_list]
min_temps = [float(row["Data.Temperature.Min Temp"]) for row in data_reader_list]
wind_directions = [float(row["Data.Wind.Direction"]) for row in data_reader_list]
wind_speeds = [float(row["Data.Wind.Speed"]) for row in data_reader_list]

plt.plot(dates, avg_temps, label='Average Temperature')
plt.plot(dates, max_temps, label='Maximum Temperature')
plt.plot(dates, min_temps, label='Minimum Temperature')
plt.plot(dates, wind_directions, label='Wind Direction')
plt.plot(dates, wind_speeds, label='Wind Speed')

plt.xlabel('Date')
plt.ylabel('Values')
plt.title('Weather Data')
plt.legend()

x = input("Do you want to get the plots? (answer with y or n): ")
while True:
    if x == "y":
        plt.show()
        break
    elif x == "n":
        break
    else:
        print("The command is not correct! Try again.")
        x = input("Do you want to get the plots? (answer with y or n): ")


#------------------------------The End...  -----------------------------------

sleep(3)
print("Parham Code")

