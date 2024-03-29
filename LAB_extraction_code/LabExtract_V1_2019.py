# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

#load and merge list of patietns from (1) HIS (2) Patients medical records
df2= pd.read_excel("C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\Sheetsbypythone\Takmili_merged.xlsx") 
df1= pd.read_excel("C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\Sheetsbypythone\Merge.xlsx") 
df1.head()
df2.head()
result = pd.merge(df1,df2, on=['id'])
result.head()
result.to_excel("C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\Sheetsbypythone\CODE&LAB_Shohada.xlsx")

#load data from multiple HIS exported xls
dfasli=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\FINITOOOO\S&E&T_Final_Code&Lab.xlsx", sheet_name="v2_Shohada_Lab&Code")
df0=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1398.xls", sheet_name=0,header=None)
df1=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1399.xls", sheet_name=0,header=None)
df2=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1399.xls", sheet_name=1,header=None)
df3=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1399.xls", sheet_name=2,header=None)
df4=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1399.xls", sheet_name=3,header=None)
df5=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1399.xls", sheet_name=4,header=None)
df6=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1399.xls", sheet_name=5,header=None)
df7=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1399.xls", sheet_name=6,header=None)
df8=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1399.xls", sheet_name=7,header=None)
df9=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1399.xls", sheet_name=8,header=None)
df10=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1399.xls", sheet_name=9,header=None)
df11=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1399.xls", sheet_name=10,header=None)
df12=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1399.xls", sheet_name=11,header=None)
df13=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1399.xls", sheet_name=12,header=None)
df14=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1399.xls", sheet_name=13,header=None)
df15=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1399.xls", sheet_name=14,header=None)
df16=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1399.xls", sheet_name=15,header=None)
df17=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1399.xls", sheet_name=16,header=None)
df18=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1400.xls", sheet_name=0,header=None)
df19=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1400.xls", sheet_name=1,header=None)
df20=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1400.xls", sheet_name=2,header=None)
df21=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1400.xls", sheet_name=3,header=None)
df22=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1400.xls", sheet_name=4,header=None)
df23=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1400.xls", sheet_name=5,header=None)
df24=pd.read_excel(r"C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\tarkhis\covid2-1400.xls", sheet_name=6,header=None)
dfcodes= pd.concat([df0, df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,
                  df18,df19,df20,df21,df22,df23,df24])
dfcodes = dfcodes.rename(columns={1: 'id'})
dfcodes=dfcodes.dropna(how='all', axis=1)
dfcodes.head()
dfcodes["id"] = dfcodes["id"].str.replace(',', '')
dfcodes.head()
dfcodes["id"] = pd.to_numeric(dfcodes["id"] )
dfcodesnew=dfcodes.drop_duplicates()

# Lab Extraction
#!/usr/bin/env python
# coding: utf-8

# In[1]:
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


# In[33]:
filename= ("C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\Cleadedforpythone_2sheethazf.xlsx")
df = pd.read_excel(filename,sheet_name=0)
df.head()
df.head(20)


# In[34]:
df["Date"]=df["Date"].str.split(" ",n=1,expand=True) #zaman ro az tarikh joda kardim ta behtar bekhone
df.head()


# In[35]:
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

Date_d =[]
for x in df["Date"]:
    Date_roz = tarikhberoz(x)
    Date_d.append(Date_roz)

df2 = df.assign (Date_Lab = Date_d)
df2.head()


# In[36]:


df2= df2.sort_values(by=['id','Lab','Date_Lab'])
df2 = df2.reset_index(drop=True)
df2.head(100)


# In[37]:


filename_bastari= ("C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\Code.xlsx")
headersBastari= ["id","Date_bastari"]
dfBastari = pd.read_excel(filename_bastari, header=None)
dfBastari.columns = headersBastari
dfBastari.head()


# In[38]:


dfBastari["Date_bastari"]=dfBastari["Date_bastari"].str.split(" ",n=1,expand=True) #zaman ro az tarikh joda kardim ta behtar bekhone
dfBastari.head()


# In[39]:



DateBastari_d =[]
for x in dfBastari["Date_bastari"]:
    Date_roz_bastari = tarikhberoz(x)
    DateBastari_d.append(Date_roz_bastari)
print(DateBastari_d)

dfBastari2 = dfBastari.assign (Date_Bastari = DateBastari_d )
dfBastari2.head()


# In[40]:


df2["delta"] = ""
Delta=0
for idx,idd in enumerate(df2["id"]):
    for idxBastari,iddBastari in enumerate(dfBastari2["id"]):
        if idd==iddBastari:
            Delta= (df2.Date_Lab[idx]-dfBastari2.Date_Bastari[idxBastari])+1
            df2.delta[idx] = Delta
df2.head(100)


# In[41]:


idfinal=[]
Pnumbfinal=[]

for idxf,iddf in enumerate(df2["id"]):
    if not(iddf in idfinal):
        idfinal.append(iddf)
d = {"id":idfinal}
dffinal = pd.DataFrame(d)
dffinal.head(10)

Result_float = pd.to_numeric(df2["Result"], downcast='float',errors='coerce')
df4 = df2.assign(Result_float=Result_float)
df4.head()


WBCFinal=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="W.B.C") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    WBCFinal.append(tmpmax)
    tmpmax=""
print("WBCFinal",WBCFinal)

WBC1=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="W.B.C") and (df4.iloc[idx,6]==1):
            tmp1 = df4.iloc[idx,2]
            WBC1.append(tmp1)
            break
    else:
        WBC1.append("")
print("WBC1",WBC1)

