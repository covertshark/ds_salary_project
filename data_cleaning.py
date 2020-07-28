# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 12:12:44 2020

@author: Mohit.S
"""


import pandas as pd
df = pd.read_csv('glassdoor_jobs.csv')

#salary parsing (removing -1 charecters from salary column, removing glassdoor name from column)

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate']!= '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))

df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['min_salary'].dtype

df['avg_salary'] = (df.min_salary+df.max_salary)/2

#company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis =1)


#state field

df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#age of company

df['age'] = df.Founded.apply(lambda x: x if x <1 else 2020 -x)

#parsing of job description(python, etc.)

df['Job Description'][0]

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()

#r studio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() else 0) #or 'r-studio' in x.lower()
df.R_yn.value_counts()

#spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark_yn.value_counts()

#aws
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws_yn.value_counts()

#excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0) #or 'r-studio' in x.lower()
df.excel_yn.value_counts()

df.columns
df_out = df.drop('Unnamed: 0', axis =1)

df_out.to_csv('Salary_data_cleaned.csv', index = False)

pd.read_csv('Salary_data_cleaned.csv')