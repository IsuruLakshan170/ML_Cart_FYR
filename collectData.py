
import pandas as pd

class dataStore:
    def __init__(self, rows, cols):
        self.arr = [[None for j in range(cols)] for i in range(rows)]
        
    def fill_data(self):
        i = 0
        while i < len(self.arr):
            date = int(input("Enter date: "))
            item =int(input("Enter item: "))

            self.arr[i][0] = date
            self.arr[i][1] = item
            i += 1
         # Convert the array to a Pandas DataFrame
            datafram = pd.DataFrame(self.arr, columns=["date", "item"])
    
        return datafram["date"],datafram["item"]