WBC2=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="W.B.C") and (df4.iloc[idx,6]==2):
            tmp2 = df4.iloc[idx,2]
            WBC2.append(tmp2)
            break
    else:
        WBC2.append("")
print("WBC2",WBC2)

WBC3=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="W.B.C") and (df4.iloc[idx,6]==3):
            tmp3 = df4.iloc[idx,2]
            WBC3.append(tmp3)
            break
    else:
        WBC3.append("")
print("WBC3",WBC3)

WBC4=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="W.B.C") and (df4.iloc[idx,6]==4):
            tmp4 = df4.iloc[idx,2]
            WBC4.append(tmp4)
            break
    else:
        WBC4.append("")
print("WBC4",WBC4)

WBC5=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="W.B.C") and (df4.iloc[idx,6]==5):
            tmp5 = df4.iloc[idx,2]
            WBC5.append(tmp5)
            break
    else:
        WBC5.append("")
print("WBC5",WBC5)
WBC6=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="W.B.C") and (df4.iloc[idx,6]==6):
            tmp6 = df4.iloc[idx,2]
            WBC6.append(tmp6)
            break
    else:
        WBC6.append("")
print("WBC6",WBC6)


dffinal2= dffinal.assign(WBC1=WBC1, WBC2=WBC2, WBC3=WBC3, WBC4=WBC4,WBC5=WBC5, WBC6=WBC6,WBCFinal=WBCFinal)
dffinal2.head()
NAMELYMPHH1=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Lymph") and (df4.iloc[idx,6]==1):
            tmp1 = df4.iloc[idx,2]
            NAMELYMPHH1.append(tmp1)
            break
    else:
        NAMELYMPHH1.append("")
print("NAMELYMPHH1",NAMELYMPHH1)

NAMELYMPHH2=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Lymph") and (df4.iloc[idx,6]==2):
            tmp2 = df4.iloc[idx,2]
            NAMELYMPHH2.append(tmp2)
            break
    else:
        NAMELYMPHH2.append("")
print("NAMELYMPHH2",NAMELYMPHH2)

NAMELYMPHH3=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Lymph") and (df4.iloc[idx,6]==3):
            tmp3 = df4.iloc[idx,2]
            NAMELYMPHH3.append(tmp3)
            break
    else:
        NAMELYMPHH3.append("")
print("NAMELYMPHH3",NAMELYMPHH3)

NAMELYMPHH4=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Lymph") and (df4.iloc[idx,6]==4):
            tmp4 = df4.iloc[idx,2]
            NAMELYMPHH4.append(tmp4)
            break
    else:
        NAMELYMPHH4.append("")
print("NAMELYMPHH4",NAMELYMPHH4)

NAMELYMPHH5=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Lymph") and (df4.iloc[idx,6]==5):
            tmp5 = df4.iloc[idx,2]
            NAMELYMPHH5.append(tmp5)
            break
    else:
        NAMELYMPHH5.append("")
print("NAMELYMPHH5",NAMELYMPHH5)
NAMELYMPHH6=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Lymph") and (df4.iloc[idx,6]==6):
            tmp6 = df4.iloc[idx,2]
            NAMELYMPHH6.append(tmp6)
            break
    else:
        NAMELYMPHH6.append("")
print("NAMELYMPHH6",NAMELYMPHH6)

NAMELYMPHHFinal=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Lymph") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    NAMELYMPHHFinal.append(tmpmax)
    tmpmax=""

Dffinal3= dffinal2.assign(NAMELYMPHH1=NAMELYMPHH1, NAMELYMPHH2=NAMELYMPHH2, NAMELYMPHH3=NAMELYMPHH3, NAMELYMPHH4=NAMELYMPHH4,NAMELYMPHH5=NAMELYMPHH5, NAMELYMPHH6=NAMELYMPHH6,NAMELYMPHHFinal=NAMELYMPHHFinal)
Dffinal3.head()
NAMENEUT1=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Neut") and (df4.iloc[idx,6]==1):
            tmp1 = df4.iloc[idx,2]
            NAMENEUT1.append(tmp1)
            break
    else:
        NAMENEUT1.append("")
print("NAMENEUT1",NAMENEUT1)

NAMENEUT2=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Neut") and (df4.iloc[idx,6]==2):
            tmp2 = df4.iloc[idx,2]
            NAMENEUT2.append(tmp2)
            break
    else:
        NAMENEUT2.append("")
print("NAMENEUT2",NAMENEUT2)

NAMENEUT3=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Neut") and (df4.iloc[idx,6]==3):
            tmp3 = df4.iloc[idx,2]
            NAMENEUT3.append(tmp3)
            break
    else:
        NAMENEUT3.append("")
print("NAMENEUT3",NAMENEUT3)

NAMENEUT4=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Neut") and (df4.iloc[idx,6]==4):
            tmp4 = df4.iloc[idx,2]
            NAMENEUT4.append(tmp4)
            break
    else:
        NAMENEUT4.append("")
print("NAMENEUT4",NAMENEUT4)

NAMENEUT5=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Neut") and (df4.iloc[idx,6]==5):
            tmp5 = df4.iloc[idx,2]
            NAMENEUT5.append(tmp5)
            break
    else:
        NAMENEUT5.append("")
print("NAMENEUT5",NAMENEUT5)
NAMENEUT6=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Neut") and (df4.iloc[idx,6]==6):
            tmp6 = df4.iloc[idx,2]
            NAMENEUT6.append(tmp6)
            break
    else:
        NAMENEUT6.append("")
print("NAMENEUT6",NAMENEUT6)

