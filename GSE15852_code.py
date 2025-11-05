# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 16:44:47 2025

@author: jessi
"""

import pandas as pd 

 

# Load the excel file  

df = pd.read_excel("C:/Users/jessi/OneDrive/Desktop/GSE15852.xlsx") 

 

# Filter genes with adjusted p-value < 0.05 and log2 fold change > 1 

filtered_df = df[(df['adjPVal'] < 0.05) & (df['logFC'].abs() >= 1)] 

 

# Sort by absolute logFC (strongest change first) 

top_250 = filtered_df.reindex(filtered_df['logFC'].abs().sort_values(ascending=False).index).head(250) 