import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import openpyxl

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)

#define name of hospital in databases, this will be used in the future
hospital_name="Emam"

if hospital_name=="Emam":
    WBCLabstring= 'W.B.C'
    LymphLabstring='Lymphocytes'
    NeutLabstring='Neutrophils'
    pltLabstring='PLT'
    hmglbnLabstring='Hb'
    mcvLabstring='MCV'
    ureaLabstring='Urea'
    CrLabstring='Creatinine'
    NaLabstring1='Serum Na'
    NaLabstring2='Whole Blood Na'
    KLabstring1='Serum K'
    KLabstring2='Whole Blood K'
    CaLabstring='Ca'
    MgLabstring='Mg'
    PLabstring='Phosphorus'
    ASTLabstring='AST'
    ALTLabstring='ALT'
    AlkPLabstring='ALk P'
    BillTotalLabstring='Bilirubin T'
    BillDirectLabstring='Bilirubin D'
    AmylaseLabstring='Amylase'
    LipaseLabstring='Lipase'
    TGLabstring='Triglyceride'
    CholesterolLabstring='Cholesterol'
    HDLLabstring='HDL-C'
    LDLLabstring='LDL-C'
    FBSLabstring='FBS'
    Hba1cLabstring='HbA1C'
    AlbuminLabstring='Alb Serum'
    LDHLabstring='LDH Serum'
    CRPLabstring='CRP - Quantitative'
    ESRLabstring='ESR'
    LactateLabstring='Lactate'
    IL6Labstring='Interleukin 6'
    CPKLabstring='CPK'
    DdimerLabstring='D-Dimer'
    TroponinLabstring='Troponin'
    CKMBLabstring='CK MB'
    ProBNPLabstring='NT-PRO-BNP'
    ProcalcitoninLabstring='Procalcitonin.PCT'
    PTTLabstring='PTT'
    PTLabstring='PT Patient'
    INRLabstring='INR'
    HBSAGLabstring='HBS Ag'
    HBsABLabstring='HBS Ab'
    HBCAbLabstring='HBC Ab Total'
    HCVAbLabstring='HCV Ab'
    HIVAbLabstring='HIV Ab'
    PhLabstring='*PH'
    PCO2Labstring='pCO2'
    HCO3Labstring='HCO3'
    BELabstring='BE'
    BloodgroupABOLabstring='ABO'
    BloodgroupRhLabstring='Rh'
    ANALabstring='ANA'
    CANCALabstring='C-ANCA (PR3)'
    PANCALabstring='P-ANCA (Anti MPO)'
    DirectCombsLabstring='Coombs direct'
    indirectCombsLabstring='Coombs indirect'
    FDPLabstring='FDP'
    FeLabstring='Fe'
    FerritinLabstring='Ferritin'
    TIBCLabstring='TIBC'
    TotalProteinLabstring='Protein Total'
    TSHLabstring='TSH'
    T4Labstring='FT4'
    T3Labstring='T3'
    VitD3Labstring='Vitamin D3'
    ZincLabstring='Zinc'
    IgMLabstring='IgM'
    IgGLabstring='IgG'
    SARSCOV2EgeneLabstring='SARS-Cov-2(E.gene)'
    SARSCOV2RDRPLabstring='SARS-Cov-2(RDRP)'
    print("labratory names are defined for emam hospital")
if hospital_name=="Loghman":
    WBCLabstring= 'WBC'
    LymphLabstring='Lymphocytes'
    NeutLabstring='Segmented Neutrophils'
    pltLabstring= 'Platelets'
    hmglbnLabstring='Hemoglobin'
    mcvLabstring='MCV'
    ureaLabstring='Urea'
    CrLabstring='Cr'
    NaLabstring= 'Na' 
    KLabstring='K' 
    CaLabstring=  'Calcium'
    MgLabstring='Mg'
    PLabstring='Phosphorus'
    ASTLabstring='SGOT AST'
    ALTLabstring='SGPT ALT'
    AlkPLabstring='ALP'
    BillTotalLabstring='Bilirubin, total'
    BillDirectLabstring='Bilirubin, direct'
    AmylaseLabstring='Amylase'
    LipaseLabstring='Lipase'
    TGLabstring='TG'
    CholesterolLabstring='Cholesterol'
    HDLLabstring='HDL-C'
    LDLLabstring='LDL-C'
    FBSLabstring='FBS'
    Hba1cLabstring= 'HbA1C'
    AlbuminLabstring='Albumin'
    LDHLabstring='LDH'
    CRPLabstring= 'CRP  quantitative'
    ESRLabstring='ESR'
    LactateLabstring='Lactate-EDTA'
    IL6Labstring='Interleukin 6-SERUM'
    CPKLabstring='CPK'
    DdimerLabstring='D-Dimer'
    TroponinLabstring='Troponin high-sensitivity'
    CKMBLabstring='CK-MB'
    ProBNPLabstring='NT-PRO BNP EDTA'
    ProcalcitoninLabstring="procalcitonin"
    PTTLabstring='PTT'
    PTLabstring='PT'
    INRLabstring='INR'
    HBSAGLabstring='HBsAg'
    HBsABLabstring='HBsAb'
    HBCAbLabstring= 'Anti Hbc Ab total'
    HCVAbLabstring= 'Anti HCV'
    HIVAbLabstring='HIV 1/2 Ab'
    PhLabstring='pH'
    PCO2Labstring='PCO2'
    HCO3Labstring='HCO3-'
    BELabstring='BE'
    BloodgroupABOLabstring='Blood Group&Rh'
    BloodgroupRhLabstring='Blood Group&Rh'
    ANALabstring='ANA'
    CANCALabstring= 'C-ANCA  PR3'
    PANCALabstring= 'P-ANCA MPO'
    DirectCombsLabstring='Coombs Direct-EDTA'
    indirectCombsLabstring='Coombs Indirect'
    FDPLabstring='FDP-citrate'
    FeLabstring='Iron'
    FerritinLabstring='Ferritin'
    TIBCLabstring='TIBC'
    TotalProteinLabstring='Total Protein'
    TSHLabstring='TSH  EIA'
    T4Labstring='T4 EIA'
    T3Labstring='T3 EIA'
    VitD3Labstring='25OH Vit D3'
    ZincLabstring='Zinc-Zn'
    IgMLabstring='IgM'
    IgGLabstring='IgG'
    SARSCOV2EgeneLabstring="Egene"
    SARSCOV2RDRPLabstring="RDRP"
    print("labratory names are defined for loghman hospital")

# read patient database
Pts_File_Adres='/media/sdamirsa/Documents/MY WORK/MaGHALE/Big COVID phase 2/Data_Medical/Phase 2.xlsx'
dfasli=pd.read_excel(Pts_File_Adres, sheet_name='Cleaned E4')
dfasli=dfasli[dfasli['Hospital_x']==hospital_name]
dfasli

# read labratories from 14 excel sheets

Lab_File_Adres='/media/sdamirsa/Documents/MY WORK/MaGHALE/Big COVID phase 2/Data_Labs/Emam/covid student.xls'

​

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

​

dfcodes= pd.concat([df0, df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13])

dfcodes = dfcodes.rename(columns={0: 'Labname', 1: 'Result',2:'Date',3:'id'})

dfcodes

​

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

​

#Keeping yyyy/mm/dd and removing time

Date_clean=[]

for i in dfcodes['Date']:

    x=i[0:10]

    Date_clean.append(x)

dfcodes['Date']=Date_clean

​

# calculating dat from 0 (for calulating delta considering different days in a month in solari hijri calender)

Tarikh_be_roz=[]

for x in dfcodes['Date']:

    Date_roz_bastari = tarikhberoz(x)

    Tarikh_be_roz.append(Date_roz_bastari)

    

dfcodes = dfcodes.assign (Tarikh_be_roz = Tarikh_be_roz )

dfcodes

​

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

​

# calculating dat from 0 (for calulating delta considering different days in a month in solari hijri calender)

