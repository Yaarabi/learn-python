
import numpy as np
import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
tables = pd.read_html(URL)

# from the URL we have 4 tables
# we need the 4th table which contains the GDP data
df = tables[3] 

# remplace the first row (header of the table ) to nambered columns
df.columns = range(df.shape[1])

# select only the columns we need
df = df[[0,2]]

# select the 10 rows and let the columns
df = df.iloc[1:11,:]

# rename the columns
df.columns = ['Country','GDP (Million USD)']

# Change the data type of the 'GDP (Million USD)' column to integer. Use astype() method.
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)

# Convert the GDP value in Million USD to Billion USD
df[['GDP (Million USD)']] = df[['GDP (Million USD)']]/1000

# # Use numpy.round() method to round the value to 2 decimal places. after cama keep just two numbers
df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']], 2)

# # Rename the column header from 'GDP (Million USD)' to 'GDP (Billion USD)'
df.rename(columns = {'GDP (Million USD)' : 'GDP (Billion USD)'})

df.to_csv('10_larges_economics.csv', index=False)