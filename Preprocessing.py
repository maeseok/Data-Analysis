import pandas as pd
exam = pd.read_csv('exam.csv')
#test=exam.query('nclass==1 | nclass==3 | nclass==5')
#print(test['math'].mean())

#print(exam[['nclass','math','english']])
#print(exam.drop(columns='math'))
#print(exam.query('nclass==1')['english'])
#print(exam.query('math>=50')[['id','math']].head(5))

#print(exam.sort_values(['nclass', 'math'], ascending=[True,False]))
#print(exam.assign(total=exam['math']+exam['english']).sort_values('total'))
#print(exam.agg(mean_math=('math', 'mean')))
#print(exam.groupby('nclass').agg(mean_math=('math', 'mean')))
test1= pd.DataFrame({'id':[1,2,3,4,5],
                     'test':[60,80,70,90,85]})
test2 = pd.DataFrame({'id':[1,2,3,4,5],
                      'test':[70,83,65,95,80]})
#print(pd.merge(test1, test2, how='left', on='id'))
group = pd.concat([test1,test2])
print(group) 