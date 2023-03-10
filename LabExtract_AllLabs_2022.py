#this code will extract all available labratories for patients (previous code will extract data on the defined labratories on defined day-from-admission)


import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import openpyxl

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)

#define name of hospital in databases, this will be used in the future
hospital_name="Emam"




# read patient database
Pts_File_Adres='/media/sdamirsa/Documents/MY WORK/MaGHALE/Big COVID phase 2/Data_Medical/Phase 2.xlsx'
dfasli=pd.read_excel(Pts_File_Adres, sheet_name='Cleaned E4')
dfasli=dfasli[dfasli['Hospital_x']==hospital_name]
# read labratories from 14 excel sheets
Lab_File_Adres='/media/sdamirsa/Documents/MY WORK/MaGHALE/Big COVID phase 2/Data_Labs/Emam/covid student.xls'

df0=pd.read_excel(Lab_File_Adres,sheet_name=0,header=None)
df1=pd.read_excel(Lab_File_Adres,sheet_name=1,header=None)
df2=pd.read_excel(Lab_File_Adres,sheet_name=2,header=None)
df3=pd.read_excel(Lab_File_Adres,sheet_name=3,header=None)
df4=pd.read_excel(Lab_File_Adres,sheet_name=4,header=None)
df5=pd.read_excel(Lab_File_Adres,sheet_name=5,header=None)
df6=pd.read_excel(Lab_File_Adres,sheet_name=6,header=None)
df7=pd.read_excel(Lab_File_Adres,sheet_name=7,header=None)
df8=pd.read_excel(Lab_File_Adres,sheet_name=8,header=None)
df9=pd.read_excel(Lab_File_Adres,sheet_name=9,header=None)
df10=pd.read_excel(Lab_File_Adres,sheet_name=10,header=None)
df11=pd.read_excel(Lab_File_Adres,sheet_name=11,header=None)
df12=pd.read_excel(Lab_File_Adres,sheet_name=12,header=None)
df13=pd.read_excel(Lab_File_Adres,sheet_name=13,header=None)

dfcodes= pd.concat([df0, df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13])
dfcodes = dfcodes.rename(columns={0: 'Labname', 1: 'Result',2:'Date',3:'id'})
dfcodes

# remove rows wiht Nan value
dfcodes.dropna( how='any',inplace=True)
dfcodes.index = range(len(dfcodes.index))
dfcodes=dfcodes.drop(index=0)
dfcodes.index = range(len(dfcodes.index))
dfcodes

#turn id vlaues to numeric
dfcodes["id"] = pd.to_numeric(dfcodes["id"] )
dfcodes

#find duplicate patients or patients without admission id (since the admission id is the key feature)
x=len(dfasli.index)
dfasli=dfasli.dropna(subset='id')
dfasli=dfasli.drop_duplicates(subset='id')
y=len(dfasli.index)
number_of_errors = x - y
print(number_of_errors)
dfasli

#define a function for calculating delta (interval between admission and labratory exam)
def tarikhberoz (args):
    Y = int (args [0:4])
    M = int (args [5:7])
    D = int (args [8:10])
    Y_D= Y*365
    if M<=6:
        M_D=M*31
    elif M>6:
        M_D=(M*30)+6
    else:
        print()
    Total_D= Y_D+M_D+D
    return Total_D

#Keeping yyyy/mm/dd and removing time
Date_clean=[]
for i in dfcodes['Date']:
    x=i[0:10]
    Date_clean.append(x)
dfcodes['Date']=Date_clean

# calculating dat from 0 (for calulating delta considering different days in a month in solari hijri calender)
Tarikh_be_roz=[]
for x in dfcodes['Date']:
    Date_roz_bastari = tarikhberoz(x)
    Tarikh_be_roz.append(Date_roz_bastari)
    
dfcodes = dfcodes.assign (Tarikh_be_roz = Tarikh_be_roz )
dfcodes

#sorting the lab databases
dfcodes=dfcodes.sort_values(by=['id','Labname','Date'])
dfcodes = dfcodes.reset_index(drop=True)
dfcodes

#Keeping yyyy/mm/dd and removing time
Date_clean=[]
for i in dfasli['Date']:
    i=str(i)
    x=i[0:10]
    Date_clean.append(x)
dfasli['Date']=Date_clean
dfasli

# calculating dat from 0 (for calulating delta considering different days in a month in solari hijri calender)
x=len(dfasli.index)
dfasli=dfasli.dropna(subset='Date')
dfasli.index = range(len(dfasli.index))
y=len(dfasli.index)
number_or_errors=x-y
print (number_or_errors)
dfasli

# in the Date column of dfasli there are some values wit "nan" strings that stop our function so lets remove them
dfasli = dfasli[dfasli.Date != 'nan']
dfasli.index = range(len(dfasli.index))
dfasli

Tarikh_be_roz=[]
for x in dfasli['Date']:
    Date_roz_bastari = tarikhberoz(x)
    Tarikh_be_roz.append(Date_roz_bastari)
dfasli=dfasli.assign(Tarikh_be_roz=Tarikh_be_roz)
dfasli


# lets calculate delta (delta is the interval between labratory exam and date of admission)

dfcodes["delta"] = ""
Delta=0
for idx,idd in enumerate(dfcodes["id"]):
    for idxBastari,iddBastari in enumerate(dfasli["id"]):
        if idd==iddBastari:
            Delta= (dfcodes.Tarikh_be_roz[idx]-dfasli.Tarikh_be_roz[idxBastari])+1
            dfcodes.delta[idx] = Delta
dfcodes


#finding patients with value labratory exam AND vali clincal exam for specific hospital 

included_id=[]
labids= dfcodes['id'].unique()
labids=labids.tolist()
for i in labids:
    for x in dfasli['id']:
        if i==x:
            included_id.append(i)
print(len(included_id))
print(included_id)

#create the structure for final dataframe =output
d = {'id':included_id}
dffinal = pd.DataFrame(d)
dffinal

df4=pd.DataFrame({'id':dfcodes['id'], 'Labname':dfcodes['Labname'], 'Result':dfcodes['Result'],'Date':dfcodes['Date'],
                  'panj':np.nan,'shesh': np.nan, 'delta': dfcodes['delta']})
df4

deltastring=[]
for i in df4['delta']:
    i=str(i)
    deltastring.append(i)
df4['delta']=deltastring
df4["name_delta"] = df4[["Labname", "delta"]].apply("-".join, axis=1)
df4

# after two years finally find a good soloution for the problem, I previously coded 2000 codes to reach same result
GOGO_mother=pd.DataFrame()
for i in included_id:
    GOGO=df4[df4['id']==i]
    GOGO_wide=pd.pivot_table(GOGO, index='id', columns=['name_delta'], values=['Result'],
                         aggfunc=lambda x: x.iloc[-1])
    GOGO_mother=pd.concat([GOGO_mother,GOGO_wide], axis=1)
    print(len(GOGO_mother))
GOGO_mother

GOGO_mother.to_csv('/home/sdamirsa/Desktop/GOGOishere_Emam.csv')
