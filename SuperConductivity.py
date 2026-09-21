import pandas as pd
import matplotlib.pyplot as plt
import os
import kagglehub

path = kagglehub.dataset_download("munumbutt/superconductor-dataset")
for f in os.listdir(path):
    print(f)

df = pd.read_csv(os.path.join(path, "train.csv"))  # filename may differ, check the listing above

print(df.shape)
print(df.head())
print(df.info())
print(df.isna().sum())
print(df.duplicated().sum())
print(df.describe())
df.hist(figsize=(20, 20))
plt.show()
print(df.corr())