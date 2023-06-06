import pandas as pd
import pyreadstat

# Read the .sav file
df, meta = pyreadstat.read_sav('data.sav')

# Write the DataFrame to an Excel file
df.to_excel('data.xlsx', index=False)