x=len(dfasli.index)

dfasli=dfasli.dropna(subset='Date')

dfasli.index = range(len(dfasli.index))

y=len(dfasli.index)

number_or_errors=x-y

print (number_or_errors)

dfasli

​

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

​

dfcodes["delta"] = ""

Delta=0

for idx,idd in enumerate(dfcodes["id"]):

    for idxBastari,iddBastari in enumerate(dfasli["id"]):

        if idd==iddBastari:

            Delta= (dfcodes.Tarikh_be_roz[idx]-dfasli.Tarikh_be_roz[idxBastari])+1

            dfcodes.delta[idx] = Delta

dfcodes

#finding patients with valid labratory exam AND  clincal exam for specific hospital 

​

included_id=[]

labids= dfcodes['id'].unique()

labids=labids.tolist()

for i in labids:

    for x in dfasli['id']:

        if i==x:

            included_id.append(i)

print(len(included_id))

print(included_id)

​

​

#create the structure for final dataframe =output

d = {'id':included_id}

dffinalmother = pd.DataFrame(d)

dffinal=dffinalmother

df1=pd.DataFrame({'id':dfcodes['id'], 'Labname':dfcodes['Labname'], 'Result':dfcodes['Result'],'Date':dfcodes['Date'],

                  'panj':np.nan,'shesh': np.nan, 'delta': dfcodes['delta']})

df1

deltastring=[]

for i in df1['delta']:

    i=str(i)

    deltastring.append(i)

df1['delta']=deltastring

df1["name_delta"] = df1[["Labname", "delta"]].apply("-".join, axis=1)

df1

after two years finally find a good soloution for the problem, I previously coded 2000 codes to reach same result

GOGO_mother=pd.DataFrame() for i in included_id: GOGO=df4[df4['id']==i] GOGO_wide=pd.pivot_table(GOGO, index='id', columns=['name_delta'], values=['Result'], aggfunc=lambda x: x.iloc[-1]) GOGO_mother=pd.concat([GOGO_mother,GOGO_wide], axis=1) print(len(GOGO_mother)) GOGO_mother

GOGO_mother.to_csv('/home/sdamirsa/Desktop/GOGOishere_Emam.csv')

##################################################################################

# now we will use previous model (just to assure phase 1 and phase 2 had been done with same method)

# to increase the speed we will first exclude cases with different Labname

# we created df4mother to keep it from change

df4mother=df1

df4mother['delta']=pd.to_numeric(df4mother['delta'])

df4mother

df4mother['Labname'].unique()

WBCLabstring= 'W.B.C' LymphLabstring='Lymphocytes' NeutLabstring='Neutrophils' pltLabstring='PLT' hmglbnLabstring='Hb' mcvLabstring='MCV' ureaLabstring='Urea' CrLabstring='Creatinine' NaLabstring1='Serum Na' NaLabstring2='Whole Blood Na' KLabstring1='Serum K' KLabstring2='Whole Blood K' CaLabstring='Ca' MgLabstring='Mg' PLabstring='Phosphorus' ASTLabstring='AST' ALTLabstring='ALT' AlkPLabstring='ALk P' BillTotalLabstring='Bilirubin T' BillDirectLabstring='Bilirubin D' AmylaseLabstring='Amylase' LipaseLabstring='Lipase' TGLabstring='Triglyceride' CholesterolLabstring='Cholesterol' HDLLabstring='HDL-C' LDLLabstring='LDL-C' FBSLabstring='FBS' Hba1cLabstring='HbA1C' AlbuminLabstring='Alb Serum' LDHLabstring='LDH Serum' CRPLabstring='CRP - Quantitative' ESRLabstring='ESR' LactateLabstring='Lactate' IL6Labstring='Interleukin 6' CPKLabstring='CPK' DdimerLabstring='D-Dimer' TroponinLabstring='Troponin' CKMBLabstring='CK MB' ProBNPLabstring='NT-PRO-BNP' ProcalcitoninLabstring='Procalcitonin.PCT' PTTLabstring='PTT' PTLabstring='PT Patient' INRLabstring='INR' HBSAGLabstring='HBS Ag' HBsABLabstring='HBS Ab' HBCAbLabstring='HBC Ab Total' HCVAbLabstring='HCV Ab' HIVAbLabstring='HIV Ab' PhLabstring='*PH' PCO2Labstring='pCO2' HCO3Labstring='HCO3' BELabstring='BE' BloodgroupABOLabstring='ABO' BloodgroupRhLabstring='Rh' ANALabstring='ANA' CANCALabstring='C-ANCA (PR3)' PANCALabstring='P-ANCA (Anti MPO)' DirectCombsLabstring='Coombs direct' indirectCombsLabstring='Coombs indirect' FDPLabstring='FDP' FeLabstring='Fe' FerritinLabstring='Ferritin' TIBCLabstring='TIBC' TotalProteinLabstring='Protein Total' TSHLabstring='TSH' T4Labstring='FT4' T3Labstring='T3' VitD3Labstring='Vitamin D3' ZincLabstring='Zinc' IgMLabstring='IgM' IgGLabstring='IgG' SARSCOV2EgeneLabstring='SARS-Cov-2(E.gene)' SARSCOV2RDRPLabstring='SARS-Cov-2(RDRP)'

df4=df4mother[df4mother['Labname']==WBCLabstring]

df4.index = range(len(df4.index))

df4

​

WBCFinal=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    WBCFinal.append(tmpmax)

    tmpmax=""

print("WBCFinal",WBCFinal)

​

WBC1=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==2):

            tmp2 = df4.iloc[idx,2]

            WBC1.append(tmp2)

            break

    else:

        WBC1.append("")

print("WBC1",WBC1)

​

WBC2=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==2):

            tmp2 = df4.iloc[idx,2]

            WBC2.append(tmp2)

            break

    else:

        WBC2.append("")

print("WBC2",WBC2)

​

WBC3=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and  (df4.iloc[idx,6]==3):

            tmp3 = df4.iloc[idx,2]

            WBC3.append(tmp3)

            break

    else:

        WBC3.append("")

print("WBC3",WBC3)

​

WBC4=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==4):

            tmp4 = df4.iloc[idx,2]

            WBC4.append(tmp4)

            break

    else:

        WBC4.append("")

print("WBC4",WBC4)

​

WBC5=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==5):

            tmp5 = df4.iloc[idx,2]

            WBC5.append(tmp5)

            break

    else:

        WBC5.append("")

print("WBC5",WBC5)

WBC6=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and  (df4.iloc[idx,6]==6):

            tmp6 = df4.iloc[idx,2]

            WBC6.append(tmp6)

            break

    else:

        WBC6.append("")

print("WBC6",WBC6)

​

dffinal2= dffinal.assign(WBC1=WBC1, WBC2=WBC2, WBC3=WBC3, WBC4=WBC4,WBC5=WBC5, WBC6=WBC6,WBCFinal=WBCFinal)

dffinal2.head()

df4=df4mother[df4mother['Labname']==LymphLabstring]

df4.index = range(len(df4.index))

df4

​

​

NAMELYMPHH1=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==1):

            tmp1 = df4.iloc[idx,2]

            NAMELYMPHH1.append(tmp1)

            break

    else:

        NAMELYMPHH1.append("")

print("NAMELYMPHH1",NAMELYMPHH1)

​

NAMELYMPHH2=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==2):

            tmp2 = df4.iloc[idx,2]

            NAMELYMPHH2.append(tmp2)

            break

    else:

        NAMELYMPHH2.append("")

print("NAMELYMPHH2",NAMELYMPHH2)

​

NAMELYMPHH3=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==3):

            tmp3 = df4.iloc[idx,2]

            NAMELYMPHH3.append(tmp3)

            break

    else:

        NAMELYMPHH3.append("")

print("NAMELYMPHH3",NAMELYMPHH3)

​

