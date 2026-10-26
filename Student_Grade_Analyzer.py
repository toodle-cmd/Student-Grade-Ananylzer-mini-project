import pandas as pd 
import numpy as np

df = pd.read_csv('output_file.csv')

scores = df[["Maths","English","Science"]].values
df["Avg"] = np.mean(scores,axis=1)

df["status"] = np.where(df["Avg"] >=65 , "PASS" ,"FAIL")
print(df)
