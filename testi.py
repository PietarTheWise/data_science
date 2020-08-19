# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 12:18:01 2020

@author: oppilas1
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

#salary parsing
#Company name text only
#state field
#age of company
#parsing of job description (python, etc)

df = df[df['Salary Estimate'] != '-1']

df