# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hcqdmMIqJTaYA3FVE54uj-Tc0RfBOcwg
"""

import numpy as np
import pandas as pd
import matplotlib as pt 
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor

from google.colab import files
uploaded=files.upload()
train_data=pd.read_excel('data_train.xlsx')

train_data.head()

train_data["Duration"].value_counts()

train_data.dropna(inplace=True)

train_data.isnull().sum()

train_data=train_data.drop(["Route","Additional_Info"],axis=1)

train_data

train_data['Journey_Day']=pd.to_datetime(train_data.Date_of_Journey,format="%d/%m/%Y").dt.day
train_data

train_data['Journey_Month']=pd.to_datetime(train_data.Date_of_Journey,format="%d/%m/%Y").dt.month
train_data

train_data=train_data.drop(["Date_of_Journey"],axis=1)
train_data

train_data['Dep_hour']=pd.to_datetime(train_data.Dep_Time).dt.hour

train_data['Dep_minute']=pd.to_datetime(train_data.Dep_Time).dt.minute

train_data

train_data['Arrival_hour']=pd.to_datetime(train_data.Arrival_Time).dt.hour
train_data['Arrival_minute']=pd.to_datetime(train_data.Arrival_Time).dt.minute
train_data



duration = list(train_data["Duration"])

for i in range (len(duration)):
  if len(duration[i].split()) != 2:

    if "h" in duration[i]:
      duration[i]=duration[i].strip()+" 0m"
    else:
      duration[i]="0h "+duration[i].strip()
 

duration_hours=[]
duration_mins=[]

for i in range (len(duration)):

  duration_hours.append(int(duration[i].split(sep ="h")[0]))     
  duration_mins.append(int(duration[i].split(sep ="m")[0].split()[-1]))

train_data["Duration_Hours"]=duration_hours
train_data["Duration_Minutes"]=duration_mins

train_data.drop(["Duration"],axis=1)

train_data.drop(["Dep_Time","Arrival_Time"],axis=1)

train_data=train_data.drop(["Dep_Time","Arrival_Time","Duration"],axis=1)

train_data

from sklearn.preprocessing import LabelEncoder
lb_s=LabelEncoder()
train_data.iloc[:,3]=lb_s.fit_transform(train_data.iloc[:,3].values)

train_data

Airline=train_data[["Airline"]]
Airline=pd.get_dummies(Airline,drop_first=True)
Airline

Source=train_data[["Source"]]
Source=pd.get_dummies(Source,drop_first=True)
Source

Destination=train_data[["Destination"]]
Destination=pd.get_dummies(Destination,drop_first=True)

train_data=pd.concat([train_data,Airline,Source,Destination],axis=1)
train_data

train_data=train_data.drop(["Airline","Source","Destination"],axis=1)
train_data

uploaded=files.upload()
test_data=pd.read_excel('test_data.xlsx')

test_data.head()

test_data["Duration"].value_counts()

test_data.dropna(inplace=True)

test_data.isnull().sum()

test_data=test_data.drop(["Route","Additional_Info"],axis=1)

test_data

test_data['Journey_Day']=pd.to_datetime(test_data.Date_of_Journey,format="%d/%m/%Y").dt.day
test_data

test_data['Journey_Month']=pd.to_datetime(test_data.Date_of_Journey,format="%d/%m/%Y").dt.month
test_data

test_data=test_data.drop(["Date_of_Journey"],axis=1)
test_data

test_data['Dep_hour']=pd.to_datetime(test_data.Dep_Time).dt.hour

test_data['Dep_minute']=pd.to_datetime(test_data.Dep_Time).dt.minute

test_data

test_data['Arrival_hour']=pd.to_datetime(test_data.Arrival_Time).dt.hour
test_data['Arrival_minute']=pd.to_datetime(test_data.Arrival_Time).dt.minute
test_data



duration = list(test_data["Duration"])

for i in range (len(duration)):
  if len(duration[i].split()) != 2:

    if "h" in duration[i]:
      duration[i]=duration[i].strip()+" 0m"
    else:
      duration[i]="0h "+duration[i].strip()
 

duration_hours=[]
duration_mins=[]

for i in range (len(duration)):

  duration_hours.append(int(duration[i].split(sep ="h")[0]))     
  duration_mins.append(int(duration[i].split(sep ="m")[0].split()[-1]))

test_data["Duration_Hours"]=duration_hours
test_data["Duration_Minutes"]=duration_mins

test_data.drop(["Duration"],axis=1)

test_data.drop(["Dep_Time","Arrival_Time"],axis=1)

test_data=test_data.drop(["Dep_Time","Arrival_Time","Duration"],axis=1)

test_data

from sklearn.preprocessing import LabelEncoder
lb_s=LabelEncoder()
test_data.iloc[:,3]=lb_s.fit_transform(test_data.iloc[:,3].values)

test_data

Airline=test_data[["Airline"]]
Airline=pd.get_dummies(Airline,drop_first=True)
Airline

Source=test_data[["Source"]]
Source=pd.get_dummies(Source,drop_first=True)
Source

Destination=test_data[["Destination"]]
Destination=pd.get_dummies(Destination,drop_first=True)

test_data=pd.concat([test_data,Airline,Source,Destination],axis=1)
test_data

test_data=test_data.drop(["Airline","Source","Destination"],axis=1)
test_data

##################################################################################### DATA CLEANING AND PREPROCESSING OVER########################################################################

train_data.shape

train_data.columns

X=train_data.loc[:,['Total_Stops','Journey_Day', 'Journey_Month', 'Dep_hour',
       'Dep_minute', 'Arrival_hour', 'Arrival_minute', 'Duration_Hours',
       'Duration_Minutes', 'Airline_Air India', 'Airline_GoAir',
       'Airline_IndiGo', 'Airline_Jet Airways', 'Airline_Jet Airways Business',
       'Airline_Multiple carriers','Airline_Multiple carriers Premium economy', 
       'Airline_SpiceJet','Airline_Vistara', 'Airline_Vistara Premium economy',
       'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
       'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
       'Destination_Kolkata', 'Destination_New Delhi']]

Y=train_data.iloc[:,1]
Y

import matplotlib.pyplot as plt

from sklearn.ensemble import ExtraTreesRegressor
selection=ExtraTreesRegressor()
selection.fit(X,Y)

print(selection.feature_importances_)

plt.figure(figsize = (12,8))
feat_importances = pd.Series(selection.feature_importances_, index=X.columns)
feat_importances.nlargest(20).plot(kind='barh')
plt.show()

################################################################################Important features###################################################################################333

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

from sklearn.ensemble import RandomForestRegressor
model=RandomForestRegressor()
model.fit(X_train,Y_train)

predictions=model.predict(X_test)
predictions

model.score(X_test,Y_test)

sns.distplot(predictions-Y_test)