NAMENEUTFinal=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Neut") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    NAMENEUTFinal.append(tmpmax)
    tmpmax=""
print("NAMENEUTFinal",NAMENEUTFinal)

Dffinal4= Dffinal3.assign(NAMENEUT1=NAMENEUT1, NAMENEUT2=NAMENEUT2, NAMENEUT3=NAMENEUT3, NAMENEUT4=NAMENEUT4,NAMENEUT5=NAMENEUT5, NAMENEUT6=NAMENEUT6,NAMENEUTFinal=NAMENEUTFinal)
Dffinal4.head()

NAMEPLT1=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="PLT") and (df4.iloc[idx,6]==1):
            tmp1 = df4.iloc[idx,2]
            NAMEPLT1.append(tmp1)
            break
    else:
        NAMEPLT1.append("")
print("NAMEPLT1",NAMEPLT1)

NAMEPLT2=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="PLT") and (df4.iloc[idx,6]==2):
            tmp2 = df4.iloc[idx,2]
            NAMEPLT2.append(tmp2)
            break
    else:
        NAMEPLT2.append("")
print("NAMEPLT2",NAMEPLT2)

NAMEPLT3=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="PLT") and (df4.iloc[idx,6]==3):
            tmp3 = df4.iloc[idx,2]
            NAMEPLT3.append(tmp3)
            break
    else:
        NAMEPLT3.append("")
print("NAMEPLT3",NAMEPLT3)

NAMEPLT4=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="PLT") and (df4.iloc[idx,6]==4):
            tmp4 = df4.iloc[idx,2]
            NAMEPLT4.append(tmp4)
            break
    else:
        NAMEPLT4.append("")
print("NAMEPLT4",NAMEPLT4)

NAMEPLT5=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="PLT") and (df4.iloc[idx,6]==5):
            tmp5 = df4.iloc[idx,2]
            NAMEPLT5.append(tmp5)
            break
    else:
        NAMEPLT5.append("")
print("NAMEPLT5",NAMEPLT5)
NAMEPLT6=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="PLT") and (df4.iloc[idx,6]==6):
            tmp6 = df4.iloc[idx,2]
            NAMEPLT6.append(tmp6)
            break
    else:
        NAMEPLT6.append("")
print("NAMEPLT6",NAMEPLT6)

NAMEPLTFinal=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="PLT") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    NAMEPLTFinal.append(tmpmax)
    tmpmax=""
print("NAMEPLTFinal",NAMEPLTFinal)

Dffinal5= Dffinal4.assign(NAMEPLT1=NAMEPLT1, NAMEPLT2=NAMEPLT2, NAMEPLT3=NAMEPLT3, NAMEPLT4=NAMEPLT4,NAMEPLT5=NAMEPLT5, NAMEPLT6=NAMEPLT6,NAMEPLTFinal=NAMEPLTFinal)
Dffinal5.head()

NAMEHB1=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="HGB") and (df4.iloc[idx,6]==1):
            tmp1 = df4.iloc[idx,2]
            NAMEHB1.append(tmp1)
            break
    else:
        NAMEHB1.append("")
print("NAMEHB1",NAMEHB1)

NAMEHB2=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="HGB") and (df4.iloc[idx,6]==2):
            tmp2 = df4.iloc[idx,2]
            NAMEHB2.append(tmp2)
            break
    else:
        NAMEHB2.append("")
print("NAMEHB2",NAMEHB2)

NAMEHB3=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="HGB") and (df4.iloc[idx,6]==3):
            tmp3 = df4.iloc[idx,2]
            NAMEHB3.append(tmp3)
            break
    else:
        NAMEHB3.append("")
print("NAMEHB3",NAMEHB3)

NAMEHB4=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="HGB") and (df4.iloc[idx,6]==4):
            tmp4 = df4.iloc[idx,2]
            NAMEHB4.append(tmp4)
            break
    else:
        NAMEHB4.append("")
print("NAMEHB4",NAMEHB4)

NAMEHB5=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="HGB") and (df4.iloc[idx,6]==5):
            tmp5 = df4.iloc[idx,2]
            NAMEHB5.append(tmp5)
            break
    else:
        NAMEHB5.append("")
print("NAMEHB5",NAMEHB5)
NAMEHB6=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="HGB") and (df4.iloc[idx,6]==6):
            tmp6 = df4.iloc[idx,2]
            NAMEHB6.append(tmp6)
            break
    else:
        NAMEHB6.append("")
print("NAMEHB6",NAMEHB6)

NAMEHBFinal=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="HGB") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    NAMEHBFinal.append(tmpmax)
    tmpmax=""
print("NAMEHBFinal",NAMEHBFinal)

Dffinal6= Dffinal5.assign(NAMEHB1=NAMEHB1, NAMEHB2=NAMEHB2, NAMEHB3=NAMEHB3, NAMEHB4=NAMEHB4,NAMEHB5=NAMEHB5, NAMEHB6=NAMEHB6,NAMEHBFinal=NAMEHBFinal)
Dffinal6.head()

NAMEMCV1=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="MCV") and (df4.iloc[idx,6]==1):
            tmp1 = df4.iloc[idx,2]
            NAMEMCV1.append(tmp1)
            break
    else:
        NAMEMCV1.append("")
print("NAMEMCV1",NAMEMCV1)

NAMEMCV2=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="MCV") and (df4.iloc[idx,6]==2):
            tmp2 = df4.iloc[idx,2]
            NAMEMCV2.append(tmp2)
            break
    else:
        NAMEMCV2.append("")
print("NAMEMCV2",NAMEMCV2)

