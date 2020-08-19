# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 10:40:26 2020

@author: oppilas1
"""

import glassdoor_scraper as gs
import pandas as pd
path = 'C:\Users\oppilas1\Desktop\PietarKood\SentedexTutorials_started_03082020\second_data_analysis_project\chromedriver'

df = gs.get_jobs('data scientist', 15, False, path, 15)
