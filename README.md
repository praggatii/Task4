# Task4
# Steam Totalizer Data Transformation

This repository contains the script and the processed data for transforming and analyzing steam totalizer data from a daily report.

## Overview

The script in this repository processes a dataset from a daily station report, filtering and transforming data related to steam totalizers into a format that is more suitable for further analysis.

Key transformations include:
- Filtering specific units (TG-1, TG-2, TG-3).
- Reshaping data by converting day-wise columns into rows.
- Merging the date and day columns into a specific date format (DD-MM-YYYY).

The processed data is saved in a new CSV format and is available for download.

## Project Structure

- **Task4.py**: Python script that loads the original dataset, processes it, and generates the transformed CSV file.
- **Daily_Station_Report_TOTALISER_24 (9).csv**: Original raw data (uploaded by the user).
- **Transformed_Station_Report.csv**: Processed data after transformation (output file).

## Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/steam-totalizer-data-transformation.git
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure you have Python 3.x and the following libraries installed:
pandas
numpy

4. Data Description
Date: The date of the report in the format DD-MM-YYYY.
KPI Name: Unit names (e.g., TG-1, TG-2, TG-3) transformed into "Specific Steam Consumption".
Day: Day number (Day 1, Day 2, Day 3).
Value: Corresponding values for each day.






#DataScience #DataTransformation #SteamTotalizer #CSVProcessing #Pandas #Python #DataCleaning #DataWrangling #KPIAnalysis #EnergyAnalysis #MachineLearning #BigData