NAMEMCV3=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="MCV") and (df4.iloc[idx,6]==3):
            tmp3 = df4.iloc[idx,2]
            NAMEMCV3.append(tmp3)
            break
    else:
        NAMEMCV3.append("")
print("NAMEMCV3",NAMEMCV3)

NAMEMCV4=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="MCV") and (df4.iloc[idx,6]==4):
            tmp4 = df4.iloc[idx,2]
            NAMEMCV4.append(tmp4)
            break
    else:
        NAMEMCV4.append("")
print("NAMEMCV4",NAMEMCV4)

NAMEMCV5=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="MCV") and (df4.iloc[idx,6]==5):
            tmp5 = df4.iloc[idx,2]
            NAMEMCV5.append(tmp5)
            break
    else:
        NAMEMCV5.append("")
print("NAMEMCV5",NAMEMCV5)
NAMEMCV6=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="MCV") and (df4.iloc[idx,6]==6):
            tmp6 = df4.iloc[idx,2]
            NAMEMCV6.append(tmp6)
            break
    else:
        NAMEMCV6.append("")
print("NAMEMCV6",NAMEMCV6)

NAMEMCVFinal=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="MCV") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    NAMEMCVFinal.append(tmpmax)
    tmpmax=""
print("NAMEMCVFinal",NAMEMCVFinal)

Dffinal7= Dffinal6.assign(NAMEMCV1=NAMEMCV1, NAMEMCV2=NAMEMCV2, NAMEMCV3=NAMEMCV3, NAMEMCV4=NAMEMCV4,NAMEMCV5=NAMEMCV5, NAMEMCV6=NAMEMCV6,NAMEMCVFinal=NAMEMCVFinal)
Dffinal7.head()

NAMEUREA1=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="BUN") and (df4.iloc[idx,6]==1):
            tmp1 = df4.iloc[idx,2]
            NAMEUREA1.append(tmp1)
            break
    else:
        NAMEUREA1.append("")
print("NAMEUREA1",NAMEUREA1)

NAMEUREA2=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="BUN") and (df4.iloc[idx,6]==2):
            tmp2 = df4.iloc[idx,2]
            NAMEUREA2.append(tmp2)
            break
    else:
        NAMEUREA2.append("")
print("NAMEUREA2",NAMEUREA2)

NAMEUREA3=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="BUN") and (df4.iloc[idx,6]==3):
            tmp3 = df4.iloc[idx,2]
            NAMEUREA3.append(tmp3)
            break
    else:
        NAMEUREA3.append("")
print("NAMEUREA3",NAMEUREA3)

NAMEUREA4=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="BUN") and (df4.iloc[idx,6]==4):
            tmp4 = df4.iloc[idx,2]
            NAMEUREA4.append(tmp4)
            break
    else:
        NAMEUREA4.append("")
print("NAMEUREA4",NAMEUREA4)

NAMEUREA5=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="BUN") and (df4.iloc[idx,6]==5):
            tmp5 = df4.iloc[idx,2]
            NAMEUREA5.append(tmp5)
            break
    else:
        NAMEUREA5.append("")
print("NAMEUREA5",NAMEUREA5)
NAMEUREA6=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="BUN") and (df4.iloc[idx,6]==6):
            tmp6 = df4.iloc[idx,2]
            NAMEUREA6.append(tmp6)
            break
    else:
        NAMEUREA6.append("")
print("NAMEUREA6",NAMEUREA6)

NAMEUREAFinal=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="BUN") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    NAMEUREAFinal.append(tmpmax)
    tmpmax=""
print("NAMEUREAFinal",NAMEUREAFinal)

Dffinal8= Dffinal7.assign(BUN1=NAMEUREA1, BUN2=NAMEUREA2, BUN3=NAMEUREA3, BUN4=NAMEUREA4,BUN5=NAMEUREA5, BUN6=NAMEUREA6,BUNFinal=NAMEUREAFinal)
Dffinal8.head()

NAMECR1=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Creatinine") and (df4.iloc[idx,6]==1):
            tmp1 = df4.iloc[idx,2]
            NAMECR1.append(tmp1)
            break
    else:
        NAMECR1.append("")
print("NAMECR1",NAMECR1)

NAMECR2=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Creatinine") and (df4.iloc[idx,6]==2):
            tmp2 = df4.iloc[idx,2]
            NAMECR2.append(tmp2)
            break
    else:
        NAMECR2.append("")
print("NAMECR2",NAMECR2)

NAMECR3=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Creatinine") and (df4.iloc[idx,6]==3):
            tmp3 = df4.iloc[idx,2]
            NAMECR3.append(tmp3)
            break
    else:
        NAMECR3.append("")
print("NAMECR3",NAMECR3)

NAMECR4=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Creatinine") and (df4.iloc[idx,6]==4):
            tmp4 = df4.iloc[idx,2]
            NAMECR4.append(tmp4)
            break
    else:
        NAMECR4.append("")
print("NAMECR4",NAMECR4)

NAMECR5=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Creatinine") and (df4.iloc[idx,6]==5):
            tmp5 = df4.iloc[idx,2]
            NAMECR5.append(tmp5)
            break
    else:
        NAMECR5.append("")
print("NAMECR5",NAMECR5)
NAMECR6=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Creatinine") and (df4.iloc[idx,6]==6):
            tmp6 = df4.iloc[idx,2]
            NAMECR6.append(tmp6)
            break
    else:
        NAMECR6.append("")
print("NAMECR6",NAMECR6)

NAMECRFinal=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Creatinine") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    NAMECRFinal.append(tmpmax)
    tmpmax=""
