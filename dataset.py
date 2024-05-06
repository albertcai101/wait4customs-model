import pandas as pd
import glob as glob

column_names = ["Airport", "Terminal", "Date", "Hour", "Citizen Avg Wait Time", "Citizen Max Wait Time", "Non citizen Avg Wait Time", "Non citizen Max Wait Time", "Average Wait Time", "Max Wait Time", "Num Passengers Q1", "Num Passengers Q2", "Num Passengers Q3", "Num Passengers Q4", "Num Passengers E1", "Num Passengers E2", "Num Passengers E3", "Excluded Passengers", "Total Passengers", "Flights"]

path = "AWT/*.xls"
files = glob.glob(path)
data = pd.DataFrame()
for file in files:
    dfs = pd.read_html(file)
    df = pd.DataFrame(dfs[0].values)
    df = df.iloc[:, :-1]
    data = pd.concat([data, df])
    print("Processed: ", file)
data.columns = column_names

# sort by airport, then terminal, then date, then hour
data = data.sort_values(by=["Airport", "Terminal", "Date", "Hour"])

data.to_csv("all_airports.csv", index=False)
