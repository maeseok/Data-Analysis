import pandas as pd
import numpy as np
#df = pd.DataFrame({'name':['김지훈','이유진','박동현','김민지'],'english':[90,80,60,70],'math':[50,60,100,20]})
#print(sum(df['english']))

#첫 번째 행을 변수명이 아닌 데이터로 인식해 불러오고, 변수명은 0부터 시작하는 숫자로 자동 지정
df_exam = pd.read_excel('excel_exam.xlsx', header=None)
#시트네임이 여러 개라면 sheet_name=2 -> 세 번째 시트 가져옴
#print(df_exam)

df_csv_exam = pd.read_csv('exam.csv')
#print(df_csv_exam)

df_midterm = pd.DataFrame({'english':[90,80,60,70], 'math':[50,60,100,20], 'nclass':[1,1,2,2]})
df_midterm.to_csv("output_newdata.csv", index=False)
df_midterm['sum']=df_midterm['english']+df_midterm['math']
#print(df_midterm)
df_midterm['test']=np.where(df_midterm['sum']>=140,'pass','fail')
#print(df_midterm)
count_test=df_midterm['test'].value_counts().sort_index()
count_test.plot()