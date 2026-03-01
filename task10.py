import pandas as pd

df = pd.read_json('data.json')
print(df.head(7))
print(df.tail(7))