NAMELYMPHH4=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==4):

            tmp4 = df4.iloc[idx,2]

            NAMELYMPHH4.append(tmp4)

            break

    else:

        NAMELYMPHH4.append("")

print("NAMELYMPHH4",NAMELYMPHH4)

​

NAMELYMPHH5=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==5):

            tmp5 = df4.iloc[idx,2]

            NAMELYMPHH5.append(tmp5)

            break

    else:

        NAMELYMPHH5.append("")

print("NAMELYMPHH5",NAMELYMPHH5)

NAMELYMPHH6=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==6):

            tmp6 = df4.iloc[idx,2]

            NAMELYMPHH6.append(tmp6)

            break

    else:

        NAMELYMPHH6.append("")

print("NAMELYMPHH6",NAMELYMPHH6)

​

NAMELYMPHHFinal=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    NAMELYMPHHFinal.append(tmpmax)

    tmpmax=""

​

Dffinal3= dffinal2.assign(NAMELYMPHH1=NAMELYMPHH1, NAMELYMPHH2=NAMELYMPHH2, NAMELYMPHH3=NAMELYMPHH3, NAMELYMPHH4=NAMELYMPHH4,NAMELYMPHH5=NAMELYMPHH5, NAMELYMPHH6=NAMELYMPHH6,NAMELYMPHHFinal=NAMELYMPHHFinal)

Dffinal3.head()

df4=df4mother[df4mother['Labname']==NeutLabstring]

df4.index = range(len(df4.index))

df4

​

NAMENEUT1=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and  (df4.iloc[idx,6]==1):

            tmp1 = df4.iloc[idx,2]

            NAMENEUT1.append(tmp1)

            break

    else:

        NAMENEUT1.append("")

print("NAMENEUT1",NAMENEUT1)

​

NAMENEUT2=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==2):

            tmp2 = df4.iloc[idx,2]

            NAMENEUT2.append(tmp2)

            break

    else:

        NAMENEUT2.append("")

print("NAMENEUT2",NAMENEUT2)

​

NAMENEUT3=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==3):

            tmp3 = df4.iloc[idx,2]

            NAMENEUT3.append(tmp3)

            break

    else:

        NAMENEUT3.append("")

print("NAMENEUT3",NAMENEUT3)

​

NAMENEUT4=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and  (df4.iloc[idx,6]==4):

            tmp4 = df4.iloc[idx,2]

            NAMENEUT4.append(tmp4)

            break

    else:

        NAMENEUT4.append("")

print("NAMENEUT4",NAMENEUT4)

​

NAMENEUT5=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==5):

            tmp5 = df4.iloc[idx,2]

            NAMENEUT5.append(tmp5)

            break

    else:

        NAMENEUT5.append("")

print("NAMENEUT5",NAMENEUT5)

NAMENEUT6=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==6):

            tmp6 = df4.iloc[idx,2]

            NAMENEUT6.append(tmp6)

            break

    else:

        NAMENEUT6.append("")

print("NAMENEUT6",NAMENEUT6)

​

NAMENEUTFinal=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    NAMENEUTFinal.append(tmpmax)

    tmpmax=""

print("NAMENEUTFinal",NAMENEUTFinal)

​

Dffinal4= Dffinal3.assign(NAMENEUT1=NAMENEUT1, NAMENEUT2=NAMENEUT2, NAMENEUT3=NAMENEUT3, NAMENEUT4=NAMENEUT4,NAMENEUT5=NAMENEUT5, NAMENEUT6=NAMENEUT6,NAMENEUTFinal=NAMENEUTFinal)

Dffinal4.head()

df4=df4mother[df4mother['Labname']==pltLabstring]

df4.index = range(len(df4.index))

df4

​

​

NAMEPLT1=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==1):

            tmp1 = df4.iloc[idx,2]

            NAMEPLT1.append(tmp1)

            break

    else:

        NAMEPLT1.append("")

print("NAMEPLT1",NAMEPLT1)

​

NAMEPLT2=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==2):

            tmp2 = df4.iloc[idx,2]

            NAMEPLT2.append(tmp2)

            break

    else:

        NAMEPLT2.append("")

print("NAMEPLT2",NAMEPLT2)

​

NAMEPLT3=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==3):

            tmp3 = df4.iloc[idx,2]

            NAMEPLT3.append(tmp3)

            break

    else:

        NAMEPLT3.append("")

print("NAMEPLT3",NAMEPLT3)

​

NAMEPLT4=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and  (df4.iloc[idx,6]==4):

            tmp4 = df4.iloc[idx,2]

            NAMEPLT4.append(tmp4)

            break

    else:

        NAMEPLT4.append("")

print("NAMEPLT4",NAMEPLT4)

​

NAMEPLT5=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==5):

            tmp5 = df4.iloc[idx,2]

            NAMEPLT5.append(tmp5)

            break

    else:

        NAMEPLT5.append("")

print("NAMEPLT5",NAMEPLT5)

NAMEPLT6=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and  (df4.iloc[idx,6]==6):

            tmp6 = df4.iloc[idx,2]

            NAMEPLT6.append(tmp6)

            break

    else:

        NAMEPLT6.append("")

print("NAMEPLT6",NAMEPLT6)

​

NAMEPLTFinal=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    NAMEPLTFinal.append(tmpmax)

    tmpmax=""

print("NAMEPLTFinal",NAMEPLTFinal)

​

Dffinal5= Dffinal4.assign(NAMEPLT1=NAMEPLT1, NAMEPLT2=NAMEPLT2, NAMEPLT3=NAMEPLT3, NAMEPLT4=NAMEPLT4,NAMEPLT5=NAMEPLT5, NAMEPLT6=NAMEPLT6,NAMEPLTFinal=NAMEPLTFinal)

Dffinal5.head()

df4=df4mother[df4mother['Labname']==hmglbnLabstring]

df4.index = range(len(df4.index))

df4

​

​

NAMEHB1=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==1):

            tmp1 = df4.iloc[idx,2]

            NAMEHB1.append(tmp1)

            break

    else:

        NAMEHB1.append("")

print("NAMEHB1",NAMEHB1)

​

NAMEHB2=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (df4.iloc[idx,6]==2):

            tmp2 = df4.iloc[idx,2]

            NAMEHB2.append(tmp2)

            break

    else:

        NAMEHB2.append("")

print("NAMEHB2",NAMEHB2)

​

NAMEHB3=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and  (df4.iloc[idx,6]==3):

            tmp3 = df4.iloc[idx,2]

            NAMEHB3.append(tmp3)

            break

    else:

        NAMEHB3.append("")

print("NAMEHB3",NAMEHB3)

​

NAMEHB4=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==4):

            tmp4 = df4.iloc[idx,2]

            NAMEHB4.append(tmp4)

            break

    else:

        NAMEHB4.append("")

print("NAMEHB4",NAMEHB4)

​

NAMEHB5=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and  (df4.iloc[idx,6]==5):

            tmp5 = df4.iloc[idx,2]

            NAMEHB5.append(tmp5)

            break

    else:

        NAMEHB5.append("")

print("NAMEHB5",NAMEHB5)

NAMEHB6=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==6):

            tmp6 = df4.iloc[idx,2]

            NAMEHB6.append(tmp6)

            break

    else:

        NAMEHB6.append("")

print("NAMEHB6",NAMEHB6)

​

NAMEHBFinal=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    NAMEHBFinal.append(tmpmax)

    tmpmax=""

print("NAMEHBFinal",NAMEHBFinal)

​

Dffinal6= Dffinal5.assign(NAMEHB1=NAMEHB1, NAMEHB2=NAMEHB2, NAMEHB3=NAMEHB3, NAMEHB4=NAMEHB4,NAMEHB5=NAMEHB5, NAMEHB6=NAMEHB6,NAMEHBFinal=NAMEHBFinal)

Dffinal6.head()

df4=df4mother[df4mother['Labname']==mcvLabstring]

df4.index = range(len(df4.index))

df4

​

