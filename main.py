import pandas as pd

wine_df = pd.read_csv("C:\\Users\\Tyson\\PycharmProjects\\StatsInterpreter\\data\\winemag-data-130k-v2.csv")

print(wine_df.points.mean())