print("NAMECRFinal",NAMECRFinal)

Dffinal9= Dffinal8.assign(NAMECR1=NAMECR1, NAMECR2=NAMECR2, NAMECR3=NAMECR3, NAMECR4=NAMECR4,NAMECR5=NAMECR5, NAMECR6=NAMECR6,NAMECRFinal=NAMECRFinal)
Dffinal9.head()

NAMENAFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Na") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    NAMENAFirst.append(tmpm)
    tmpm=""
    
print("NAMENAFirst",NAMENAFirst)

NAMENAFinal=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Na") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    NAMENAFinal.append(tmpmax)
    tmpmax=""
print("NAMENAFinal",NAMENAFinal)



Dffinal10= Dffinal9.assign(NAMENAFirst=NAMENAFirst,NAMENAFinal=NAMENAFinal)
Dffinal10.head()

NAMEKFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="K") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    NAMEKFirst.append(tmpm)
    tmpm=""
print("NAMEKFirst",NAMEKFirst)

NAMEKFinal=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="K") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    NAMEKFinal.append(tmpmax)
    tmpmax=""
print("NAMEKFinal",NAMEKFinal)



Dffinal11= Dffinal10.assign(NAMEKFirst=NAMEKFirst,NAMEKFinal=NAMEKFinal)
Dffinal11.head()

NAMECAFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Ca") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    NAMECAFirst.append(tmpm)
    tmpm=""
print("NAMECAFirst",NAMECAFirst)

NAMEMGFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Mg") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    NAMEMGFirst.append(tmpm)
    tmpm=""
print("NAMEMGFirst",NAMEMGFirst)

NAMEPFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Phosphorus") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    NAMEPFirst.append(tmpm)
    tmpm=""
print("NAMEPFirst",NAMEPFirst)

Dffinal12= Dffinal11.assign(NAMECAFirst=NAMECAFirst,NAMEMGFirst=NAMEMGFirst,NAMEPFirst=NAMEPFirst)
Dffinal12.head()

NAMEAST1=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="AST") and (df4.iloc[idx,6]==1):
            tmp1 = df4.iloc[idx,2]
            NAMEAST1.append(tmp1)
            break
    else:
        NAMEAST1.append("")
print("NAMEAST1",NAMEAST1)

NAMEAST2=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="AST") and (df4.iloc[idx,6]==2):
            tmp2 = df4.iloc[idx,2]
            NAMEAST2.append(tmp2)
            break
    else:
        NAMEAST2.append("")
print("NAMEAST2",NAMEAST2)

NAMEAST3=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="AST") and (df4.iloc[idx,6]==3):
            tmp3 = df4.iloc[idx,2]
            NAMEAST3.append(tmp3)
            break
    else:
        NAMEAST3.append("")
print("NAMEAST3",NAMEAST3)

NAMEAST4=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="AST") and (df4.iloc[idx,6]==4):
            tmp4 = df4.iloc[idx,2]
            NAMEAST4.append(tmp4)
            break
    else:
        NAMEAST4.append("")
print("NAMEAST4",NAMEAST4)

NAMEAST5=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="AST") and (df4.iloc[idx,6]==5):
            tmp5 = df4.iloc[idx,2]
            NAMEAST5.append(tmp5)
            break
    else:
        NAMEAST5.append("")
print("NAMEAST5",NAMEAST5)
NAMEAST6=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="AST") and (df4.iloc[idx,6]==6):
            tmp6 = df4.iloc[idx,2]
            NAMEAST6.append(tmp6)
            break
    else:
        NAMEAST6.append("")
print("NAMEAST6",NAMEAST6)

NAMEASTFinal=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="AST") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    NAMEASTFinal.append(tmpmax)
    tmpmax=""
print("NAMEASTFinal",NAMEASTFinal)


Dffinal13= Dffinal12.assign(NAMEAST1=NAMEAST1, NAMEAST2=NAMEAST2, NAMEAST3=NAMEAST3, NAMEAST4=NAMEAST4,NAMEAST5=NAMEAST5, NAMEAST6=NAMEAST6,NAMEASTFinal=NAMEASTFinal)
Dffinal13.head()

NAMEALT1=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="ALT") and (df4.iloc[idx,6]==1):
            tmp1 = df4.iloc[idx,2]
            NAMEALT1.append(tmp1)
            break
    else:
        NAMEALT1.append("")
print("NAMEALT1",NAMEALT1)

NAMEALT2=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="ALT") and (df4.iloc[idx,6]==2):
            tmp2 = df4.iloc[idx,2]
            NAMEALT2.append(tmp2)
            break
    else:
        NAMEALT2.append("")
print("NAMEALT2",NAMEALT2)

NAMEALT3=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="ALT") and (df4.iloc[idx,6]==3):
            tmp3 = df4.iloc[idx,2]
            NAMEALT3.append(tmp3)
            break
    else:
        NAMEALT3.append("")
print("NAMEALT3",NAMEALT3)

NAMEALT4=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="ALT") and (df4.iloc[idx,6]==4):
            tmp4 = df4.iloc[idx,2]
            NAMEALT4.append(tmp4)
            break
    else:
        NAMEALT4.append("")
print("NAMEALT4",NAMEALT4)

NAMEALT5=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="ALT") and (df4.iloc[idx,6]==5):
            tmp5 = df4.iloc[idx,2]
            NAMEALT5.append(tmp5)
            break
    else:
        NAMEALT5.append("")