NAMEMCV1=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==1):

            tmp1 = df4.iloc[idx,2]

            NAMEMCV1.append(tmp1)

            break

    else:

        NAMEMCV1.append("")

print("NAMEMCV1",NAMEMCV1)

​

NAMEMCV2=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==2):

            tmp2 = df4.iloc[idx,2]

            NAMEMCV2.append(tmp2)

            break

    else:

        NAMEMCV2.append("")

print("NAMEMCV2",NAMEMCV2)

​

NAMEMCV3=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==3):

            tmp3 = df4.iloc[idx,2]

            NAMEMCV3.append(tmp3)

            break

    else:

        NAMEMCV3.append("")

print("NAMEMCV3",NAMEMCV3)

​

NAMEMCV4=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==4):

            tmp4 = df4.iloc[idx,2]

            NAMEMCV4.append(tmp4)

            break

    else:

        NAMEMCV4.append("")

print("NAMEMCV4",NAMEMCV4)

​

NAMEMCV5=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and  (df4.iloc[idx,6]==5):

            tmp5 = df4.iloc[idx,2]

            NAMEMCV5.append(tmp5)

            break

    else:

        NAMEMCV5.append("")

print("NAMEMCV5",NAMEMCV5)

NAMEMCV6=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and  (df4.iloc[idx,6]==6):

            tmp6 = df4.iloc[idx,2]

            NAMEMCV6.append(tmp6)

            break

    else:

        NAMEMCV6.append("")

print("NAMEMCV6",NAMEMCV6)

​

NAMEMCVFinal=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    NAMEMCVFinal.append(tmpmax)

    tmpmax=""

print("NAMEMCVFinal",NAMEMCVFinal)

​

Dffinal7= Dffinal6.assign(NAMEMCV1=NAMEMCV1, NAMEMCV2=NAMEMCV2, NAMEMCV3=NAMEMCV3, NAMEMCV4=NAMEMCV4,NAMEMCV5=NAMEMCV5, NAMEMCV6=NAMEMCV6,NAMEMCVFinal=NAMEMCVFinal)

Dffinal7.head()

df4=df4mother[df4mother['Labname']==ureaLabstring]

df4.index = range(len(df4.index))

df4

​

NAMEUREA1=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (df4.iloc[idx,6]==1):

            tmp1 = df4.iloc[idx,2]

            NAMEUREA1.append(tmp1)

            break

    else:

        NAMEUREA1.append("")

print("NAMEUREA1",NAMEUREA1)

​

NAMEUREA2=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (df4.iloc[idx,6]==2):

            tmp2 = df4.iloc[idx,2]

            NAMEUREA2.append(tmp2)

            break

    else:

        NAMEUREA2.append("")

print("NAMEUREA2",NAMEUREA2)

​

NAMEUREA3=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (df4.iloc[idx,6]==3):

            tmp3 = df4.iloc[idx,2]

            NAMEUREA3.append(tmp3)

            break

    else:

        NAMEUREA3.append("")

print("NAMEUREA3",NAMEUREA3)

​

NAMEUREA4=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (df4.iloc[idx,6]==4):

            tmp4 = df4.iloc[idx,2]

            NAMEUREA4.append(tmp4)

            break

    else:

        NAMEUREA4.append("")

print("NAMEUREA4",NAMEUREA4)

​

NAMEUREA5=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (df4.iloc[idx,6]==5):

            tmp5 = df4.iloc[idx,2]

            NAMEUREA5.append(tmp5)

            break

    else:

        NAMEUREA5.append("")

print("NAMEUREA5",NAMEUREA5)

NAMEUREA6=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (df4.iloc[idx,6]==6):

            tmp6 = df4.iloc[idx,2]

            NAMEUREA6.append(tmp6)

            break

    else:

        NAMEUREA6.append("")

print("NAMEUREA6",NAMEUREA6)

​

NAMEUREAFinal=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    NAMEUREAFinal.append(tmpmax)

    tmpmax=""

print("NAMEUREAFinal",NAMEUREAFinal)

​

Dffinal8= Dffinal7.assign(BUN1=NAMEUREA1, BUN2=NAMEUREA2, BUN3=NAMEUREA3, BUN4=NAMEUREA4,BUN5=NAMEUREA5, BUN6=NAMEUREA6,BUNFinal=NAMEUREAFinal)

Dffinal8.head()

df4=df4mother[df4mother['Labname']==CrLabstring]

df4.index = range(len(df4.index))

df4

​

NAMECR1=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==1):

            tmp1 = df4.iloc[idx,2]

            NAMECR1.append(tmp1)

            break

    else:

        NAMECR1.append("")

print("NAMECR1",NAMECR1)

​

NAMECR2=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==2):

            tmp2 = df4.iloc[idx,2]

            NAMECR2.append(tmp2)

            break

    else:

        NAMECR2.append("")

print("NAMECR2",NAMECR2)

​

NAMECR3=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==3):

            tmp3 = df4.iloc[idx,2]

            NAMECR3.append(tmp3)

            break

    else:

        NAMECR3.append("")

print("NAMECR3",NAMECR3)

​

NAMECR4=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==4):

            tmp4 = df4.iloc[idx,2]

            NAMECR4.append(tmp4)

            break

    else:

        NAMECR4.append("")

print("NAMECR4",NAMECR4)

​

NAMECR5=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==5):

            tmp5 = df4.iloc[idx,2]

            NAMECR5.append(tmp5)

            break

    else:

        NAMECR5.append("")

print("NAMECR5",NAMECR5)

NAMECR6=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==6):

            tmp6 = df4.iloc[idx,2]

            NAMECR6.append(tmp6)

            break

    else:

        NAMECR6.append("")

print("NAMECR6",NAMECR6)

​

NAMECRFinal=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    NAMECRFinal.append(tmpmax)

    tmpmax=""

print("NAMECRFinal",NAMECRFinal)

​

Dffinal9= Dffinal8.assign(NAMECR1=NAMECR1, NAMECR2=NAMECR2, NAMECR3=NAMECR3, NAMECR4=NAMECR4,NAMECR5=NAMECR5, NAMECR6=NAMECR6,NAMECRFinal=NAMECRFinal)

Dffinal9.head()

df4=df4mother[(df4mother['Labname']==NaLabstring1)|(df4mother['Labname']==NaLabstring2)]

df4.index = range(len(df4.index))

df4

​

​

​

NAMENAFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    NAMENAFirst.append(tmpm)

    tmpm=""

    

print("NAMENAFirst",NAMENAFirst)

​

NAMENAFinal=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    NAMENAFinal.append(tmpmax)

    tmpmax=""

print("NAMENAFinal",NAMENAFinal)

​

​

​

Dffinal10= Dffinal9.assign(NAMENAFirst=NAMENAFirst,NAMENAFinal=NAMENAFinal)

Dffinal10.head()

​

df4=df4mother[(df4mother['Labname']==KLabstring1)|(df4mother['Labname']==KLabstring2)]

df4.index = range(len(df4.index))

df4

​

​

NAMEKFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

        

    NAMEKFirst.append(tmpm)

    tmpm=""

print("NAMEKFirst",NAMEKFirst)

​

NAMEKFinal=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    NAMEKFinal.append(tmpmax)

    tmpmax=""

print("NAMEKFinal",NAMEKFinal)

​

​

​

Dffinal11= Dffinal10.assign(NAMEKFirst=NAMEKFirst,NAMEKFinal=NAMEKFinal)

Dffinal11.head()

​

df4=df4mother[df4mother['Labname']==CaLabstring]

df4.index = range(len(df4.index))

df4

​

​

NAMECAFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    NAMECAFirst.append(tmpm)

    tmpm=""

print("NAMECAFirst",NAMECAFirst)

​

df4=df4mother[df4mother['Labname']==MgLabstring]

df4.index = range(len(df4.index))

df4

​

NAMEMGFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    NAMEMGFirst.append(tmpm)

    tmpm=""

