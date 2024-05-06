import pandas as pd

# Load the data
df = pd.read_csv('dataset.csv')

# Ensure 'Date' is a datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Extract month and day of month
df['Month'] = df['Date'].dt.month
df['Day of Month'] = df['Date'].dt.day

# Remove the original 'Date' column
df.drop('Date', axis=1, inplace=True)

# Define the new column order with 'Month' and 'Day of Month' as the third and fourth columns
new_column_order = ['Airport', 'Terminal', 'Month', 'Day of Month', 'Hour', 'Citizen Avg Wait Time', 'Citizen Max Wait Time', 
                    'Non citizen Avg Wait Time', 'Non citizen Max Wait Time', 'Average Wait Time', 'Max Wait Time', 
                    'Num Passengers Q1', 'Num Passengers Q2', 'Num Passengers Q3', 'Num Passengers Q4', 
                    'Num Passengers E1', 'Num Passengers E2', 'Num Passengers E3', 'Excluded Passengers', 
                    'Total Passengers', 'Flights']

# Reorder the DataFrame according to new_column_order
df = df[new_column_order]

df['Hour'] = df['Hour'].str.split(' - ').str[0].astype(int) // 100  # Converts "1300 - 1400" to "13"

# Save the updated dataset to a new CSV file
df.to_csv('updated_dataset.csv', index=False)

print("Dataset updated with Month and Day of Month as the third and fourth columns.")