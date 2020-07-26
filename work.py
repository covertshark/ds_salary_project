# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 22:12:54 2020

@author: Mohit.S
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/KIIT/Documents/ds_salary_project/chromedriver"

df= gs.get_jobs('data scientist', 15, False, path, 15)

df.to_csv('glassdoor_jobs.csv', encoding='utf-8')