import pandas as pd


df = pd.read_json("Pandas\dummy_json_data.json")

# df = pd.read_csv("output.csv")
print("display the info of data set")

print(df.info())