print("NAMEMGFirst",NAMEMGFirst)

df4=df4mother[df4mother['Labname']==PLabstring]

df4.index = range(len(df4.index))

df4

​

NAMEPFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    NAMEPFirst.append(tmpm)

    tmpm=""

print("NAMEPFirst",NAMEPFirst)

​

​

Dffinal12= Dffinal11.assign(NAMECAFirst=NAMECAFirst,NAMEMGFirst=NAMEMGFirst,NAMEPFirst=NAMEPFirst)

Dffinal12.head()

df4=df4mother[df4mother['Labname']==ASTLabstring]

df4.index = range(len(df4.index))

df4

​

NAMEAST1=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)and (df4.iloc[idx,6]==1):

            tmp1 = df4.iloc[idx,2]

            NAMEAST1.append(tmp1)

            break

    else:

        NAMEAST1.append("")

print("NAMEAST1",NAMEAST1)

​

NAMEAST2=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==2):

            tmp2 = df4.iloc[idx,2]

            NAMEAST2.append(tmp2)

            break

    else:

        NAMEAST2.append("")

print("NAMEAST2",NAMEAST2)

​

NAMEAST3=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==3):

            tmp3 = df4.iloc[idx,2]

            NAMEAST3.append(tmp3)

            break

    else:

        NAMEAST3.append("")

print("NAMEAST3",NAMEAST3)

​

NAMEAST4=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==4):

            tmp4 = df4.iloc[idx,2]

            NAMEAST4.append(tmp4)

            break

    else:

        NAMEAST4.append("")

print("NAMEAST4",NAMEAST4)

​

NAMEAST5=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==5):

            tmp5 = df4.iloc[idx,2]

            NAMEAST5.append(tmp5)

            break

    else:

        NAMEAST5.append("")

print("NAMEAST5",NAMEAST5)

NAMEAST6=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==6):

            tmp6 = df4.iloc[idx,2]

            NAMEAST6.append(tmp6)

            break

    else:

        NAMEAST6.append("")

print("NAMEAST6",NAMEAST6)

​

NAMEASTFinal=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    NAMEASTFinal.append(tmpmax)

    tmpmax=""

print("NAMEASTFinal",NAMEASTFinal)

​

​

Dffinal13= Dffinal12.assign(NAMEAST1=NAMEAST1, NAMEAST2=NAMEAST2, NAMEAST3=NAMEAST3, NAMEAST4=NAMEAST4,NAMEAST5=NAMEAST5, NAMEAST6=NAMEAST6,NAMEASTFinal=NAMEASTFinal)

Dffinal13.head()

​

df4=df4mother[df4mother['Labname']==ALTLabstring]

df4.index = range(len(df4.index))

df4

​

​

NAMEALT1=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==1):

            tmp1 = df4.iloc[idx,2]

            NAMEALT1.append(tmp1)

            break

    else:

        NAMEALT1.append("")

print("NAMEALT1",NAMEALT1)

​

NAMEALT2=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==2):

            tmp2 = df4.iloc[idx,2]

            NAMEALT2.append(tmp2)

            break

    else:

        NAMEALT2.append("")

print("NAMEALT2",NAMEALT2)

​

NAMEALT3=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==3):

            tmp3 = df4.iloc[idx,2]

            NAMEALT3.append(tmp3)

            break

    else:

        NAMEALT3.append("")

print("NAMEALT3",NAMEALT3)

​

NAMEALT4=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==4):

            tmp4 = df4.iloc[idx,2]

            NAMEALT4.append(tmp4)

            break

    else:

        NAMEALT4.append("")

print("NAMEALT4",NAMEALT4)

​

NAMEALT5=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==5):

            tmp5 = df4.iloc[idx,2]

            NAMEALT5.append(tmp5)

            break

    else:

        NAMEALT5.append("")

print("NAMEALT5",NAMEALT5)

NAMEALT6=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==6):

            tmp6 = df4.iloc[idx,2]

            NAMEALT6.append(tmp6)

            break

    else:

        NAMEALT6.append("")

print("NAMEALT6",NAMEALT6)

​

NAMEALTFinal=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    NAMEALTFinal.append(tmpmax)

    tmpmax=""

print("NAMEALTFinal",NAMEALTFinal)

​

​

Dffinal14= Dffinal13.assign(NAMEALT1=NAMEALT1, NAMEALT2=NAMEALT2, NAMEALT3=NAMEALT3, NAMEALT4=NAMEALT4,NAMEALT5=NAMEALT5, NAMEALT6=NAMEALT6,NAMEALTFinal=NAMEALTFinal)

Dffinal14.head()

df4=df4mother[df4mother['Labname']==AlkPLabstring]

df4.index = range(len(df4.index))

df4

​

NAMEALKPFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    NAMEALKPFirst.append(tmpm)

    tmpm=""

print("NAMEALKPFirst",NAMEALKPFirst)

df4=df4mother[df4mother['Labname']==BillTotalLabstring]

df4.index = range(len(df4.index))

df4

​

NAMEBILLTFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    NAMEBILLTFirst.append(tmpm)

    tmpm=""

print("NAMEBILLTFirst",NAMEBILLTFirst)

​

df4=df4mother[df4mother['Labname']==BillDirectLabstring]

df4.index = range(len(df4.index))

df4

​

NAMEBILLDFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    NAMEBILLDFirst.append(tmpm)

    tmpm=""

print("NAMEBILLDFirst",NAMEBILLDFirst)

df4=df4mother[df4mother['Labname']==AmylaseLabstring]

df4.index = range(len(df4.index))

df4

​

AMYLASEFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    AMYLASEFirst.append(tmpm)

    tmpm=""

print("AMYLASEFirst",AMYLASEFirst)

df4=df4mother[df4mother['Labname']==LipaseLabstring]

df4.index = range(len(df4.index))

df4

​

LIPASEFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    LIPASEFirst.append(tmpm)

    tmpm=""

print("LIPASEFirst",LIPASEFirst)

​

Dffinal15= Dffinal14.assign(NAMEALKPFirst=NAMEALKPFirst, NAMEBILLTFirst=NAMEBILLTFirst, NAMEBILLDFirst=NAMEBILLDFirst, AMYLASEFirst=AMYLASEFirst,LIPASEFirst=LIPASEFirst)

Dffinal15.head()

df4=df4mother[df4mother['Labname']==TGLabstring]

df4.index = range(len(df4.index))

df4

​

​

NAMETGFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    NAMETGFirst.append(tmpm)

    tmpm=""

print("NAMETGFirst",NAMETGFirst)

df4=df4mother[df4mother['Labname']==CholesterolLabstring]

df4.index = range(len(df4.index))

df4

​

CHOLESTROLFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    CHOLESTROLFirst.append(tmpm)

    tmpm=""

print("CHOLESTROLFirst",CHOLESTROLFirst)

df4=df4mother[df4mother['Labname']==HDLLabstring]

df4.index = range(len(df4.index))

df4

​

NAMEHDLFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    NAMEHDLFirst.append(tmpm)

    tmpm=""

print("NAMEHDLFirst",NAMEHDLFirst)

df4=df4mother[df4mother['Labname']==LDLLabstring]

df4.index = range(len(df4.index))

df4

​

NAMELDLFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    NAMELDLFirst.append(tmpm)

    tmpm=""

print("NAMELDLFirst",NAMELDLFirst)

Dffinal16= Dffinal15.assign(NAMETGFirst=NAMETGFirst, CHOLESTROLFirst=CHOLESTROLFirst, NAMEHDLFirst=NAMEHDLFirst, NAMELDLFirst=NAMELDLFirst)

Dffinal16.head()

df4=df4mother[df4mother['Labname']==FBSLabstring]

df4.index = range(len(df4.index))

df4

​

NAMEFBSFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    NAMEFBSFirst.append(tmpm)

    tmpm=""

print("NAMEFBSFirst",NAMEFBSFirst)

df4=df4mother[df4mother['Labname']==Hba1cLabstring]

