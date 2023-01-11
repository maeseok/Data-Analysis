import pandas as pd
import numpy as np

mpg = pd.read_csv('mpg.csv')
import seaborn as sns 
sns.boxplot(data=mpg, y='hwy')







"""
df = pd.DataFrame({'sex':[1,2,1,3,2,1],
                'score': [5,4,3,4,2,6]})
print(df['sex'].value_counts().sort_index())
print()
df['sex']=np.where(df['sex']==3, np.nan, df['sex'])
df['score']=np.where(df['score']>5, np.nan, df['score'])
df = df.dropna(subset=['sex','score']).groupby('sex').agg(mean_score=('score','mean'))
print(df)"""


