import pandas as pd

# Load the data from the CSV file
data = pd.read_csv('sleep-data.csv')

# Convert the nanoseconds timestamps to datetime
data['startTime'] = pd.to_datetime(data['startTimeNanos'], unit='ns')
data['endTime'] = pd.to_datetime(data['endTimeNanos'], unit='ns')

# Select the columns you need
selected_columns = ['fitValue/0/value/intVal', 'dataTypeName', 'startTime', 'endTime']
selected_data = data[selected_columns]

# Filter by dataTypeName
selected_data = selected_data[selected_data['dataTypeName'] == 'com.google.sleep.segment']

# Rename the columns
selected_data.columns = ['sleep_stage', 'data_type', 'start_time', 'end_time']

# Print the selected data
print(data.columns)
print('\n\n')
print(selected_data)