df4.index = range(len(df4.index))

df4

​

NAMEHBA1CFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    NAMEHBA1CFirst.append(tmpm)

    tmpm=""

print("NAMEHBA1CFirst",NAMEHBA1CFirst)

df4=df4mother[df4mother['Labname']==AlbuminLabstring]

df4.index = range(len(df4.index))

df4

​

ALBUMINFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    ALBUMINFirst.append(tmpm)

    tmpm=""

print("ALBUMINFirst",ALBUMINFirst)

​

Dffinal17= Dffinal16.assign(NAMEFBSFirst=NAMEFBSFirst, NAMEHBA1CFirst=NAMEHBA1CFirst, ALBUMINFirst=ALBUMINFirst)

Dffinal17.head()

​

df4=df4mother[df4mother['Labname']==LDHLabstring]

df4.index = range(len(df4.index))

df4

​

NAMELDH1=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==1):

            tmp1 = df4.iloc[idx,2]

            NAMELDH1.append(tmp1)

            break

    else:

        NAMELDH1.append("")

print("NAMELDH1",NAMELDH1)

​

NAMELDH2=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==2):

            tmp2 = df4.iloc[idx,2]

            NAMELDH2.append(tmp2)

            break

    else:

        NAMELDH2.append("")

print("NAMELDH2",NAMELDH2)

​

NAMELDH3=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==3):

            tmp3 = df4.iloc[idx,2]

            NAMELDH3.append(tmp3)

            break

    else:

        NAMELDH3.append("")

print("NAMELDH3",NAMELDH3)

​

NAMELDH4=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==4):

            tmp4 = df4.iloc[idx,2]

            NAMELDH4.append(tmp4)

            break

    else:

        NAMELDH4.append("")

print("NAMELDH4",NAMELDH4)

​

NAMELDH5=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==5):

            tmp5 = df4.iloc[idx,2]

            NAMELDH5.append(tmp5)

            break

    else:

        NAMELDH5.append("")

print("NAMELDH5",NAMELDH5)

NAMELDH6=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==6):

            tmp6 = df4.iloc[idx,2]

            NAMELDH6.append(tmp6)

            break

    else:

        NAMELDH6.append("")

print("NAMELDH6",NAMELDH6)

​

NAMELDHFinal=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    NAMELDHFinal.append(tmpmax)

    tmpmax=""

print("NAMELDHFinal",NAMELDHFinal)

​

Dffinal18= Dffinal17.assign(NAMELDH1=NAMELDH1, NAMELDH2=NAMELDH2, NAMELDH3=NAMELDH3, NAMELDH4=NAMELDH4,NAMELDH5=NAMELDH5, NAMELDH6=NAMELDH6,NAMELDHFinal=NAMELDHFinal)

Dffinal18.head()

df4=df4mother[df4mother['Labname']==CRPLabstring]

df4.index = range(len(df4.index))

df4

​

NAMECRP1=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==1):

            tmp1 = df4.iloc[idx,2]

            NAMECRP1.append(tmp1)

            break

    else:

        NAMECRP1.append("")

print("NAMECRP1",NAMECRP1)

​

NAMECRP2=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==2):

            tmp2 = df4.iloc[idx,2]

            NAMECRP2.append(tmp2)

            break

    else:

        NAMECRP2.append("")

print("NAMECRP2",NAMECRP2)

​

NAMECRP3=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==3):

            tmp3 = df4.iloc[idx,2]

            NAMECRP3.append(tmp3)

            break

    else:

        NAMECRP3.append("")

print("NAMECRP3",NAMECRP3)

​

NAMECRP4=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==4):

            tmp4 = df4.iloc[idx,2]

            NAMECRP4.append(tmp4)

            break

    else:

        NAMECRP4.append("")

print("NAMECRP4",NAMECRP4)

​

NAMECRP5=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==5):

            tmp5 = df4.iloc[idx,2]

            NAMECRP5.append(tmp5)

            break

    else:

        NAMECRP5.append("")

print("NAMECRP5",NAMECRP5)

NAMECRP6=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==6):

            tmp6 = df4.iloc[idx,2]

            NAMECRP6.append(tmp6)

            break

    else:

        NAMECRP6.append("")

print("NAMECRP6",NAMECRP6)

​

NAMECRPFinal=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    NAMECRPFinal.append(tmpmax)

    tmpmax=""

print("NAMECRPFinal",NAMECRPFinal)

​

Dffinal19= Dffinal18.assign(NAMECRP1=NAMECRP1, NAMECRP2=NAMECRP2, NAMECRP3=NAMECRP3, NAMECRP4=NAMECRP4,NAMECRP5=NAMECRP5, NAMECRP6=NAMECRP6,NAMECRPFinal=NAMECRPFinal)

Dffinal19.head()

df4=df4mother[df4mother['Labname']==ESRLabstring]

df4.index = range(len(df4.index))

df4

​

ESRFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    ESRFirst.append(tmpm)

    tmpm=""

print("ESRFirst",ESRFirst)

df4=df4mother[df4mother['Labname']==LactateLabstring]

df4.index = range(len(df4.index))

df4

​

LACTATEFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

    LACTATEFirst.append(tmpm)

    tmpm=""

print("LACTATEFirst",LACTATEFirst)

​

df4=df4mother[df4mother['Labname']==IL6Labstring]

df4.index = range(len(df4.index))

df4

​

IL6First=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    IL6First.append(tmpm)

    tmpm=""

print("IL6First",IL6First)

df4=df4mother[df4mother['Labname']==CPKLabstring]

df4.index = range(len(df4.index))

df4

​

CPKFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    CPKFirst.append(tmpm)

    tmpm=""

print("CPKFirst",CPKFirst)

df4=df4mother[df4mother['Labname']==DdimerLabstring]

df4.index = range(len(df4.index))

df4

​

DDIMERFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    DDIMERFirst.append(tmpm)

    tmpm=""

print("DDIMERFirst",DDIMERFirst)

Dffinal20= Dffinal19.assign(ESRFirst=ESRFirst, LACTATEFirst=LACTATEFirst, IL6First=IL6First, CPKFirst=CPKFirst,DDIMERFirst=DDIMERFirst)

Dffinal20.head()

df4=df4mother[df4mother['Labname']==TroponinLabstring]

df4.index = range(len(df4.index))

df4

​

TROPONINEFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    TROPONINEFirst.append(tmpm)

    tmpm=""

print("TROPONINEFirst",TROPONINEFirst)

df4=df4mother[df4mother['Labname']==CKMBLabstring]

df4.index = range(len(df4.index))

df4

​

CKMBFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    CKMBFirst.append(tmpm)

    tmpm=""

print("CKMBFirst",CKMBFirst)

df4=df4mother[df4mother['Labname']==ProBNPLabstring]

df4.index = range(len(df4.index))

df4

​

PROBNPFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    PROBNPFirst.append(tmpm)

    tmpm=""

print("PROBNPFirst",PROBNPFirst)

df4=df4mother[df4mother['Labname']==ProcalcitoninLabstring]

df4.index = range(len(df4.index))

df4

​

PROCALCITONINFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    PROCALCITONINFirst.append(tmpm)

    tmpm=""

print("PROCALCITONINFirst",PROCALCITONINFirst)

​

Dffinal21= Dffinal20.assign(TROPONINEFirst=TROPONINEFirst, CKMBFirst=CKMBFirst, PROBNPFirst=PROBNPFirst, PROCALCITONINFirst=PROCALCITONINFirst)

Dffinal21.head()

df4=df4mother[df4mother['Labname']==PTTLabstring]

df4.index = range(len(df4.index))

df4

​

PTTFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    PTTFirst.append(tmpm)

    tmpm=""

print("PTTFirst",PTTFirst)

df4=df4mother[df4mother['Labname']==PTLabstring]

df4.index = range(len(df4.index))

df4

​

PTFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    PTFirst.append(tmpm)

    tmpm=""