print("NAMEALT5",NAMEALT5)
NAMEALT6=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="ALT") and (df4.iloc[idx,6]==6):
            tmp6 = df4.iloc[idx,2]
            NAMEALT6.append(tmp6)
            break
    else:
        NAMEALT6.append("")
print("NAMEALT6",NAMEALT6)

NAMEALTFinal=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="ALT") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    NAMEALTFinal.append(tmpmax)
    tmpmax=""
print("NAMEALTFinal",NAMEALTFinal)


Dffinal14= Dffinal13.assign(NAMEALT1=NAMEALT1, NAMEALT2=NAMEALT2, NAMEALT3=NAMEALT3, NAMEALT4=NAMEALT4,NAMEALT5=NAMEALT5, NAMEALT6=NAMEALT6,NAMEALTFinal=NAMEALTFinal)
Dffinal14.head()
NAMEALKPFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="ALk P") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    NAMEALKPFirst.append(tmpm)
    tmpm=""
print("NAMEALKPFirst",NAMEALKPFirst)

NAMEBILLTFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Bilirubin T") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    NAMEBILLTFirst.append(tmpm)
    tmpm=""
print("NAMEBILLTFirst",NAMEBILLTFirst)

NAMEBILLDFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Bilirubin D") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    NAMEBILLDFirst.append(tmpm)
    tmpm=""
print("NAMEBILLDFirst",NAMEBILLDFirst)

AMYLASEFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Amylase") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    AMYLASEFirst.append(tmpm)
    tmpm=""
print("AMYLASEFirst",AMYLASEFirst)

LIPASEFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Lipase") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    LIPASEFirst.append(tmpm)
    tmpm=""
print("LIPASEFirst",LIPASEFirst)

Dffinal15= Dffinal14.assign(NAMEALKPFirst=NAMEALKPFirst, NAMEBILLTFirst=NAMEBILLTFirst, NAMEBILLDFirst=NAMEBILLDFirst, AMYLASEFirst=AMYLASEFirst,LIPASEFirst=LIPASEFirst)
Dffinal15.head()
NAMETGFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="TG") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    NAMETGFirst.append(tmpm)
    tmpm=""
print("NAMETGFirst",NAMETGFirst)

CHOLESTROLFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Cholestrol") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    CHOLESTROLFirst.append(tmpm)
    tmpm=""
print("CHOLESTROLFirst",CHOLESTROLFirst)

NAMEHDLFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="HDL-C") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    NAMEHDLFirst.append(tmpm)
    tmpm=""
print("NAMEHDLFirst",NAMEHDLFirst)

NAMELDLFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="LDL-C") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    NAMELDLFirst.append(tmpm)
    tmpm=""
print("NAMELDLFirst",NAMELDLFirst)

Dffinal16= Dffinal15.assign(NAMETGFirst=NAMETGFirst, CHOLESTROLFirst=CHOLESTROLFirst, NAMEHDLFirst=NAMEHDLFirst, NAMELDLFirst=NAMELDLFirst)
Dffinal16.head()

NAMEFBSFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="FBS") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    NAMEFBSFirst.append(tmpm)
    tmpm=""
print("NAMEFBSFirst",NAMEFBSFirst)

NAMEHBA1CFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="HbA1C") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    NAMEHBA1CFirst.append(tmpm)
    tmpm=""
print("NAMEHBA1CFirst",NAMEHBA1CFirst)

ALBUMINFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Alb Serum") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    ALBUMINFirst.append(tmpm)
    tmpm=""
print("ALBUMINFirst",ALBUMINFirst)

Dffinal17= Dffinal16.assign(NAMEFBSFirst=NAMEFBSFirst, NAMEHBA1CFirst=NAMEHBA1CFirst, ALBUMINFirst=ALBUMINFirst)
Dffinal17.head()
NAMELDH1=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="LDH Serum") and (df4.iloc[idx,6]==1):
            tmp1 = df4.iloc[idx,2]
            NAMELDH1.append(tmp1)
            break
    else:
        NAMELDH1.append("")
print("NAMELDH1",NAMELDH1)

NAMELDH2=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="LDH Serum") and (df4.iloc[idx,6]==2):
            tmp2 = df4.iloc[idx,2]
            NAMELDH2.append(tmp2)
            break
    else:
        NAMELDH2.append("")
print("NAMELDH2",NAMELDH2)

NAMELDH3=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="LDH Serum") and (df4.iloc[idx,6]==3):
            tmp3 = df4.iloc[idx,2]
            NAMELDH3.append(tmp3)
            break
    else:
        NAMELDH3.append("")
print("NAMELDH3",NAMELDH3)

NAMELDH4=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="LDH Serum") and (df4.iloc[idx,6]==4):
            tmp4 = df4.iloc[idx,2]
            NAMELDH4.append(tmp4)
            break
    else:
        NAMELDH4.append("")
print("NAMELDH4",NAMELDH4)

NAMELDH5=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="LDH Serum") and (df4.iloc[idx,6]==5):
            tmp5 = df4.iloc[idx,2]
            NAMELDH5.append(tmp5)
            break
    else:
        NAMELDH5.append("")
print("NAMELDH5",NAMELDH5)
NAMELDH6=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="LDH Serum") and (df4.iloc[idx,6]==6):
            tmp6 = df4.iloc[idx,2]
            NAMELDH6.append(tmp6)
            break
    else:
        NAMELDH6.append("")
print("NAMELDH6",NAMELDH6)

NAMELDHFinal=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="LDH Serum") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    NAMELDHFinal.append(tmpmax)
    tmpmax=""
print("NAMELDHFinal",NAMELDHFinal)

