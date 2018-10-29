import pandas as pd
import seaborn as sns

bakery_df = pd.read_csv("C:\\Users\\Tyson\\PycharmProjects\\StatsInterpreter\\data\\BreadBasket_DMS.csv")

print(bakery_df.Item.value_counts(sort=False))

hot_chocolate_sales = bakery_df.loc[bakery_df['Item']=="Coffee"]

print(hot_chocolate_sales.Item.value_counts(sort=False))

hot_chocolate_daily = hot_chocolate_sales.Date.value_counts().sort_index()

print(hot_chocolate_daily)

date_index = pd.date_range('10-30-2016', '04-09-2017')

hot_chocolate_daily.index = pd.DatetimeIndex(hot_chocolate_daily.index)

hot_chocolate_daily = hot_chocolate_daily.reindex(date_index, fill_value=0)

ax_daily = hot_chocolate_daily.plot()

rolling = hot_chocolate_daily.rolling(7, min_periods=1).mean()

rolling.plot(ax=ax_daily)
