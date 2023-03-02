import pandas as pd
from datetime import datetime, timedelta
import random

class DatasetGenerator:
  def __init__(self,datasetSize):
        # Start and end dates
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 12, 31)

        # Number of rows to generate
        num_rows = datasetSize

        # Create a list of dates by repeating the date range multiple times
        date_range = pd.date_range(start=start_date, end=end_date, freq='D')
        dates = [d for d in date_range for _ in range(num_rows//len(date_range) + 1)]
        dates = dates[:num_rows]

        # Convert the list of dates to a dataframe and add a "Date" column
        df = pd.DataFrame(dates, columns=['Date'])
        # Get the year, month, and day
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month
        df['Day'] = df['Date'].dt.day

        # Add the "Item" column
        for i, row in df.iterrows():
            month = row["Month"]
            
            if month in range(1,5):
                if random.random() < 0.95:
                    df.at[i, "Item"] = 1
                else:
                    df.at[i, "Item"] = random.choice([2, 3])
            elif month in range(5, 9):
                if random.random() < 0.95:
                    df.at[i, "Item"] = 2
                else:
                    df.at[i, "Item"] = random.choice([1, 3])
            else:
                if random.random() < 0.95:
                    df.at[i, "Item"] = 3
                else:
                    df.at[i, "Item"] = random.choice([1, 2])

        # Ensure that the "Item" column values are integers
        df["Item"] = df["Item"].astype(int)
        df.to_csv('dataset/dataset.csv', index=False)
        print("Generated and Saved")
        
