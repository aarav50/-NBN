A=0
import csv
import pandas as pd
import plotly.express as px
import statistics
q =0
df=pd.read_csv("aarav.csv")
data=df["female"].toList()
data1=df["quant_saved"].toList()
fig=px.scatter(x=data,y=data1)
fig.show()

for q in randge(1,len(data)):
  print(data[A]+"the mean medain mode abd stdev are"+statistics.mean(data1[a])+statistics.medain(data1[a])+statistics.mode(data1[a])+statistics.stdev(data1[a])) 
  A=A+1