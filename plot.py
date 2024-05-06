import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')

wait_time = df['Average Wait Time']
num_flights = df['Flights']

for i in range(num_flights.min(), num_flights.max() + 1):
    wait_times = wait_time[num_flights == i]
    plt.boxplot(wait_times, positions=[i], widths=0.6)

plt.xlabel('Number of Flights')
plt.ylabel('Average Wait Time')
plt.title('Average Wait Time vs Number of Flights')
plt.savefig('plots/wait time vs num flights.png')
plt.clf()

num_passengers = df['Total Passengers']

# Chunk the number of passengers into 10 bins
# For each bin, plot a boxplot of the average wait time
num_bins = 10
bin_size = num_passengers.max() / num_bins
for i in range(num_bins):
    wait_times = wait_time[(num_passengers >= i * bin_size) & (num_passengers < (i + 1) * bin_size)]
    plt.boxplot(wait_times, positions=[i], widths=0.6)

plt.xlabel('Number of Passengers (binsize = ' + str(bin_size) + ')')
plt.ylabel('Average Wait Time')
plt.title('Average Wait Time vs Number of Passengers')
plt.savefig('plots/wait time vs num passengers.png')
plt.clf()

time_of_day = df['Hour']

# plot the median wait time for each hour of the day
# hours are formatted like 1200-1300, etc
median_wait_times = []
for i in range(24):
    wait_times = wait_time[time_of_day == str(i).zfill(2) + '00 - ' + str(i + 1).zfill(2) + '00']
    median_wait_times.append(wait_times.median())

plt.plot(range(24), median_wait_times)
plt.xlabel('Hour of the Day')
plt.ylabel('Median Wait Time')
plt.title('Median Wait Time vs Hour of the Day')
plt.savefig('plots/median wait time vs hour of the day.png')