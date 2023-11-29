import pandas as pd
file = 'california_housing_train.csv'
df = pd.read_csv(file)

avg = (df.loc[df.population < 500, 'median_house_value'].mean())
print(avg)
