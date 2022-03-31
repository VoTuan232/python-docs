import pandas
import numpy as np
import matplotlib.pyplot as plt
import csv

phantabear=pandas.read_csv("phantabear.csv")
start=0
end=19

while end<=(len(phantabear)-1):
	
	ethPrice='contract_0x67D9417C9C3c250f61A83C7e8658daC487B56B09.ethPrice'
	outlier='outlier'
	past_20_transactions=phantabear.loc[start:end,:]
	current_data=phantabear.loc[end,ethPrice]
	print(current_data)
	Q1,Q3=np.percentile(past_20_transactions.loc[:,ethPrice],[25,75])
	IQR=Q3-Q1
	Upper_bound=Q3+IQR*1.5
	Lower_bound=Q1-IQR*1.5

	if current_data<Lower_bound:
		phantabear.loc[end,outlier]="true"

	start=start+1
	end=end+1

phantabear.to_csv('phantabear_outlier_flag.csv')