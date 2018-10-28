import pandas as pd
import seaborn as sb
from io import StringIO

scotch_df = pd.read_csv("C:\\Users\\Tyson\\PycharmProjects\\StatsInterpreter\\data\\scotch_review.csv")

print(scotch_df.score.mean())
print(scotch_df.score.value_counts(sort=False))
print(scotch_df.price.value_counts(sort=False))


cleaned_df = scotch_df[scotch_df.price.apply(lambda x: x.isnumeric())]

print(cleaned_df.score.value_counts(sort=False))
print(cleaned_df.price.value_counts(sort=False))

cleaned_df = cleaned_df.sort_values(by=['price'])

sb.regplot('price', 'score', data=cleaned_df)