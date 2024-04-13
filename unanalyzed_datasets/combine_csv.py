import pandas as pd

# List of CSV files to combine
csv_files = [
    "./dataset/raw_scrape.csv",
    "./dataset/1403-1553.csv",
    "./dataset/1554-1665.csv",
    "./dataset/1666-1800.csv",
    "./dataset/1801-2300.csv",
    "./dataset/2301-2700.csv",
    "./dataset/2701-2800.csv"
]

# Initialize an empty list to store dataframes
dfs = []

# Read each CSV file and append to the list
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    dfs.append(df)

# Concatenate all dataframes in the list
final_df = pd.concat(dfs, ignore_index=True)

# Save the combined dataframe to a new CSV file
final_df.to_csv("final_raw.csv", index=False)

print("All files combined and saved as final_raw.csv!")
