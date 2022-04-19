import pandas as pd
import numpy as np
import scipy 
from sklearn import preprocessing
conf19 = pd.read_csv('time_series_covid19_confirmed_global.csv')
conf19

#membuat data asia tenggara
asia =  ['Kamboja','Laos','Myanmar','Thailand','Vietnam','Brunei','Filipina','Indonesia','Malaysia','Singapura','Timor-Leste']
df_asia = conf19.loc[
                conf19['Country/Region'].isin(asia)
                & conf19['Province/State'].isna()]
df_asia = df_asia.drop(['Province/State','Lat','Long'],axis = 1) 
df_asia

array = df_asia.values
#memisahkan array menjadi komponen input dan output
x = array [:,1: ]  #membuat array dari kolom bertipe numerik
negara = array [:,0]
scaler = preprocessing.StandardScaler()
trans_asia_scaler = scaler.fit_transform(x)
trans_asia_scaler

#menjadikan array ke dataframe
df_transasia_z = pd.DataFrame(trans_asia_scaler)
#menambahkan negara di kolom
asia = ['Brunei','Indonesia','Laos','Malaysia','Thailand','Timor-Leste','Vietnam']
df_transasia_z.insert(0,'Country/Region',asia)
#mengubah index kolom menjadi negara
df_transasia_z.rename(index=lambda x: df_transasia_z.at[x,'Country/Region'], inplace=True)
#mengahpus kolom Country/Region
df_transasia_z1 = df_transasia_z.drop(['Country/Region'],axis = 1) 
df_transasia_z1

df_transasia_z1 = df_transasia_z1.transpose()
df_transasia_z1

#membuat list tanggal rentang start date sampai end date
import datetime
start = datetime.datetime.strptime("2020-01-22", "%Y-%m-%d")
end = datetime.datetime.strptime("2022-02-24", "%Y-%m-%d")
date_generated = pd.date_range(start, end)
datelist = date_generated.strftime("%Y-%m-%d")
#menambahkan tanggal ke kolom dataframe
df_transasia_z1.insert(0,'date',datelist)
df_transasia_z1

#mengubah index menjadi date
df_transasia_z1.rename(index=lambda x: df_transasia_z1.at[x,'date'], inplace=True)
#mengubah index date menjad datetime
df_transasia_z1.index = pd.to_datetime(df_transasia_z1.index)
df_transasia_z1 = df_transasia_z1.drop(['date'], axis = 1)
df_transasia_z1

import matplotlib.pyplot as plt
df_transasia_z1.plot(figsize=(15,10))
plt.title('Normalisasi data terkonfirmasi covid')
plt.xlabel('Dates')
plt.ylabel('confirmed covid')
plt.show()