print("PTFirst",PTFirst)

df4=df4mother[df4mother['Labname']==INRLabstring]

df4.index = range(len(df4.index))

df4

​

NAMEINRFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    NAMEINRFirst.append(tmpm)

    tmpm=""

print("NAMEINRFirst",NAMEINRFirst)

df4=df4mother[df4mother['Labname']==HBSAGLabstring]

df4.index = range(len(df4.index))

df4

​

HBSAGFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    HBSAGFirst.append(tmpm)

    tmpm=""

print("HBSAGFirst",HBSAGFirst)

df4=df4mother[df4mother['Labname']==HBsABLabstring]

df4.index = range(len(df4.index))

df4

​

HBSAbFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    HBSAbFirst.append(tmpm)

    tmpm=""

print("HBSAbFirst",HBSAbFirst)

df4=df4mother[df4mother['Labname']==HBCAbLabstring]

df4.index = range(len(df4.index))

df4

​

HBCABFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    HBCABFirst.append(tmpm)

    tmpm=""

print("HBCABFirst",HBCABFirst)

df4=df4mother[df4mother['Labname']==HCVAbLabstring]

df4.index = range(len(df4.index))

df4

​

HCVABFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    HCVABFirst.append(tmpm)

    tmpm=""

print("HCVABFirst",HCVABFirst)

df4=df4mother[df4mother['Labname']==HIVAbLabstring]

df4.index = range(len(df4.index))

df4

​

HIVABFirst=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    HIVABFirst.append(tmpm)

    tmpm=""

print("HIVABFirst",HIVABFirst)

Dffinal22= Dffinal21.assign(PTTFirst=PTTFirst, PTFirst=PTFirst, NAMEINRFirst=NAMEINRFirst, HBSAGFirst=HBSAGFirst, HBSAbFirst=HBSAbFirst, HBCABFirst=HBCABFirst,HCVABFirst=HCVABFirst, HIVABFirst=HIVABFirst)

Dffinal22.head()

df4=df4mother[df4mother['Labname']==PhLabstring]

df4.index = range(len(df4.index))

df4

​

​

NAMEPH1=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==1):

            tmp1 = df4.iloc[idx,2]

            NAMEPH1.append(tmp1)

            break

    else:

        NAMEPH1.append("")

print("NAMEPH1",NAMEPH1)

​

NAMEPH2=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==2):

            tmp2 = df4.iloc[idx,2]

            NAMEPH2.append(tmp2)

            break

    else:

        NAMEPH2.append("")

print("NAMEPH2",NAMEPH2)

​

NAMEPH3=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==3):

            tmp3 = df4.iloc[idx,2]

            NAMEPH3.append(tmp3)

            break

    else:

        NAMEPH3.append("")

print("NAMEPH3",NAMEPH3)

​

NAMEPH4=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==4):

            tmp4 = df4.iloc[idx,2]

            NAMEPH4.append(tmp4)

            break

    else:

        NAMEPH4.append("")

print("NAMEPH4",NAMEPH4)

​

NAMEPH5=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==5):

            tmp5 = df4.iloc[idx,2]

            NAMEPH5.append(tmp5)

            break

    else:

        NAMEPH5.append("")

print("NAMEPH5",NAMEPH5)

NAMEPH6=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==6):

            tmp6 = df4.iloc[idx,2]

            NAMEPH6.append(tmp6)

            break

    else:

        NAMEPH6.append("")

print("NAMEPH6",NAMEPH6)

​

NamePh=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    NamePh.append(tmpmax)

    tmpmax=""

print("NamePh",NamePh)

df4=df4mother[df4mother['Labname']==PCO2Labstring]

df4.index = range(len(df4.index))

df4

​

NAMEPCO21=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==1):

            tmp1 = df4.iloc[idx,2]

            NAMEPCO21.append(tmp1)

            break

    else:

        NAMEPCO21.append("")

print("NAMEPCO21",NAMEPCO21)

​

NAMEPCO22=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==2):

            tmp2 = df4.iloc[idx,2]

            NAMEPCO22.append(tmp2)

            break

    else:

        NAMEPCO22.append("")

print("NAMEPCO22",NAMEPCO22)

​

NAMEPCO23=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==3):

            tmp3 = df4.iloc[idx,2]

            NAMEPCO23.append(tmp3)

            break

    else:

        NAMEPCO23.append("")

print("NAMEPCO23",NAMEPCO23)

​

NAMEPCO24=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==4):

            tmp4 = df4.iloc[idx,2]

            NAMEPCO24.append(tmp4)

            break

    else:

        NAMEPCO24.append("")

print("NAMEPCO24",NAMEPCO24)

​

NAMEPCO25=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==5):

            tmp5 = df4.iloc[idx,2]

            NAMEPCO25.append(tmp5)

            break

    else:

        NAMEPCO25.append("")

print("NAMEPCO25",NAMEPCO25)

NAMEPCO26=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==6):

            tmp6 = df4.iloc[idx,2]

            NAMEPCO26.append(tmp6)

            break

    else:

        NAMEPCO26.append("")

print("NAMEPCO26",NAMEPCO26)

​

Namepco2=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    Namepco2.append(tmpmax)

    tmpmax=""

print("Namepco2",Namepco2)

df4=df4mother[df4mother['Labname']==HCO3Labstring]

df4.index = range(len(df4.index))

df4

​

NAMEHCO31=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==1):

            tmp1 = df4.iloc[idx,2]

            NAMEHCO31.append(tmp1)

            break

    else:

        NAMEHCO31.append("")

print("NAMEHCO31",NAMEHCO31)

​

NAMEHCO32=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==2):

            tmp2 = df4.iloc[idx,2]

            NAMEHCO32.append(tmp2)

            break

    else:

        NAMEHCO32.append("")

print("NAMEHCO32",NAMEHCO32)

​

NAMEHCO33=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==3):

            tmp3 = df4.iloc[idx,2]

            NAMEHCO33.append(tmp3)

            break

    else:

        NAMEHCO33.append("")

print("NAMEHCO33",NAMEHCO33)

​

NAMEHCO34=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==4):

            tmp4 = df4.iloc[idx,2]

            NAMEHCO34.append(tmp4)

            break

    else:

        NAMEHCO34.append("")

print("NAMEHCO34",NAMEHCO34)

​

NAMEHCO35=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==5):

            tmp5 = df4.iloc[idx,2]

            NAMEHCO35.append(tmp5)

            break

    else:

        NAMEHCO35.append("")

print("NAMEHCO35",NAMEHCO35)

NAMEHCO36=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==6):

            tmp6 = df4.iloc[idx,2]

            NAMEHCO36.append(tmp6)

            break

    else:

        NAMEHCO36.append("")

print("NAMEHCO36",NAMEHCO36)

​

Namehco3=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    Namehco3.append(tmpmax)

    tmpmax=""

print("Namehco3",Namehco3)

​

df4=df4mother[df4mother['Labname']==BELabstring]

df4.index = range(len(df4.index))

df4

​

NAMEBE1=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==1):

            tmp1 = df4.iloc[idx,2]

            NAMEBE1.append(tmp1)

            break

    else:

        NAMEBE1.append("")

print("NAMEBE1",NAMEBE1)

​

NAMEBE2=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==2):

            tmp2 = df4.iloc[idx,2]

            NAMEBE2.append(tmp2)

            break

    else:

        NAMEBE2.append("")

print("NAMEBE2",NAMEBE2)

​

NAMEBE3=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==3):

            tmp3 = df4.iloc[idx,2]

            NAMEBE3.append(tmp3)

            break

    else:

        NAMEBE3.append("")

print("NAMEBE3",NAMEBE3)

​

NAMEBE4=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==4):

            tmp4 = df4.iloc[idx,2]

            NAMEBE4.append(tmp4)

            break

    else:

        NAMEBE4.append("")

print("NAMEBE4",NAMEBE4)

​

