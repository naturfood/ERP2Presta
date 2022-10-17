import os

import pandas as pd

path="d:/urunler/"

data=pd.read_excel(path+"Artikel.xlsx")

for i in range(0,len(data)):
    print(i,data.loc[i][1],data.loc[i][0])