import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the sleep data into a DataFrame
data = pd.read_csv('sleep-data.csv')

# Convert the nanoseconds timestamps to datetime
data['startTime'] = pd.to_datetime(data['startTimeNanos'], unit='ns')
data['endTime'] = pd.to_datetime(data['endTimeNanos'], unit='ns')

# Select the columns you need and filter by date
selected_columns = ['fitValue/0/value/intVal', 'dataTypeName', 'startTime', 'endTime']
selected_data = data[selected_columns]
selected_data = selected_data[selected_data['dataTypeName'] == 'com.google.sleep.segment']
selected_data = selected_data[selected_data['startTime'] >= '2021-04-01']

# Rename the columns
selected_data.columns = ['sleep_stage', 'data_type', 'start_time', 'end_time']

# Calculate the sleep duration in hours
selected_data['duration_hours'] = (selected_data['end_time'] - selected_data['start_time']).dt.total_seconds() / 3600

# Create a line plot of sleep duration over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=selected_data, x='start_time', y='duration_hours')
plt.title('Sleep duration over time')
plt.xlabel('Date')
plt.ylabel('Duration (hours)')

# Save the line plot as a PNG file
plt.savefig('sleep-duration-over-time.png')
plt.clf()

# Add a column for the day of the week
selected_data['day_of_week'] = selected_data['start_time'].dt.day_name()

# Create a box plot of sleep duration by day of the week
plt.figure(figsize=(9, 6))
sns.boxplot(data=selected_data, x='day_of_week', y='duration_hours')
plt.title('Sleep duration by day of the week')
plt.xlabel('Day of the week')
plt.ylabel('Duration (hours)')

# Save the box plot as a PNG file
plt.savefig('sleep-duration-by-day.png')
plt.clf()

# Create a histogram of sleep duration
plt.figure(figsize=(9, 6))
sns.histplot(data=selected_data, x='duration_hours')
plt.title('Distribution of sleep duration')
plt.xlabel('Duration (hours)')
plt.ylabel('Count')

# Save the histogram as a PNG file
plt.savefig('distribution-of-sleep-duration.png')
plt.clf()

# Create a scatter plot of bedtime vs. sleep duration
plt.figure(figsize=(9, 6))
sns.scatterplot(data=selected_data, x='start_time', y='duration_hours')
plt.title('Bedtime vs. sleep duration')
plt.xlabel('Bedtime')
plt.ylabel('Duration (hours)')

# Save the scatter plot as a PNG file
plt.savefig('sleep-duration-and-bedtime.png')
plt.clf()