NAMEBE5=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==5):

            tmp5 = df4.iloc[idx,2]

            NAMEBE5.append(tmp5)

            break

    else:

        NAMEBE5.append("")

print("NAMEBE5",NAMEBE5)

NAMEBE6=[]

for idxf,iddf in enumerate(dffinal["id"]):

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (df4.iloc[idx,6]==6):

            tmp6 = df4.iloc[idx,2]

            NAMEBE6.append(tmp6)

            break

    else:

        NAMEBE6.append("")

print("NAMEBE6",NAMEBE6)

​

Namebe=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    Namebe.append(tmpmax)

    tmpmax=""

print("Namebe",Namebe)

Dffinal23= Dffinal22.assign(NAMEPH1=NAMEPH1, NAMEPH2=NAMEPH2, NAMEPH3=NAMEPH3, NAMEPH4=NAMEPH4,NAMEPH5=NAMEPH5, NAMEPH6=NAMEPH6, NamePhlast=NamePh, NAMEPCO21=NAMEPCO21, NAMEPCO22=NAMEPCO22, NAMEPCO23=NAMEPCO23, NAMEPCO24=NAMEPCO24,NAMEPCO25=NAMEPCO25, NAMEPCO26=NAMEPCO26, Namepco2last=Namepco2,NAMEHCO31=NAMEHCO31, NAMEHCO32=NAMEHCO32, NAMEHCO33=NAMEHCO33, NAMEHCO34=NAMEHCO34,NAMEHCO35=NAMEHCO35, NAMEHCO36=NAMEHCO36, Namehco3last=Namehco3,NAMEBE1=NAMEBE1, NAMEBE2=NAMEBE2, NAMEBE3=NAMEBE3, NAMEBE4=NAMEBE4,NAMEBE5=NAMEBE5, NAMEBE6=NAMEBE6, Namebelast=Namebe)

Dffinal23.head()

df4=df4mother[df4mother['Labname']==BloodgroupABOLabstring]

df4.index = range(len(df4.index))

df4

​

BloodGroupABO=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    BloodGroupABO.append(tmpm)

    tmpm=""

print("BloodGroupABO",BloodGroupABO)

​

df4=df4mother[df4mother['Labname']==BloodgroupRhLabstring]

df4.index = range(len(df4.index))

df4

​

BloodGroupRh=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    BloodGroupRh.append(tmpm)

    tmpm=""

print("BloodGroupRh",BloodGroupRh)

df4=df4mother[df4mother['Labname']==ANALabstring]

df4.index = range(len(df4.index))

df4

​

ANA=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    ANA.append(tmpm)

    tmpm=""

print("ANA",ANA)

df4=df4mother[df4mother['Labname']==CANCALabstring]

df4.index = range(len(df4.index))

df4

​

CANCA=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    CANCA.append(tmpm)

    tmpm=""

print("CANCA",CANCA)

df4=df4mother[df4mother['Labname']==PANCALabstring]

df4.index = range(len(df4.index))

df4

​

PANCA=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    PANCA.append(tmpm)

    tmpm=""

print("PANCA",PANCA)

df4=df4mother[df4mother['Labname']==DirectCombsLabstring]

df4.index = range(len(df4.index))

df4

​

directCombs=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    directCombs.append(tmpm)

    tmpm=""

print("directCombs",directCombs)

df4=df4mother[df4mother['Labname']==indirectCombsLabstring]

df4.index = range(len(df4.index))

df4

​

indirectCombs=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    indirectCombs.append(tmpm)

    tmpm=""

print("indirectCombs",indirectCombs)

df4=df4mother[df4mother['Labname']==FDPLabstring]

df4.index = range(len(df4.index))

df4

​

FDP=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    FDP.append(tmpm)

    tmpm=""

print("FDP",FDP)

df4=df4mother[df4mother['Labname']==FeLabstring]

df4.index = range(len(df4.index))

df4

​

Fe=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    Fe.append(tmpm)

    tmpm=""

print("Fe",Fe)

​

df4=df4mother[df4mother['Labname']==FerritinLabstring]

df4.index = range(len(df4.index))

df4

​

Ferritin=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    Ferritin.append(tmpm)

    tmpm=""

print("Ferritin",Ferritin)

df4=df4mother[df4mother['Labname']==TIBCLabstring]

df4.index = range(len(df4.index))

df4

​

TIBC=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    TIBC.append(tmpm)

    tmpm=""

print("TIBC",TIBC)

df4=df4mother[df4mother['Labname']==TotalProteinLabstring]

df4.index = range(len(df4.index))

df4

​

TotalProtein=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    TotalProtein.append(tmpm)

    tmpm=""

print("TotalProtein",TotalProtein)

df4=df4mother[df4mother['Labname']==TSHLabstring]

df4.index = range(len(df4.index))

df4

​

TSH=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    TSH.append(tmpm)

    tmpm=""

print("TSH",TSH)

​

df4=df4mother[df4mother['Labname']==T4Labstring]

df4.index = range(len(df4.index))

df4

​

T4=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    T4.append(tmpm)

    tmpm=""

print("T4",T4)

df4=df4mother[df4mother['Labname']==T3Labstring]

df4.index = range(len(df4.index))

df4

​

T3=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    T3.append(tmpm)

    tmpm=""

print("T3",T3)

df4=df4mother[df4mother['Labname']==VitD3Labstring]

df4.index = range(len(df4.index))

df4

​

VitD3=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    VitD3.append(tmpm)

    tmpm=""

print("VitD3",VitD3)

df4=df4mother[df4mother['Labname']==ZincLabstring]

df4.index = range(len(df4.index))

df4

​

Zinc=[]

for idxf,iddf in enumerate(dffinal["id"]):

    firstidx=len(df4["id"])

    x=0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx<firstidx):

            tmpm=df4.iloc[idx,2]

            firstidx = idx

            x=x+1

    if x==0:

        tmpm=''

    Zinc.append(tmpm)

    tmpm=""

print("Zinc",Zinc)

df4=df4mother[df4mother['Labname']==IgMLabstring]

df4.index = range(len(df4.index))

df4

​

IgM=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf) and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    IgM.append(tmpmax)

    tmpmax=""

print("IgM",IgM)

df4=df4mother[df4mother['Labname']==IgGLabstring]

df4.index = range(len(df4.index))

df4

​

​

IgG=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    IgG.append(tmpmax)

    tmpmax=""

print("IgG",IgG)

df4=df4mother[df4mother['Labname']==SARSCOV2EgeneLabstring]

df4.index = range(len(df4.index))

df4

​

​

SARSCOV2Egene=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    SARSCOV2Egene.append(tmpmax)

    tmpmax=""

print("SARSCOV2Egene",SARSCOV2Egene)

df4=df4mother[df4mother['Labname']==SARSCOV2RDRPLabstring]

df4.index = range(len(df4.index))

df4

​

SARSCOV2RDRP=[]

for idxf,iddf in enumerate(dffinal["id"]):

    lastidx =0

    for idx,idd in enumerate(df4["id"]):

        if (idd==iddf)  and (idx>lastidx):

            tmpmax=df4.iloc[idx,2]

            lastidx = idx

    SARSCOV2RDRP.append(tmpmax)

    tmpmax=""

print("SARSCOV2RDRP",SARSCOV2RDRP)

Dffinal24= Dffinal23.assign(BloodGroupABO=BloodGroupABO, BloodGroupRh=BloodGroupRh, ANA=ANA, CANCA=CANCA, PANCA=PANCA, directCombs=directCombs, indirectCombs=indirectCombs, 

                            FDP=FDP, Fe=Fe,Ferritin=Ferritin, TIBC=TIBC,TotalProtein=TotalProtein,TSH=TSH,

                            T4=T4,T3=T3,VitD3=VitD3,Zinc=Zinc,IgM=IgM,IgG=IgG,SARSCOV2Egene=SARSCOV2Egene,SARSCOV2RDRP=SARSCOV2RDRP)

Dffinal24.head()


