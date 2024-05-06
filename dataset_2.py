import pandas as pd

# Load the data
df = pd.read_csv('dataset.csv')

# Define all possible hour ranges
hour_ranges = [f"{str(i).zfill(2)}00 - {str(i + 1).zfill(2)}00" for i in range(24)]

# Ensure the data type for 'Date' is appropriate
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%m/%d/%Y')

# Group by 'Airport', 'Terminal', 'Date' and then apply a custom function to handle missing hours
def fill_missing_hours(group):
    existing_hours = set(group['Hour'])
    missing_hours = set(hour_ranges) - existing_hours
    missing_data = []
    for hour in missing_hours:
        # Create a row with all zeros for missing hours
        missing_data.append({
            'Airport': group['Airport'].iloc[0],
            'Terminal': group['Terminal'].iloc[0],
            'Date': group['Date'].iloc[0],
            'Hour': hour,
            'Citizen Avg Wait Time': 0,
            'Citizen Max Wait Time': 0,
            'Non citizen Avg Wait Time': 0,
            'Non citizen Max Wait Time': 0,
            'Average Wait Time': 0,
            'Max Wait Time': 0,
            'Num Passengers Q1': 0,
            'Num Passengers Q2': 0,
            'Num Passengers Q3': 0,
            'Num Passengers Q4': 0,
            'Num Passengers E1': 0,
            'Num Passengers E2': 0,
            'Num Passengers E3': 0,
            'Excluded Passengers': 0,
            'Total Passengers': 0,
            'Flights': 0
        })
    # Concatenate missing data with the group
    if missing_data:
        missing_df = pd.DataFrame(missing_data)
        return pd.concat([group, missing_df], ignore_index=True)
    return group

# Apply the function to each group
complete_df = df.groupby(['Airport', 'Terminal', 'Date']).apply(fill_missing_hours).reset_index(drop=True)

# Reformat date to YYYY-MM-DD
complete_df['Date'] = pd.to_datetime(complete_df['Date']).dt.strftime('%Y-%m-%d')

# Sort the DataFrame again to make it orderly
complete_df.sort_values(by=['Airport', 'Terminal', 'Date', 'Hour'], inplace=True)

# Save the filled dataset to a new CSV file
complete_df.to_csv('filled_dataset.csv', index=False)