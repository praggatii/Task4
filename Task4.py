import pandas as pd
from calendar import monthrange

# Load the uploaded CSV file to examine its structure
file_path = '/home/priyapragati/Downloads/Daily_Station_Report_TOTALISER_24 (9).csv'
data = pd.read_csv(file_path)

# Rename the column "Unit" to "KPI Name"
data.rename(columns={"Unit": "KPI Name"}, inplace=True)

# Filter the first three rows of the specified KPI Name
filtered_data = data[data['KPI Name'].isin([
    "TG-1 (Steam Totalizer)", 
    "TG-2 (Steam Totalizer)", 
    "TG-3 (Steam Totalizer)"
])].copy()  # Use .copy() to avoid the SettingWithCopyWarning

# Rename the filtered KPI Names to "Specific Steam Consumption"
filtered_data.loc[:, 'KPI Name'] = "Specific Steam Consumption"

# Melt the DataFrame to transform day columns into rows
transformed_data = pd.melt(
    filtered_data,
    id_vars=["Date", "KPI Name"],
    value_vars=[col for col in data.columns if "Day" in col],  # Select day columns
    var_name="Day",
    value_name="Value"
)

# Merge Day and Date columns into a single column in the desired format
def merge_date_day(row):
    # Extract day number and month abbreviation
    day_number = int(row['Day'].replace("Day", ""))
    month_name = row['Date'].split('-')[0][:3]  # Abbreviate the month

    # Standardize and convert to datetime
    month_year = pd.to_datetime(f"{month_name}-{row['Date'].split('-')[1]}", format="%b-%y")

    # Adjust day number if it exceeds the last day of the month
    last_day = monthrange(month_year.year, month_year.month)[1]
    day_number = min(day_number, last_day)

    # Return formatted date
    return month_year.replace(day=day_number).strftime("%d-%m-%Y")

# Apply the function to merge the day and date columns
transformed_data['Date'] = transformed_data.apply(merge_date_day, axis=1)

# Drop the original Day column
transformed_data = transformed_data.drop(columns=["Day"])

# Save the processed data to a new CSV file
output_file_path = '/home/priyapragati/Downloads/Transformed_Station_Report.csv'
transformed_data.to_csv(output_file_path, index=False)

output_file_path