Dffinal18= Dffinal17.assign(NAMELDH1=NAMELDH1, NAMELDH2=NAMELDH2, NAMELDH3=NAMELDH3, NAMELDH4=NAMELDH4,NAMELDH5=NAMELDH5, NAMELDH6=NAMELDH6,NAMELDHFinal=NAMELDHFinal)
Dffinal18.head()
NAMECRP1=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="CRP کمی") and (df4.iloc[idx,6]==1):
            tmp1 = df4.iloc[idx,2]
            NAMECRP1.append(tmp1)
            break
    else:
        NAMECRP1.append("")
print("NAMECRP1",NAMECRP1)

NAMECRP2=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="CRP کمی") and (df4.iloc[idx,6]==2):
            tmp2 = df4.iloc[idx,2]
            NAMECRP2.append(tmp2)
            break
    else:
        NAMECRP2.append("")
print("NAMECRP2",NAMECRP2)

NAMECRP3=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="CRP کمی") and (df4.iloc[idx,6]==3):
            tmp3 = df4.iloc[idx,2]
            NAMECRP3.append(tmp3)
            break
    else:
        NAMECRP3.append("")
print("NAMECRP3",NAMECRP3)

NAMECRP4=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="CRP کمی") and (df4.iloc[idx,6]==4):
            tmp4 = df4.iloc[idx,2]
            NAMECRP4.append(tmp4)
            break
    else:
        NAMECRP4.append("")
print("NAMECRP4",NAMECRP4)

NAMECRP5=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="CRP کمی") and (df4.iloc[idx,6]==5):
            tmp5 = df4.iloc[idx,2]
            NAMECRP5.append(tmp5)
            break
    else:
        NAMECRP5.append("")
print("NAMECRP5",NAMECRP5)
NAMECRP6=[]
for idxf,iddf in enumerate(dffinal["id"]):
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="CRP کمی") and (df4.iloc[idx,6]==6):
            tmp6 = df4.iloc[idx,2]
            NAMECRP6.append(tmp6)
            break
    else:
        NAMECRP6.append("")
print("NAMECRP6",NAMECRP6)

NAMECRPFinal=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="CRP کمی") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    NAMECRPFinal.append(tmpmax)
    tmpmax=""
print("NAMECRPFinal",NAMECRPFinal)

Dffinal19= Dffinal18.assign(NAMECRP1=NAMECRP1, NAMECRP2=NAMECRP2, NAMECRP3=NAMECRP3, NAMECRP4=NAMECRP4,NAMECRP5=NAMECRP5, NAMECRP6=NAMECRP6,NAMECRPFinal=NAMECRPFinal)
Dffinal19.head()
ESRFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="ESR") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    ESRFirst.append(tmpm)
    tmpm=""
print("ESRFirst",ESRFirst)

LACTATEFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Lactate") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
    LACTATEFirst.append(tmpm)
    tmpm=""
print("LACTATEFirst",LACTATEFirst)

IL6First=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Interleukins 6") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    IL6First.append(tmpm)
    tmpm=""
print("IL6First",IL6First)

CPKFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="CPK") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    CPKFirst.append(tmpm)
    tmpm=""
print("CPKFirst",CPKFirst)

DDIMERFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="D-Dimer") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    DDIMERFirst.append(tmpm)
    tmpm=""
print("DDIMERFirst",DDIMERFirst)

Dffinal20= Dffinal19.assign(ESRFirst=ESRFirst, LACTATEFirst=LACTATEFirst, IL6First=IL6First, CPKFirst=CPKFirst,DDIMERFirst=DDIMERFirst)
Dffinal20.head()
TROPONINEFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Troponinکمی") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    TROPONINEFirst.append(tmpm)
    tmpm=""
print("TROPONINEFirst",TROPONINEFirst)

CKMBFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="CK MB") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    CKMBFirst.append(tmpm)
    tmpm=""
print("CKMBFirst",CKMBFirst)

PROBNPFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="PRO-BNP") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    PROBNPFirst.append(tmpm)
    tmpm=""
print("PROBNPFirst",PROBNPFirst)

PROCALCITONINFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Pro-calcitonin") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    PROCALCITONINFirst.append(tmpm)
    tmpm=""
print("PROCALCITONINFirst",PROCALCITONINFirst)

Dffinal21= Dffinal20.assign(TROPONINEFirst=TROPONINEFirst, CKMBFirst=CKMBFirst, PROBNPFirst=PROBNPFirst, PROCALCITONINFirst=PROCALCITONINFirst)
Dffinal21.head()
PTTFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="PTT") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    PTTFirst.append(tmpm)
    tmpm=""
print("PTTFirst",PTTFirst)

PTFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="PT") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    PTFirst.append(tmpm)
    tmpm=""
print("PTFirst",PTFirst)

NAMEINRFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="INR") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    NAMEINRFirst.append(tmpm)
    tmpm=""
print("NAMEINRFirst",NAMEINRFirst)

HBSAGFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="HBSAg") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    HBSAGFirst.append(tmpm)
    tmpm=""
print("HBSAGFirst",HBSAGFirst)

HBSAbFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="HBS Ab") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    HBSAbFirst.append(tmpm)
    tmpm=""
print("HBSAbFirst",HBSAbFirst)

HBCAGFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="HBC Ab Total") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    HBCAGFirst.append(tmpm)
    tmpm=""
print("HBCAGFirst",HBCAGFirst)

HCVABFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="HCV Ab  ELISA") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    HCVABFirst.append(tmpm)
    tmpm=""
print("HCVABFirst",HCVABFirst)

HIVABFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="HIV Ab") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    HIVABFirst.append(tmpm)
    tmpm=""
print("HIVABFirst",HIVABFirst)

Dffinal22= Dffinal21.assign(PTTFirst=PTTFirst, PTFirst=PTFirst, NAMEINRFirst=NAMEINRFirst, HBSAGFirst=HBSAGFirst, HBSAbFirst=HBSAbFirst, HBCAGFirst=HBCAGFirst,HCVABFirst=HCVABFirst, HIVABFirst=HIVABFirst)
Dffinal22.head()
NAMEPHFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="PH") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    NAMEPHFirst.append(tmpm)
    tmpm=""
print("NAMEPHFirst",NAMEPHFirst)

NamePh=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="PH") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    NamePh.append(tmpmax)
    tmpmax=""
print("NamePh",NamePh)

NAMEPCO2First=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="PCO2") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    NAMEPCO2First.append(tmpm)
    tmpm=""
print("NAMEPCO2First",NAMEPCO2First)

Namepco2=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="PCO2") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    Namepco2.append(tmpmax)
    tmpmax=""
print("Namepco2",Namepco2)

NAMEHCO3First=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="HCO3") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    NAMEHCO3First.append(tmpm)
    tmpm=""
print("NAMEHCO3First",NAMEHCO3First)

Namehco3=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="HCO3") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    Namehco3.append(tmpmax)
    tmpmax=""
print("Namehco3",Namehco3)

NAMEBEFirst=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Be") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    NAMEBEFirst.append(tmpm)
    tmpm=""
print("NAMEBEFirst",NAMEBEFirst)

Namebe=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="BE") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    Namebe.append(tmpmax)
    tmpmax=""
print("Namebe",Namebe)

Dffinal23= Dffinal22.assign(NAMEPHFirst=NAMEPHFirst, NamePh=NamePh, NAMEPCO2First=NAMEPCO2First, Namepco2=Namepco2,NAMEHCO3First=NAMEHCO3First, Namehco3=Namehco3,NAMEBEFirst=NAMEBEFirst, Namebe=Namebe)
Dffinal23.head()
#############################################################################################
BloodGroup=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="ABO") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    BloodGroup.append(tmpm)
    tmpm=""
print("BloodGroup",BloodGroup)

ANA=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="ANA") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    ANA.append(tmpm)
    tmpm=""
print("ANA",ANA)

CANCA=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="C ANCA") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    CANCA.append(tmpm)
    tmpm=""
print("CANCA",CANCA)

PANCA=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="P ANCA") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    PANCA.append(tmpm)
    tmpm=""
print("PANCA",PANCA)

directCombs=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Coombs direct") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    directCombs.append(tmpm)
    tmpm=""
print("directCombs",directCombs)


indirectCombs=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="indirect coombs") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    indirectCombs.append(tmpm)
    tmpm=""
print("indirectCombs",indirectCombs)

FDP=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="FDP") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    FDP.append(tmpm)
    tmpm=""
print("FDP",FDP)

Fe=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Fe") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    Fe.append(tmpm)
    tmpm=""
print("Fe",Fe)

Ferritin=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Ferritin") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    Ferritin.append(tmpm)
    tmpm=""
print("Ferritin",Ferritin)

TIBC=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="TIBC") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    TIBC.append(tmpm)
    tmpm=""
print("TIBC",TIBC)

TotalProtein=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Total Protein") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    TotalProtein.append(tmpm)
    tmpm=""
print("TotalProtein",TotalProtein)

TSH=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="TSH CLIA") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    TSH.append(tmpm)
    tmpm=""
print("TSH",TSH)

T4=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="T4 CLIA") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    T4.append(tmpm)
    tmpm=""
print("T4",T4)

T3=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="T3 CLIA") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    T3.append(tmpm)
    tmpm=""
print("T3",T3)

VitD3=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="25- Vitamin D3") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    VitD3.append(tmpm)
    tmpm=""
print("VitD3",VitD3)

Zinc=[]
for idxf,iddf in enumerate(dffinal["id"]):
    firstidx =70000 # chon har sheet 65 hezaratas gozashtam 70000
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="Zinc") and (idx<firstidx):
            tmpm=df4.iloc[idx,2]
            firstidx = idx
    Zinc.append(tmpm)
    tmpm=""
print("Zinc",Zinc)

IgM=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="IgM ELISA") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    IgM.append(tmpmax)
    tmpmax=""
print("IgM",IgM)

IgG=[]
for idxf,iddf in enumerate(dffinal["id"]):
    lastidx =0
    for idx,idd in enumerate(df4["id"]):
        if (idd==iddf) and (df4.iloc[idx,1]=="IgG ELISA") and (idx>lastidx):
            tmpmax=df4.iloc[idx,2]
            lastidx = idx
    IgG.append(tmpmax)
    tmpmax=""
print("IgG",IgG)

Dffinal24= Dffinal23.assign(BloodGroup=BloodGroup, ANA=ANA, CANCA=CANCA, PANCA=PANCA, directCombs=directCombs, indirectCombs=indirectCombs, 
                            FDP=FDP, Fe=Fe,Ferritin=Ferritin, TIBC=TIBC,TotalProtein=TotalProtein,TSH=TSH,
                            T4=T4,T3=T3,VitD3=VitD3,Zinc=Zinc,IgM=IgM,IgG=IgG)
Dffinal24.head()


Dffinal24.to_excel("C:\DOCUMENTS\MY WORK\MaGHALE\Big COVID PROJECT\Shohada\Sheetsbypythone\sheet7.xlsx")
