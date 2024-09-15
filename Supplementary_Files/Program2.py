#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 21:44:28 2024

@author: apm
barname 2

"""

#===========================================
#===========================================
#===========================================
#===========================================
#===========================================
#====================L10====================
#===========================================
#===========================================
#===========================================
#===========================================
#===========================================
#===========================================

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd


a_list=list((30,40,50,60,70,80))
a_array=np.array([30,40,50,60,70,80])
a_series=pd.Series([30,40,50,60,70,80])


#structure
#Series(data,index)
a_series=pd.Series([30,40,50,60,70,80],index=['a','b','c','DD','oon','akhari'])

#b che dard mikhore?


#bbin listo numpu mikhasi acces koni
#dovomio mikhasi

a_list[2] #Out[38]: 50
a_array[2] #Out[39]: 50

#hala fk kon 10000 ta index has 

a_series['akhari'] #Out[40]: 80
a_series['c'] #Out[41]: 50


#avalin chizi k sakht --> sereies ---> numppy 1D hast k indexash ma mitonim nam gozari konim

#assign
pd.Series([20,30,40],index=['ali','vahid','reza'])

#ye raveshe dg dare bename dict dictionary

#dictionary
#list []
#dict {}
calories_list=['day1','day2','day3']
calories = {"day1": 420, "day2": 380, "day3": 390}
#esme zarf = 



new=pd.Series([20,30,40],index=['ali','vahid','reza'])

new_dict={'ali':20 , 'vahid':30, 'reza':40}

#dict ro tbdl b serie

convertshode=pd.Series(new_dict)




#===========================
#kholase ye asli
#yechi dahstim bname list


#numpy , array ovord k sari tr bodo do bodi mishod


#pandas omd ychi ovord benaME Series k mitonesim b jaye index ha khodemon y chizi bzarim hala esm bashe adad

#2d?

#omd gof 
#ychizi drm bename DataFrame --> Serie 2  bodi


#********************************



a=np.array([[11,10],[12,20],[13,30],[14,40]])
b=pd.DataFrame(a)
b=pd.DataFrame(a,index=['a','b','c','d'])
#b=pd.DataFrame(a,label=['takane','dama'])

#yekare dg--> dictionary
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

c=pd.DataFrame(data)

c=pd.DataFrame(data,index=['data1','data22','data3'],columns=['ali','vali'])


#access-->
#BE oon radi brsi daghigh mes elisto
#list a[2]
#kasfie bnvisei esmeshpo va esme index

c['data1']


#2d
a2_array=np.array([[30,40,50,60,70,80],[5,6,7,8,9,10]])

a=pd.DataFrame([[10,20,30],[5,4,3],[1,2,3]]) 


#DataFrame hamon Numpy arraye e 2 bodi has
#fght indexo columns balash mitoni adad ya horof bzari




#yeki az rahaye moheme assign
data2 = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

mydf=pd.DataFrame(data2)

mydf=pd.DataFrame(data2,index=['data1','data2','data3'])


#assign ro yd grftim
#baraye acces----

#mese list mese numpy
mydf[0] #KeyError: 0

mydf['data1'] #KeyError: 'data1'

#ina baraye numpy o list bood

mydf.loc['data1']
#calories    420
#duration     50
#Name: data1, dtype: int64


#agar indexat frgh nmikrd ham
mydf.loc[0]


#==================
#assigne value dastiiiiii
#ag yek file dahstim chi? masalan excell bashe ya ya ya


#ye formate kh kh mahboob --> csv
#aval openesh konid

#esme zarf mziri
mydf=pd.read
#inop k mizni harchi formate miare vbarat

mydf=pd.read_csv('C:\\Users\\sunhouse\\Desktop\\data.csv')

#C:\\Users\\sunhouse\\Desktop\\data.csv

#az open estefadekoni b formate csav miad inja

#ama in pd.read_csv -->o oon csv ro mikone yek dataframe

type(mydf) #Out[71]: pandas.core.frame.DataFrame


print(mydf) #vaghty print bzni
#hamon csv file ro miare
#5 ta readife aval 5 ta radife akhar
#paenesham mige chanta radif dar chanta sotoon

#mian esme oon zarfi k zakhire krdno mizanan
#va chnta kar bahash mikonan

#analyse avalie
#mydf file e mane
mydf.head() #5 ta radife avalo
mydf.head(10) #10 taeo miare
mydf.tail()
mydf.tail(10)
#mhemtrin
mydf.info()

#4 ta column (soton drim)
#jolosh nvshte harkodom chanta non-null
#ma ba inkar mibinim k chanta sotonemon null hast ya nan hast
#null o nan yani kahli ya harhcizi --> naghs

#assign
#khodemon dasti midim
#dictionary
#liste --> series
#np array 
#file hast

a=np.array([[1,2,3],[4,5,6]])
b=pd.DataFrame(a,columns=['a','b','c'])

#dastresi
#dota dastresi
#ya mikhay b indexi brsi loc
b.loc[0]
#a    1
#b    2
#c    3
#Name: 0, dtype: int32

#age column sotonio mikham
#esme moteghayed yni dataframemon ye [] dakhelesh esme sotonm
b['a']
#0    1
#1    4
#Name: a, dtype: int32


#preprocesign --> ghable farayanad

#analys mikonim dataro



#--------initial analysis ( analize avalie )----------------------

#azinja bbad analyse nahaee -- DATA CLEANING - PAKSAZIE DATA-----------
#---DATA CLEANING-------
#hamishe datahmon baraye hsohe masnooe ya film ( nadeer) , ax 
#dataa ( hamon adad) --> formatesh chie? word, excell , csv(hjmishe)

#formatesh pas na array hast na pd hast na hichiii

#ama mitonim ba read_format --> tbdilesh konim bn dataframe

#aval initial analysis miznim

#naghs dr datahmon
#1-empty cfell ( khali bashe)
#2-wrong format
#3-wrong data 
#4-duplicated (tekrari)


#pas dar datahmon 4 ta naghs drim



#harja khali bashe moshkel dar convert open bashe 
#NAN= not a number

#ag bjaye str zade adsad -- wrong fromat

#baste b application , 

#wrong data
#masalan y kari mikonim bayad damaha hame beyne 20 ta 60 bashe

#ag jaee zade shode bashe 700 --> ghalate
#in ghalat shayd bkhtre dastgahe , nemname , kasi k type krde , convert , 
#mohem nis ressource manabe khata mohyem nis

#mohem ine ke yek naghsi dr data hast
#hala yki az in charta 1-empty cell (nan) 2-wrong format (bjaye str int)
#3-duplicated (tekrari has) 4-wrong data ( rangesh frgh mikone y aya)



#dr in soorat avalin akremon in bod k ba info mididm k chnta mpty drim

#deoone donne mikhaym brim bbinim chjikaresh konm

#-----empty cell------------------
#aval info miznim mibinim khob dare dg
#marhale1-bfhmim null darim ya na---> info
#marhale 2- agha asan fhmidim hala chikarwesh konim?

#hazdfesh konim?--ag are ok haazf kon
#ya replace konim? --bachi??

#hazf
#kole oon datframeto bnvisi

mydf.dropna() #yani drop kon na number
#ino bzni bayad savesh koni dakhele ye variable e dg

#ama vase rahati
mydf.dropna(inplace=True)
#miad rooye khode mydf emal
mydf.info() #baraye chek krdne

#az 169 ta row , 164 
#hgaashonam shdoan non-null

#be sadegii


#agha nmitonim rotye felan soton inakro konim?
#baraye hazf na********


#replace --> jaygozin kon --> ba chi? chi jahs bzrm?

#jaye tamoome null ha bia

mydf.info()

mydf.fillna(120) #ba in mitoni fill koni 
#tamame noghate khalio ba 120

#ama in khdoesh yek datfrsame e jadid mide emal nmishe

mydf.fillna(120,inplace=True)

mydf.info()
#hamon 160  ta radif monde ama 
#calories , 164 non -null boid alan shode 169 ta yani poresh krdim ma


#masalan fght yek sotono biad empty cell hasho por kone
mydf['Calories'].fillna(120,inplace=True)
mydf['Pulse'].fillna(200,inpalce=True)
#aval ino mzini b kjole soton dastresi peyda mikone


#overview: ya roo kole columnha yani kole dataframe harchi empty cell dre por koni
#y bgi felan soton felan adad felan...

#karhaye ghashngtar
#mean() / median() / mode()


x=mydf['Calories'].mean()
print(x) #368.22248520710065

mydf['Calories'].fillna(x,inplace=True)

#--------------

mydf=pd.read_csv('C:\\Users\\sunhouse\\Desktop\\data.csv')


ffil_df=mydf.fillna(method='ffill')
bfill_df=mydf.fillna(method='bfill')

#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html
#method{‘backfill’, ‘bfill’, ‘ffill’, None}, default None
#Method to use for filling holes in reindexed Series:
#ffill: propagate last valid observation forward to next valid.
#backfill / bfill: use next valid observation to fill gap.


#-----------2wrong format
#str bashe bokonm int
#fek kon yek df drim 
#charta soton dre 1000 ta radif
#yeki az soton ha date hast
#bayad hame injori bnashan '2/6/8'
#ama bazia momkene 2/6/8 adad bashan na str

#minvisi
#avalk mirm toye sotonm
#pd.to yani ino hamashono in format kon
mydf['Date']=pd.to_datetim(mydf['Date'])

#ya hat miutoni az remove estefade koni
#in remove frgh dre

df.dropna(subset=['Date'], inplace = True)


#** tozih




#-----------
import sklearn



#-------QUIZ-----
#VOICE TROZIHESH

'''
bebinid bayad yek tabe besazid ke az taraf
file e csv bgire

yani aval biad ba dastoore zir oono tabdil kone be yek pd.DataFrame

name=pd.read_csv(input)


#badesh yekseri calculation anjam bde ( ya khodesh ya tahiresh bdid b numpy)


va sepas an ra nasb kone

hameye ina bayd dar yek tabe bashe 

mesal: azmayeshe tensile yek testi hast ke miad nemone ro mikeshe
va dar har stress , strain ro andaze giri mikone

nahayat yek file e csv mide ke

1000 ta radif hast k har radif do sotone yek soton strain , yek soton stress

tabeye zir file ro migire va monhanie stress-strain roi mikeshe

va yekser chizaro mananande modole young ham hesab mikone



'''

def magnet_curve(fa):
    mydf=pd.read_csv(fa)
    x=mydf['Applied Magnetic Field']
    y=mydf['Magnetization']
    plt.plot(x,y)
    plt.xlabel('Applied Magnetic Field')
    plt.ylabel('Magnetization')
    plt.show()
    
    
    
    
def Stress_Strain_Curve(input_file,which):
    '''
    This function is belonged to stress strain
    Parameters
    ----------
    input_file : .csv format
        the file must be inserted in csv.
    whcih : str
        please say which work we do ( plot or calculate?).

    '''
    #convert the file
    mydf=pd.read_csv(input_file)
    
    if which=='plot':
        #get the data on each columns
        stress=mydf['stress']
        strain=mydf['strain']
        
        #plotting data
        plt.plot(stress,strain)
        plt.title('stress-strain curve')
        plt.xlabel('stress')
        plt.ylabel('strain')
        plt.show()
    
    
    if which=='max stress':
        #calculat the stress_max
        stress_max=mydf['stress'].max()
        return stress_max

    if which=='young modul':
        #calculate young modul and .....
        return young_module
    
    
    
    
    
    




#===========
#=========
#============
#==============
#==============
#=======L11====#==
#================================
#=====================
#review-----
#python built in function ha
#dastoorat ( if , if else , while , for )
#str,list + method
#random
#def
#numpy
#matplotlib
#pandas-----
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#frghe list numpy
a_list=list((30,40,50,60,70,80))
a_array=np.array([30,40,50,60,70,80])
a_series=pd.Series([3040,50,60,70,80])
a_series=pd.Series([30,40,50,60,70,80],index=['a','b','c','DD','oon','akhari'])
#assign--> dasti bnvbisi/ list bzar / numpy array bzari / data ro import koni / dictonary
#access
a_list[2] #Out[38]: 50
a_array[2] #Out[39]: 50

#pandas
#fght bjaye index esme on index
a_series['akhari'] #Out[40]: 80
new_dict={'ali':20 , 'vahid':30, 'reza':40}
new_dict={'ali':[20,30,40] , 'vahid':[30,40,50], 'reza':[40,50,60]}

#2d --> DataFrame too pandas / 1D--> Series
a=np.array([[11,10],[12,20],[13,30],[14,40]])

#ino tbdil konm b datframe chanta rah dre
#avalin rah--dasti
a=pd.DataFrame([[11,10],[12,20],[13,30],[14,40]])
#dovomin rah--> tabdile arraye b df
new_array=np.array([[11,10],[12,20],[13,30],[14,40]])
a=pd.DataFrame(new_array)
#sevomin rah--> tabdile dict be df
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
a=pd.DataFrame(data)
#4 omin rah--> open the file 
a=pd.read_csv('address')


#4 rtahe dataframe sakhtan ro ayd grftrim
#frghe df ba arr chie?
#mitonim [index radif row ]haro ya [label (column) soton]

#index
#yeki az ravesh haye bala assign kon value ro 
#badesh ....
df=pd.DataFrame([[11,10],[12,20],[13,30],[14,40]],index=['a','salam','taghire khoon','nemoneye4'])

#baraye column ha ya soton ha ya label
df=pd.DataFrame([[11,10],[12,20],[13,30],[14,40]],columns=['vizhegie 1','vizhegie 2'])


#hala cdhijori access konm?
#baraye np array ha-->
arr=np.array([[1,2],[3,4]])
#masalan acces b yek value mikhasim

#esm bad beraket arr[kodom radif, kodom soton]
arr[1,0]

#pd
#ya yek element bkshi biron , ya yek row , yek yek columns
#ag yek soton bekhaym
df['vizhegie 1']
#ag element khasi
df['vizhegie 1'][2]
df['vizhegie 1',2] #KeyError: ('vizhegie 1', 2) mnmitone

#radif mikhay
df.loc[0]

#element mnikham
df.loc[0]['vizhegie 1']
#or
df.loc[0,'vizhegie 1']


#mitonimmm hata az yechizi bname iloc estefade konim
#yani kari dg nadare chi esmesh chie dagghighan mese numpy amal mikoen
#esmefile.[kodom index][kodom soton] hamaro b adad bgo az 0 b badd

df.iloc[0][1]
#or
df.iloc[0,1]

#-------operator
#+
#-
df1=pd.DataFrame([[1,3],[2,4]])
df2=pd.DataFrame([[5,7],[6,8]])

#jam
zarfe_jadid=df1+df2
#df1-df2
#xarb dar yek adad df1*2
#be tavan df1**4

#na tanha kole dataframe ro operate mitoni koni balke mitoni har soton ro ya har radif ro

#dar hame ja baraye acces b 
#************
#tooye pandas ma
#4 ta chiz drim
#1-kole datframe--> df
#2-fght yek radif --> df.loc(9)
#3-fght yek sotonm --> df.['esm']
#4-yek element (yani yedon adad) df.iloc[0,1]

#operat ro rooye kol ya harkodom k bkhay anjham bdi
df1=pd.DataFrame([[1,3],[2,4]])

df3=df1+1



#biay bgi columne avalio inkaro konm baahsh
#**********aval access bad apply
zakhirer=df1[0] +1 
zakhire=df.loc[0]+1

df1=pd.DataFrame([[1,3],[2,4]],columns=['v1','v2'])
                 
#operator haye amari bzni

df1.max() #chonj dota soton drim vase harkodom maximume on sotrono mide

#access apply
df1['v1'].max()

df1.loc[0].max()


#dg harchi paeen miznm 
#shoam mitoni roye kole df , roye yek soiton , roye yek radif ya rooye yek element ejra koni

df1.max(axis=1) #inm baraye oona


df2=df1.T#resizew

#masalan fk kon yek dataframe drim bename air_quality
#chn nemoneye operation

#sakhte yek dsoton

df1['v3']=df1['v1']*2.45


air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
air_quality["ratio_paris_antwerp"] = (
    air_quality["station_paris"] / air_quality["station_antwerp"]
)


#sort--> tartib ddn --> soal mishe man bar ch asas tartib bdm , bar asase kjodom columns

df.sort_values(by="Age")
#yani bia df emon ro sort kon bar asase sotone  Age


#cjoinn , chasbond

df3=pd.concat([df1,df2],axis=0)
#**
#axise 0 yani dar toole ofoghi
#axise 1 dar toole amoodi
mydf=pd.read_csv('C:\\Users\\sunhouse\\Desktop\\data.csv')


#chikar mikone? kole sotone duration ro hazf mikone
mydf.drop(columns='Duration')

#tamame dSTOR HAYE pandas , emal nmishe balke ye df e jadid
#mide va bayad zakhirash koni
#vali hamashon yechi drn bename inplace ag True koni mishe emal
newdf=mydf.drop(columns='Duration')

#or
mydf.drop(columns='Duration',inplace=True)

#ina hazfe soton bod
#hazfe radif chtor?
mydf.drop(index=12)
#m,esle hamishe in dastor ye array pas mide bayad zakhire konim


mydf.drop(index=12,inplace=True)

#ag inplace False bashe true nabashe taghirat rooye df save nmishe




#====analyss================

#vared krdne data
mydf=pd.read_csv('C:\\Users\\sunhouse\\Desktop\\data.csv')
mydf=pd.read_csv('C:\\Users\\sunhouse\\Desktop\\data.csv',index_col=0)
#ag 0 bzni in vase vaghtye ke
#ya mitoni joloye index_col= esme dsotoni kmikhay bar hasbe oon index gzoari bshe

#initiual analasys --> analize avalie
mydf.head() #5 radife avalo
mydf.head(10) 
mydf.tail()#5 taye akhar
mydf.tail(15)
mydf.info() #Initial analysis
#caval mige chanta row drim , entries yani chnta radif drim chanta sample drim chnat nemonde drim
#har soton chantash non-nulle
#bayad non-null ha ba entries barabar basher

#null== dadeye naghes

#===========================bahse cleaning data

#isna
pd.isna(mydf) #vase kochika harja true bashe yani naghese

#----Null chn type drn
#1-nan --> empty cell --> khalie 
#2-formatesh bade
#3-eshtebahe (yani masan damaha nmitonan zire 0K) damamon has -10
#4-dupliocated tekrary repeated

#-------empty
#1-remove
#2-replace ( 1- yek adad dasti , 2-ya mean modian bgiri , 3-methdohaye forward backward)

#remove
mydf.dropna(inplace=True)

#ag replace koni yani fill
mydf.fillna(120)
newdf=mydf.fillna(120)


mydf.fillna(120,inplace=True)


#yadete goftm az chand aspect janbe bbin #in vase kole df ha has
#ag bnkhaym rooye yek column ya yek soton taghir ijad konm chi?
#acces apply

mydf['Calories'].fillna(120,inplace=True)
#yni in soton , harchi khalie ro ba 120 avaz kon


#fotmat frgh kone chi
#miam migim kole oon soton ro b felan format tabdil kon
x=mydf['Calories'].mean()
print(x) #368.22248520710065
mydf['Calories'].fillna(x,inplace=True)


ffil_df=mydf.fillna(method='ffill')
bfill_df=mydf.fillna(method='bfill')


#-----------------
#flash back
#taghire yek element

#103 bod mikham konm 106
mydf.loc[2,'Pulse']=106

#----vaghty yek element eshtebah bshe dakhele data mitoni injori aqvazesh koni

#soal=--> man yad grftm chijori dadeye ghalato wrong data 
#taghir bdm ama khob datam 1 millyard value dre chikar konm

#for o if o ina inja mian bkar

#ghablesh dota chizo yad bgir


mydf.index #listye indexaro mide
mydf.columns #listi az column hato


for x in mydf.index:
    if mydf.loc[x,'Pulse']>200:
        mydf.loc[x,'Pulse']=100
        

#masalan dama

for i in mydf.index:
    if mydf.loc[i,'Tempreture']<-273:
        mydf.loc[i,'Tempreture']=0
        
#repeated ya duplicated
print(mydf.duplicated()) 

mydf.drop_duplicates(inplace = True)




#-----------------------akharin marhale pas az analysis

#vaghty drop mishan index ha bham mikhore *****
mydf.drop(index=4,inplace=True)

#indexa bhm mirize
mydf.reset_index(drop=True,inplace=True) 




#==================
#yechizi drim bname corr
mydf.corr()


#age rabetey soyon haro bkhaym bbinim azin estefade mikonim
#pulse ba pulse / ya x ba x ch rabete ee dre
#x=x / pulse = pulse = pulse = (1)* pulse

#1- rabete mostaghim
#0 yani hcih rabete ee beyneshon nist



#===================
#plot

#mitoniaz matplotlib estefade koni 
#mitoni xnadi
y=mydf['Pulse']
x=np.arange(len(y))

plt.plot(x,y)
plt.show()


#ya mitoni az khode pandas estefade koni
mydf.plot()
plt.show()


#in ke fght plot e sadas ma scatter dahstim vba va

mydf.plot(kind = 'scatter', x = 'Calorie', y = 'Calories')


#---------
import sklearn

#-----------------------------------------------------------
#============================================================
#OVERAL
'''
YEK computer yek mashin hesabe sade hast k az koli 'bit' tashkil shode ke
mohasebat ro ba in bit ha anjam mide yani miad mige har khone (yek khaneye 
jamed) age bargh vasl bashe 1 hast age bargh vasl nabashe 0 hast.
ba in technique e 0 o 1 i (binary) tonestim be yek jesme jamed 0 o 1 yad
bedim vad ba tabdile donyae paye ye 10 be paye ye 2 tonestim hame adad haro
barash besazim.

khob in computer na fahm dare na mitone yad begir na ..
faghat yek mashin hesabe pishraftas hamin.

omadan goftan ma niaz darim kari konim ke machine (computer) betone 
1-yad begire 2-fekr kone 3-tebhe oonn tasmim begire(amal kone)
khob in 3 ta paye ye hooshe masnoee shod

dota nasl hooshe masnooe darim:
    1-nasle aval miomadan migoftan bia ba if-else koli shorot bezarim
    va ba in shart ha betonim yek barname ye control shode besazim
    ba in kar system haye khebre (ke javabe soalaro midad) 
    chat bot haye avalie ke masalan age (if) benevisi salam mige salam
    va hata robot haee k sensorash age masalan felan signalo bede onam
    felan signalo mide va tabdil be harekate mechanici mishe
    
    2-nasle dovom: in nasl ba omadane machine learning oomad yani gfotan 
    bia ye kari konim computer ha betonan yad begiran va khob ba inkar
    soale aval--> az chi yad begiran ? khob az data (badan migim datachie?)
    khob fek kon machine ha betonan az data yad begiran(1*) va badesh tavasote
    yad gerefte hash ba manteghi ke bedast ovorde (2*) betonan pishbini
    konan ya daste bandi konan (tasmim begiran)
    ba in kar system haye khebre kareshono dadan b ChatGPT ba machine learning
    robotic ha ba inakr dg yad grftn yani b morore zaman hata behtar mishan
    
    
khob pas midonim k 70-80% e hooshe masnoee az machine learning omade
in machine learning yani chi ? goftim hoshe masnoe yani
1-yad bgire 2-mantegh kasb kone 3-tasmim bgire
chijori inkaro mikone?

machine elarning yani data driven ( mobtani bar dade)
khob yani data migire --> data ha chian?
data ha daghighan yek data frame hastan ya yek array hastan va ina
chanta radif dare ( tedade nemoone)
hameye in nemone ha chanta soton daran

dar beyne in sotonha , yekserihash vorodi hast yani (x) yani oni ke
ma mitonim taghireh bedim
va yek soton (k mamolan akharin soton) hamon khorojimon (y) hast yani hmaon
parametere mohemi k baramon moheme va oon parametere mohemo mikhaym
besanjim ya .....
khob pas midonim k in x o y beham bastegi daran yani y fght marbote b x
ba taghire x , yek rabete ee beyne x o y hast k y ham taghir mikone nesbat
be hamoon rabete.
mesal: y=2x+1 yani age x=0 bashe, y mishe 1/ hala x o taghir bdi
ba hamin formol y ham taghir mikone pas beyne y va x yek rabete hast
va in rabete hamin formoool hast.

mesale pazhoheshi:
    dar har reshte ee ma dastgahi darim ke yek setting dare ke ma mitonim
    taghiresh bedim va in yechizi khoroji mide k hala khorojish yek adade
    moheme ya oon khoorji ma yek moalefe ee azash ro baraye sanjidane 
    quality (keifiatesh) ya behaviour(raftaresh) dar nazar migirm
    
    masalan dastgahe 3d printing yek chizi dre yek setting ke mitoni
    taghiresh bdi. yek adade beyne 300 ta 400 mitoni taghir bdi
    'taghir'= pas yani in parameter vorodimone (x)
    
    khob ma ba in dastgah masalan ostokhone masnoe, ya organ haye
    masnooe misazim. khob in jesme masnoee ke ma misazim ehtemalan
    mitonim moshakhasate moshakhasi ro biaym azash dar nazar 
    begirim ( characterization) ta betonim befahmim keifiatesh chijorie
    (quality).
    khob in yani khorojimone (y), masalan estehkamesho mikhaym bbinim
    mishe y
    
    khob pas ma yek setting drim taghiresh midim (x emon) k az 300 ta
    400 mtionim taghiresh bedim va module e estehkamesh ham ma mikhaym
    bbinim har dafe ke setting avaz mishe (x) dar asl ostokhoni k sakhte mishe
    estehkamesh baz frgh dre (y)
    
    khob ma miaym hododan 10 ta setting dr nazar migirm hey azmayesh mikonim
    hey khorojiro k estehkamesh has ro misanjim
    yani masalan setting ro 10 ta adad mizarim , 300,310,320,330,340
    350,360,370,380,390
    khob har dafe k setting avaz mishe ehtemalan estehkam avaz mishe
    masalan settinge dastgah ro mizrim 310, estehkam mishe 10000
    bad mikonim 330 masan mishe 20000
    pas datamon chi mishe ? DATA chie?
    yek Data Frame hast k 10 ta radif dare ( tasavoresh konid)
    chera 10 radif? choon 10  ta nemone drim dg yani 10 bar azmayesh ro 
    anjam dadam
    khob in dah radif dota soton dare 
    yek soton settingemone (300-400) hamon x hamon vorodimon
    yek soton estehkmemone yani hamonn y hamn khoroji
    
    data=pd.DataFrame([[300,2000],[310,2300],[320,2600],[330,2800],
                       [340,2900],[350,3200],[360,3400],[370,3600],
                       [380,3800],[390,4000]],
                      columns=['Setting(x)','Estehkam(y)'])
    ino run bznid mishe data framemon dgahighan
    
    khob pas data yani x darim o y [** x ha mitone masalan 3,4 ta soton bashe
                                    yani masalan 3,4 ta setting drim]
    
    hooshe masnooe miad in rabete ye beyne x o y ro yad migire.(chijori?->migim alan)
    khob vaghty in rabete ro yad migire mitone pishbini kone va tasmim bgire
    pas 1-yad grft (az data ha) 2-moadel sakht(mantegh yad grft)3-bar hasbe manteghesh
    mitone pishbni kone (tasmim bgire o amal kone)


    khob khorojimon do no hast 1- mesle mesale bala adade peyvaste yani 
    1230,323032,21231,313,311 ya hata 14,14.22,14.7,14.9
    be in khoroji ha be mosheklemon migim regression

    hala bazi jaya x hamon hamone ama y emon khorojimon adadi nist
    balke masalan mikhaym begim in ostokhon ha gorohe 'a' bazia gorohe
    'b' yani oon 10 ta ostokhon ya gorohe a hastan ya gorohe b

    ya masalan aya mishakann ya na ag beshkanan (yes) ag nashkanan (no)
    ya a o b o yes o no k frgh dnre msn begim 0 ya 1 bashan
    yani in 10 ta data ya gorohe 1 hastan ( gorohi k msihkanan) ya
    gorohe 2 hastan ( gorohi ke ghavian nemishkanan)

    mesal:
        data=pd.DataFrame([[300,'yes'],[310,'no'],[320,'no'],[330,'yes'],
                           [340,'no'],[350,'no'],[360,'yes'],[370,'yes'],
                           [380,'yes'],[390,'no']],
                          columns=['Setting(x)','mishkane?(y)'])
    khob age khoroji gosaste bashe yani maasalann chantae chantae
    khob be in problem ha migan classification (daste bandi)
    

Kholase (summary):
    machine learning yani machine biad az data(?) yad begire(?)va
    
    data chie? yekseri x dare yani vorodi yani chizi k taghiresh 
    mitonim bedim . yekseri y dare yani khoroji yani chize nahaee k moheme
    baramon. va midonim x o y baham yek rabete ee daran yani ag
    x ro taghir bdim y taghir mikone
    
    khob khorojimon ag peyvaste bood --> regression
    age khorojimon gosaste bood---> classification
    


khob berim bebinim regression chie?
***in regressione sadast rabti b hooshe masnooe ndre
#oon bala regression va classification yani regression va classifcione e
hoshe masnooeee/

ama alan mikhaym rajebe regressione sade harf bezanim bebinim chie



Farz konid yek microbubble darim, yani chi yani yek hobabe kheyli kochik
darim ke in hobab ro mikhaym bahash karaee konim. in hobab az esmesh malome
hobabe, yani zood mitereke. yek azmayeshi darim k feshar behesh emal mikonim
yani mizarimesh zire press va miterekonimsh, ye adad mide in dastgah be name
omega. omega yani cheghad tahamol dare in microbubble, hrchi balatar bashe in
omega yani hobabe ghavi tare, yani tahamole bishtari dare yani paydarie
fesharesh bala hast.
ama avalin test ke migirm rooye yek hobab behemon 200 midde omega ke in adad
kheyli kame.
ma nemitonim ba in moghavemato paydari az hobab ha estefade konim dr donyaey vaghe ei
application o karbordesh chie? masalan mikhan toye hobab daroo bezaran bere too
badan. ya azash estefade konan toosh nano mavad ro besazan ya masalan toosh
baraye haffario CO2 captur o ina estefade beshe.
motasefane dar tamame in application ha bayad paydar bashe va khode hobab
age bezarim too kar yeho mitereke.
vase hamin ma miaym tooye in hobab ha yechizi bename 3D graphene mizarim
yani yek made ee fek konid chanta noghte o mavade kochik hast
tazrigh mikonim dakhele micro hobab ha ta paydarish bere bala.

midonim ke khode microbubbl khob dakhelesh graphene nist az aval yani dar asl
0% graphene toshe. khob ma chan drsad graphene toosh vared konim?
aya 10 %? aya 80%? chii?
nemishe goft.
choon shayad masalan age 10 darsad berizim moghavemat ziad she
ama age masalan 40 darsasd berizim. momkene sangini ijad kone toye hobab
va hobab ro beterkone pas yani moosalaman ba afzayeshe graphene hatman
paydari afzayesh nemiabad.
pas yek rabete ee beyne darsade geraphene va paydarie fesharie bubble ha hast.

ma mitonim darsade geraphene ro 'tagghir bdim'--> yani settingesho taghir
bdim->yani in vorodimone --> yani in X emone.
vasamon paydarie feshari ke hamon omega hast moheme--> keifiate nahaee ro
moshakhas mikone--> pas in khorojimone --> yani Y hast

pas ye x o y darim k harmoghe x ro taghir bdim y ham taghir mikone va nemidonim
ke rabete beyne x o y chie daghighan khob ma donbale yek machine hastim ke
betoone in 'rabete' beyne  x o y ro 'yad begire'.

khob khorojimon choon omega hast va peyvaste hast yani 3000,34324,1231 yani
moshekelmon chie ? machine learning regression.

ghabl az inke varessh beshim mikhaym bedonim khode regression che mani ee mide
badesh berim soraghe machine learning regression chon in dota frgh daran.


dar regression, in miad mige khob ma panja dade darim

x=np.array([0,4,8,16,32])
y=np.array([200,310,420,560,630])
ya hata mitone besorate excelo dataframe bashe :
    data=pd.DataFrame([[0,200],[4,310],[8,420],[16,560],[32,630]],columns=['darsad','paydari'])
    #injori x o yemon mishe har kodom az sotonash --> access
    x=data['darsad']
    y=data['paydari']
    
    
baraye rasmesh do rah drim:
    1-plt.scatter(x,y)
    ya
    2-plt.plot(x,y,'o')



rasmehs konido bebinidesh. khob ma midonim ke vaghty x emon yeki az 0 ,
4,8,16,32 bashe khob midonim chie y emon ama khob age bekhaym bbinim x emon 10 bashe
chi?? --> daronyabi behesh migan

age bekhaym bbinid masalan 40 darsad geraphene , paydari chghd mishe ?
behehs migan boron yabi.

khob sade tarin kar ine k biam noghat ro beham dg vasl konim:
    plt.plot(x,y)
khob moshkel ine ke fk konid khodeoton mikhayd har noghte ro b enoghte dg vasl konid
mesle shekle bala
khob vase noghte 40,50 ya balatar mikhayn noghte 32 ro b chi vasl konid?
pas yani boron yabi nmitoni ba inkar konid


#***********************
regressione sade miad mige:

mige bebinid man bekham yek khat bekesham. formole yek khat mishe in
Y=aX+b

mitonid rasm konid bbini

masalan:
    
    x=np.arange(5)
    a=1
    b=1
    y=a*x+b #y=x+1
    plt.plot(x,y)
    
    --------
    x=np.arange(5)
    a=1
    b=0
    y=a*x+b #y=x
    plt.plot(x,y)
    
    --------
    x=np.arange(5)
    a=2
    b=0
    y=a*x+b #y=2x
    plt.plot(x,y)
    
    --------
    x=np.arange(5)
    a=3
    b=4
    y=a*x+b #y=3x+4
    plt.plot(x,y)
    
    
    -----------------------------
    
khob ma faghat ba taghire a va b mitonim hezaran khat bekeshim.
regression mige man miad 1000 ta khat rasm mikonam ba taghire a o b.
chijori? miad aval yek hads mizne yani miad hsansi yek a o b entekhab mikone
masalan a=4 , b=2 masalan formol mishe y=4*x+2 va in khat ro rasm mikone
va haminjori be tartib a o b ro hey rasm mikone.
(soal?= khob chera inhame kaht rasm mkone? ke chi?)

mige man miad inkaro mikonam bad har khat ke rasm krdm . miad faseleye
har noghte ro ta in khat migiramesh R.
badesh vase inke kole fasele haro bebinam
zigma= R1**2 + R2**2 +......
pas in tabeye zigma omade faselehame noghat ro ta in khat hesab krde
be in tabe migan --> cost function

bad inghd hey a o b ro taghir mdie inghd mizare hesab mikone
va paeeen tarin zigma yani chi? paeen tarin zigmna yani
oon khati k paeen tarin zimgma ro dre yani b hame noghat nazdikk tre az beyne
hame khat ha

pas b in kar migan --> optimization ( behine sazi)

pas ba in kar mitone yek khat bedast biare ke a o b sh ro peyda krde
(chijori? hzarta a o b avaz krde hey zigma ro hesab krde
 az beyne oonhame khat oon khati ke kamtarin zigma ro dre omde
 dide ke a o b ish chie va gofte hala in khat
 masalan y=ax+b khate awlie mane)

dg bejaye oon panja noghte ma in khato drim y=ax+b
masaan fk kon a=1 , b=2 in kamtarin fasele ro dashtan ba noghat

miad mige azin bebad har noghte ee
har noghte ( yani beyne range daroon bashe masalan 10 k beyne 8 o 16 e)
ya biron az baze ( yani masalan 40)

mitoni b onvane x bzari too in formol va bdast biari y ro.


ba inkar oomad dar asl yek khat drovord
in khat chie???
nazdiktrin khat be noghat.
khat yani chi?--> yani formol yani hamon y=ax+b
pas dar asl chikar krde??-->omade 'rabete ' beyne x o y ro ' yad gerefte'
in kar kare hosh masnoe nis?



pas hala fahmidim chetro ba riazio amar yek model mitone rabete beyne x o y
ro yad bgire.


hala in regressione sade hast.

regresione machine learning chie???

jalase bad sohbat mishe



Alipilehvar1999@gmail.com
ai.course22.alipilehvar@gmail.com


GOOD LUCK!!!!!!




'''








#25
#25
#30
#3
#0
83/5

#16.6
= train score = baraye dade hae ke roosh fitt krdim

#training score


#10
#test score





#-----------------------------------
#datahamon yekseri x dare yekseri y dare khob
#chanta radifan masalan 100 ta (100 ppont noghte)

#20 tashonpo vardar bokon test dataset --> yani asan enga rndrimesh ahzfeshon kone

#chanta mimone?



#80 ta --> b ina migan train dataset --> hala ba in 80 ta fk kopn kole nemonamone

#bia hey khataro rasm kon hey roo ina fit kon
#hey roo ina fit kon
#cost function baraye har khat dr biar

#$kamtarin cost function bbin a o bish chie

#y=ax+b --> rabetamonnnnnnnnnn

#hala bbin in noghati k dahstim yani 80 ta 
#x eshono bzaar too rabete bbin y chi mide

#y predicted chie? menahsh ckon az y e vaghe ei
#hame ye 80 ta maoedelsh mishe ---> train scoreee



#20 taro dashtim k nayovordim jolo
#20 ta x oi  y dshtim

# x ashpo bzar too in rabete he ke model darovorde
#bbin y chi mishe

#y e ino ba y e v aghei menha kon taghsim bar 20 
#test scoree



#train scorer--> fasele noghati k dadim model amzoesh dide ba noghate vaghe ei --> fitting o neshon mdie --> cheghad yad grfte

#test score--> yani onae k model nadside --> ma pishbnish krdim ---> test scorer --> prediction --> pishbini pazirti generalization , neshon mide




#========================
#mqachien elarning yani
#1-yad bgire az data 2-mantegh kasb kone 3-tasmim bgire


#1- yadgiri***********
#qaz data yad migire
#fdata chie ? yek dataframe ke koli x darwe o ydone y
#khob agar y ha peyvaste bashe migim supervised regression
#ag y ha gosaste bashe migim supervbised classfication

#supervised-----> 1-regression 2-classfvication



#2--- mantegh *******
#bad rabeyteye x and y ro yadmigire


#har x e jadidi behesh bdim baema y mide ****
#ye mon ya predict mikoen ya daste bandio mige
#tasmim migire





#-------ejraye dastooor chejorie ?

#- datamon ro dataframe drim
#midonim chanta radife yani chanta point ya noght edrim
#in noghat chanta x ya chanta y drn
#**y baya dbbinim ya classificatione e , regressione


#avalin kar--> daTAMONO taghsim mikonim
#yek darsadi (80) mizrim traININ DATASET 
#20 darsad ro mizrim test dataset



#model miad azin 80 ta train dataset , rabetey x o y ro dr miare
#bad mibine ina chijori fit shodsan ye score mide bname training_score --> fittingo nshon mide


#oon 20 darsadam hala x asho mzirim too in rabete y ro dr miarim va moghayes emikonim
#oon 20 a ro ndide --> test scorer = pishbinimon chghd ghaviee




#ba estefade az test score va train score mifhmim modelemon cheijorie




#KOILE CONCEPTE MACHINE LEARNING



#inke chijori rooye training dataset ( 80 ta)
#cxhijooori vagehan rabetey x o y ro dr maire
#noe model

#1- linear regression (LR)
#2-  KNN (K Nearest neigbourws)
#3- Decision tree (DT)
#4- randomk fporest (rf)
#5- svm (support vector machine)
#6- mlp (multy layer perceptrion)/ANN artificial neural network

#in model ha fght fargheshon ine ke
#yejoori rabeteye beyne x o y ro dr miaran ama raveshehson frgh dre baham

#ona ham mian yeseri kara mikone
#yechizaee bename cost function drn 
#vase hame hadsashon dr miaran
#bhtrrino peyda mikonan
#va migan inam rabetamon

#LR hey y=ax+b khat midad
#baghie ravehs haye dg




#========================================
#========================================
#========================================
#========================================
#========================================
#========================================
#===================L12==================
#========================================
#========================================
#========================================
#========================================
#========================================
#========================================







#25
#25
#30
#3
#0
83/5

#16.6
= train score = baraye dade hae ke roosh fitt krdim

#training score


#10
#test score





#-----------------------------------
#datahamon yekseri x dare yekseri y dare khob
#chanta radifan masalan 100 ta (100 ppont noghte)

#20 tashonpo vardar bokon test dataset --> yani asan enga rndrimesh ahzfeshon kone

#chanta mimone?



#80 ta --> b ina migan train dataset --> hala ba in 80 ta fk kopn kole nemonamone

#bia hey khataro rasm kon hey roo ina fit kon
#hey roo ina fit kon
#cost function baraye har khat dr biar

#$kamtarin cost function bbin a o bish chie

#y=ax+b --> rabetamonnnnnnnnnn

#hala bbin in noghati k dahstim yani 80 ta 
#x eshono bzaar too rabete bbin y chi mide

#y predicted chie? menahsh ckon az y e vaghe ei
#hame ye 80 ta maoedelsh mishe ---> train scoreee



#20 taro dashtim k nayovordim jolo
#20 ta x oi  y dshtim

# x ashpo bzar too in rabete he ke model darovorde
#bbin y chi mishe

#y e ino ba y e v aghei menha kon taghsim bar 20 
#test scoree



#train scorer--> fasele noghati k dadim model amzoesh dide ba noghate vaghe ei --> fitting o neshon mdie --> cheghad yad grfte

#test score--> yani onae k model nadside --> ma pishbnish krdim ---> test scorer --> prediction --> pishbini pazirti generalization , neshon mide




#========================
#mqachien elarning yani
#1-yad bgire az data 2-mantegh kasb kone 3-tasmim bgire


#1- yadgiri***********
#qaz data yad migire
#fdata chie ? yek dataframe ke koli x darwe o ydone y
#khob agar y ha peyvaste bashe migim supervised regression
#ag y ha gosaste bashe migim supervbised classfication

#supervised-----> 1-regression 2-classfvication



#2--- mantegh *******
#bad rabeyteye x and y ro yadmigire


#har x e jadidi behesh bdim baema y mide ****
#ye mon ya predict mikoen ya daste bandio mige
#tasmim migire





#-------ejraye dastooor chejorie ?

#- datamon ro dataframe drim
#midonim chanta radife yani chanta point ya noght edrim
#in noghat chanta x ya chanta y drn
#**y baya dbbinim ya classificatione e , regressione


#avalin kar--> daTAMONO taghsim mikonim
#yek darsadi (80) mizrim traININ DATASET 
#20 darsad ro mizrim test dataset



#model miad azin 80 ta train dataset , rabetey x o y ro dr miare
#bad mibine ina chijori fit shodsan ye score mide bname training_score --> fittingo nshon mide


#oon 20 darsadam hala x asho mzirim too in rabete y ro dr miarim va moghayes emikonim
#oon 20 a ro ndide --> test scorer = pishbinimon chghd ghaviee




#ba estefade az test score va train score mifhmim modelemon cheijorie




#KOILE CONCEPTE MACHINE LEARNING



#inke chijori rooye training dataset ( 80 ta)
#cxhijooori vagehan rabetey x o y ro dr maire
#noe model

#1- linear regression (LR)
#2-  KNN (K Nearest neigbourws)
#3- Decision tree (DT)
#4- randomk fporest (rf)
#5- svm (support vector machine)
#6- mlp (multy layer perceptrion)/ANN artificial neural network

#in model ha fght fargheshon ine ke
#yejoori rabeteye beyne x o y ro dr miaran ama raveshehson frgh dre baham

#ona ham mian yeseri kara mikone
#yechizaee bename cost function drn 
#vase hame hadsashon dr miaran
#bhtrrino peyda mikonan
#va migan inam rabetamon

#LR hey y=ax+b khat midad
#baghie ravehs haye dg




#----------avalin mesal gol haye iris--------------

#import sklearn
#in ketabkhon kheyli bozorgeeee hamasho nabaayd import krd sakhte


from sklearn.datasets import load_iris

iris=load_iris()

#INPUT, X , FEATURE --> VORODI
#OUTPUT, Y , TARGET --> KHOROJI


iris.feature_names
#Out[85]: 
#['sepal length (cm)',
# 'sepal width (cm)',
# 'petal length (cm)',
# 'petal width (cm)']

iris.target_names
#'setosa', 'versicolor', 'virginica'
#esme se ta gole


x=iris.data
y=iris.target

#too in mesalaye sklearn injorie 
#ama donyaye vaghe ei bayad yaek dataframe dri
#baayd jdoash koni  b x va y 

#in datamon
#*(**Tpozihat)


#hadaf chie?

#yek mdoel bsazim baid yad bgire 
#rabetey ebyen ex haro ba y 
#ke chi bshge

#ke vaghty ye goli ma grftim andaze giri krdim 4 ta vzihegisho
#gozaahtim too mdoel
#model behgemon bege jozvge kodom dastas (cxlassififcation)


#150 gol
#4 ta vizghegi dre k -->x
#1 done khoroji k noe gol ro nvshte --> y


#---avalin kar???
#preprocedssign---> yani dade haye parto hazf koni
#scaleshon doiros koni va a,.......


#vali dade haee k sklearn dre mhame preprocess hsodas


#vali ytdmon bashde bayad har datae ro preprocesing anjam bdim
#dovomi kar
#bayad datamono b test va train taghhism konim

#yani 80% train bnashan , 20% test
#vazeh tr bgm

#yani 80 % x bashe jolosh 80% y
#20 % x bashe 20% y



x=iris.data
y=iris.target
from sklearn.model_selection import train_test_split

#aval bgo too koja brizm vaghtyy joa krdm

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,shuffle=True,random_state=0)



#gharoghati kon tartib

#shuffle

#daddd ro taghsim konim b test dataset va train dataset
#ke mdoel bre yad bgire az train dataset va biad bge 
#psihbnini kone test dataset ro

#ta inja baraye hame ravesh ha yeksaen

#alan ye mdoel mkihaym roye training dataset  yad bgire
#in mdoel az ye raveshi mire k hala felan yedonasho bldim

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()



#--------------
#hala yek model drim
#mikhaym bgim model bioro rooye traina dataset ha
#oon 80% e yani oon 120 ta noghte yad bgir rabetey x o y ro


model.fit(x_train,y_train)

#@ychi drim bname model, hamin variable e model
#alkan rfte yad grfte

#tooo delehszh yeseri chizas

#ghabla z inke predict bznim mikhaym bbinim
#modele k sakhte yani rfte yad grfte

#test datasetaro onae k ndide ro chijori mitone predict kone

score=model.score(x_test,y_test)
print('our accuracy is :',score)
#our accuracy is : 1.0






#mikham ydchize jdid bdm k pishbini kone
#yek golo drm 4 ta vzihegisho grftm mikham bdm behesh

new_data=np.array([5.9,2.7,5.2,2.4]).reshape(1,-1)
preddcited_data= model.predict(new_data)

print(preddcited_data)


#5








#=============




from sklearn import datasets

#https://scikit-learn.org/stable/datasets.html#datasets

data1=datasets.load_iris()
data2=datasets.load_boston()
data3=datasets.load_breast_cancer()
data4=datasets.load_linnerud()
data5=datasets.load_wine()
data6=datasets.load_diabetes()
data7=datasets.fetch_california_housing()




#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================
#==================================================================================


#overview--------


'''

Pas kolan machine learning 3 no hast
1-Supervised learning
2-Unsupervised learning
3-reinforcement learning


khode supervised learning b do no taghsim mishe 1-Regression 2-classification
va unsupervised yani khooshe bandi (clustring)

khob bebinid kolan machine learning Model ha mesle ye BOX hast
dota faz dre


1-Train dadane BOX:
in Box data migire va in data ( Ye x dare ye Y dre)
In box be yek tarighi rabeteye beyne X va Y ro bedast miare (yani yad migire train)

2-predictioNE BOX (pishbini):
hala ye x e jadid behesh bdim tebghe rabete ee k balade y ro behemon mide (pishbini)



.......
hala in datamon ( ke x o y dare) ag y emon adade peyvaste bashe 1.43,3.543,6,..
be masalamon migan supervised regression
age datamon Y esh gosaste bashe yani case1,case2,case3 behesh migan
classification ( dastebandi)

dar har sorat data ro k beehsh midim miad rabeteye beyne x o y ro yad migire
age regression bashe: miad mige in x ha ch rabete e ba y daran k x e jadid 
migire betone y ro pishbini one
age classification abshe: miad mibine in x ha ba y ch rabete ee drn k x e jadid
migire betone bege Y esh kodome ( yani jozve kodom daste hast)

agar dar masaele daste bandi Y ro b model nadim va bgim khodet boro too x ha
begardo begard bbin frghashon chie va khdoet khoshe bandishon kon behesh mign
unsupervised



......
pass dobare mitonim begim kole machine learning shabihe derakhte zire


..............................Machine learning.......................................
.....1-supervised.............2-unsupervised...........3-reinforcment................
...1.1.Regression..............clustring................(IN dar mohit train mibine)..
...1.2.classification...................................(bar asase padasho azab).....
.....................................................................................

Pas ye Box (modele machine learning) darim ke do faz dare yeki 1-train bbine
2-badesh k hala yad grft btone pishbini kone

khob chijori train mibine? yani chijori mitone yad bgire rabete ro ?
hezaran rah hast 1-lienar regression (hamoni k tozih dadim) 2-K Nearest Neighbour
3-Decision Tree 4-Random Forest 5-Support vector
bebini hameye in model ha ham baraye regressionhast ham baraye classification
hameye in model ha ye thrick mizanan va rabeteye beyne x o y ro bedast miaran
faghat harkodom raveshi k estefade mikone fargh dare(behesh mipardazim...)

khob hala fk kon yad grft tamom , aaz koja bdonim doros pishbini krde?
khob bayad brim ye x i azmayesh konim bbinim y chie / bad x ro bzarim too in model
bbinim y ro chi pishbini mikone va badesh bebinim ke in Y ha chghdr shabihe hame

Bejaye inke aval train bdim model ro roo kole data ha bad ye noghte jadid 
brim begirim
miaym migim az aval bia dade haro taghsim kon be dobakhsh 1-train 2-test

model rooye dade haye aval train bbine (yani rabete ro peyda kone) bad
biad oon test haro x esho bzare too model ye y i migire ba y i k vaghena dre
moghayese kone va bbine model cheghadr nazdiek ( be in migan score ya metric ya error)

khob Hala ma fhmidim chishdoe.

hala mikhaym biaym too code nevisi bbinim ch konim.

Bebinid kolan dataye ma ye Dataframe hast yani chanta soton drim chanta radif
radif ha yani tedad nemone hamon ama yekseri sotonemon X emon (vorodimon) has
va yek soton Y (khoroji) hast



888888888888888888888888888888888888888888888888888888888888888888888888888888
888888888888888888888888888888888888888888888888888888888888888888888888888888

Kole hooshe masnoee chnta marhale dare:
    

Marhale (1)--> datamono biarim too barname spyder 


Marhale (2)--> preprocessing : yani bayad ba oon ravesh haye pandas
              kamel analysesh konim tamame jahaye khali , ghalat va ... ro hazf konim
             
              
Marhale (3)--> bayad in datamono soton haye x ro brizim dar Yek varibale e X
               va sotooone y ro brizim too yek variable bename Y
            
               
Marhale(4)---> hala datamono be do bakhsh taghsim konim yek darsadi ro bokonim
               training yekdastaro bokonim test

**gharare model biad az rooye x o y haye Training dataset , rabete ro yad begire
ba in rabete biad x haye Test dataset ro bgire va yek y BENAME Y_PREDICT pishbini 
kone va ba y haye test dataset moghayese kone va in moghayese behesh migan
error, metric , score --> ke neshangare khata va deghate modelemone



Marhale(5)--> Hala yek model entekhab konim ( felan yek modele linearregression
                                             va Logisticregresion baladim)
**ama ma model haee mesle KNN, DT, RF, SVR darim ke hamashon mian az rooye
training dataset rabeteye beyne x o y ro yad migiran va badesh ba oon x e jadid 
migiran va y ro pishbini mkonan
farghe in mdoel ha baham fght dar raveshe yadgiri ee hast k poshte tabashon emal
shode, dar natije hamashoon fght rabeteye beyne x o y ro dr miare


Marhale(6)---> hala in modelemono migim boro fght az training-dataset 
rabete beyne x o y ro dr biar va yad bgir ( kari b test dataset ndshte bash)
va mire o yad migire tamaaaaam!!

Marhale(7)---> hala midonim yek test dataset drim k yekseri x dre yekseri y dre
be y haye in migan true_y yani vageh eie. hala ma fght x e in test dataset ro
midim be modelemon ( modelemon az training dataset , rabete ro yad gerefte)
va hala migim y ro pishbini kon va y ro pishbini mikone va bema yek
y_predicted mide va ma miaym y_predicted va y_real ro baham moghayese mikonim



Marhale(8)-->  Dar marhaleye moghayese ma bayad bedonim he vaghty model
miad az training dataset rabeteye x o y ro dr miare, vaghty hamoon x haro bhsh mdiim
ye y e taghribi mide be ezaye har x, khataye in y haee ke mide ba vaghe e haro
behesh migan deghate fitting ya training_score yani chegahd toneste in rabete ro
dorost mdoelling kone
hala in, marboot be oon x o y haee bood ke dide bood
miaym behesh x_y e test_dataset behehs midim ke nadide va mikhyam bebinim
pishbinish chtore
miad x haro migire va yek y i pishbini mikone va moghayese mikonim va b in migan
train_score

pas kolan yek train_score drim ke namayangare yadgirie model ya fittingo modelingeshe
yek test_score ke neshangare tavanaeeie pishbinie model baraye datahayee ke nadide hast




Age train_score kh paeen bashe --> Underfitting -> yani doros natonese yad bgire
Age train_score kh bala bashe va test_score paeen bashe--> overfitting--> yani
kh dige yad grfte yani ba inke yekseri khata has dar dataha , oon nois ha ham yad grfte
va hamishe in ziad yadgrftn khob nis chon baes mishe natonim datahaye jadid ro
khoob pishbini konim ( behesh migan generalization yani ooomomi sazi)


9999999999999999999999999999999999999999999999999999999999999999999999999999999
9999999999999999999999999999999999999999999999999999999999999999999999999999999
Pas kolan 8 ta marhale darim che baraye regression ch classification
alan mikhaym code nevesisho bgim
**esmashono yad bgirid**



Marhale 1--> (IMPORTING)------------------------------------------------------
miaym az Open() ya pd._read estefade mikonim  ya az dataset haye sklearn k amade hast

Marhale2--> (Preprocessing)------------------------------------------------------
az rasvesh haye cleaning data dar pandas esteafde shavad mesle pd.drop va ...

Marhale3--> (taghsim b x o y)------------------------------------------------------
Kh sade ba ['esme soton'] inaro brizim too dota zarf yeki X yeki Y

Marhale4-->(train test split)------------------------------------------------------
Mitonim az tabeye train_test_split ke yeki az tabe haye ketabkhone sklearn
hast estefade konim k datahamono miad taghdim mikone be test o train
inke chan darsad vardare taghsim kone ham daste mast 


Marhale5--->(Model selection)------------------------------------------------------
Kh sade ba seda kardane oon modeli k mikhaym va rikhtnsh too yek zarf
mitonim azash estefade konim
mymodel=SVR()  ya  mymodel=DecisionTree()
#chra nmiaym mostaghim estefade konim? choon dakhele parantez mitonim yekseri
settinge model ro tanzim konim hamon aval setting ro tanzim mikonim va mirizmsh too
yek zarf, beja inke hey sedash bznim va hey biaym tanzim bechinim

Marhale6-->(training / fitting)------------------------------------------------------
Hala vaghteshe be modeli k entekhab krdim bgim boro az train dataset yad bgir
yani train bbin
kh sade esmesho seda miznim migim fit sho

mymodel.fit(x_train,y_train)

y x_train o y_train drim k hamonaee has k dar marhale 4 taghsimesh krdim
hala migim modelemon k dr marhale 5 entekhab krdim bre az x o y e
training , rabete beyne x  o y ro befahme

Marhale7--->(Prediction)------------------------------------------------------
Hala modelemon yad grfte va kh sade mitonim hamin model ro seda bznim va bgim
felan x ( x i k made nazaremone) behesh bdim va bgim bnzrt y chi mishe? (pishbini)

mymodel.predict(new_x)
in yani mymodel k modele mane k train dide yani yad grfte hala x bhsh midim 
va yek y ro predict mmikone


Marhale8--->(Scoring / Error / Metric )------------------------------------------------------

Hamontor k goftam do no score drim
yek score migan train_score yeki test_score

train_score yani midonim training dataset yek seri x_train dre ye y_train
model yek rabete ee beyne ina peyda krde (rabete he ke 100% doros nis)
yani yechizi beyneshone ( fek konid b oon khate ke beyne noghat rad shode bood)
khob bayad bbinim in model age in x haye train ro bhsh bdim ch y ro predict mikone
yani cheghad khoob toneste model beshe ya fiitt bshe

yedone hasm test_score drim yanii oon test dataset ke negah dashte boodim k pishbinie
model ro bahash besanjim
yek x_test dre ye y_test/ y_test emon dr asl behesh migan y_true yani in vaghe eiate
hala ma in x_test ro midim k modelemon predict kone va bema yek y_predicted
mide va hala ba moghayese krdne y_predicted ba y_true
yani y hayee k model pishbini krde ba y haee k bayad mishode yani entezar dshtim inshe
behesh migan test_score ke neshangare tavanaeeie pishbinie mdoelemone


kafie az code e zir estefade she

model.score(y_true,y_predicted)









Moafagh bashid,
Alipilehvar1999@gmail.com
Ai.Course22.Alipilehvar@gmail.com



'''



#overview--------


'''

Pas kolan machine learning 3 no hast
1-Supervised learning
2-Unsupervised learning
3-reinforcement learning


khode supervised learning b do no taghsim mishe 1-Regression 2-classification
va unsupervised yani khooshe bandi (clustring)

khob bebinid kolan machine learning Model ha mesle ye BOX hast
dota faz dre


1-Train dadane BOX:
in Box data migire va in data ( Ye x dare ye Y dre)
In box be yek tarighi rabeteye beyne X va Y ro bedast miare (yani yad migire train)

2-predictioNE BOX (pishbini):
hala ye x e jadid behesh bdim tebghe rabete ee k balade y ro behemon mide (pishbini)



.......
hala in datamon ( ke x o y dare) ag y emon adade peyvaste bashe 1.43,3.543,6,..
be masalamon migan supervised regression
age datamon Y esh gosaste bashe yani case1,case2,case3 behesh migan
classification ( dastebandi)

dar har sorat data ro k beehsh midim miad rabeteye beyne x o y ro yad migire
age regression bashe: miad mige in x ha ch rabete e ba y daran k x e jadid 
migire betone y ro pishbini one
age classification abshe: miad mibine in x ha ba y ch rabete ee drn k x e jadid
migire betone bege Y esh kodome ( yani jozve kodom daste hast)

agar dar masaele daste bandi Y ro b model nadim va bgim khodet boro too x ha
begardo begard bbin frghashon chie va khdoet khoshe bandishon kon behesh mign
unsupervised



......
pass dobare mitonim begim kole machine learning shabihe derakhte zire


..............................Machine learning.......................................
.....1-supervised.............2-unsupervised...........3-reinforcment................
...1.1.Regression..............clustring................(IN dar mohit train mibine)..
...1.2.classification...................................(bar asase padasho azab).....
.....................................................................................

Pas ye Box (modele machine learning) darim ke do faz dare yeki 1-train bbine
2-badesh k hala yad grft btone pishbini kone

khob chijori train mibine? yani chijori mitone yad bgire rabete ro ?
hezaran rah hast 1-lienar regression (hamoni k tozih dadim) 2-K Nearest Neighbour
3-Decision Tree 4-Random Forest 5-Support vector
bebini hameye in model ha ham baraye regressionhast ham baraye classification
hameye in model ha ye thrick mizanan va rabeteye beyne x o y ro bedast miaran
faghat harkodom raveshi k estefade mikone fargh dare(behesh mipardazim...)

khob hala fk kon yad grft tamom , aaz koja bdonim doros pishbini krde?
khob bayad brim ye x i azmayesh konim bbinim y chie / bad x ro bzarim too in model
bbinim y ro chi pishbini mikone va badesh bebinim ke in Y ha chghdr shabihe hame

Bejaye inke aval train bdim model ro roo kole data ha bad ye noghte jadid 
brim begirim
miaym migim az aval bia dade haro taghsim kon be dobakhsh 1-train 2-test

model rooye dade haye aval train bbine (yani rabete ro peyda kone) bad
biad oon test haro x esho bzare too model ye y i migire ba y i k vaghena dre
moghayese kone va bbine model cheghadr nazdiek ( be in migan score ya metric ya error)

khob Hala ma fhmidim chishdoe.

hala mikhaym biaym too code nevisi bbinim ch konim.

Bebinid kolan dataye ma ye Dataframe hast yani chanta soton drim chanta radif
radif ha yani tedad nemone hamon ama yekseri sotonemon X emon (vorodimon) has
va yek soton Y (khoroji) hast



888888888888888888888888888888888888888888888888888888888888888888888888888888
888888888888888888888888888888888888888888888888888888888888888888888888888888

Kole hooshe masnoee chnta marhale dare:
    

Marhale (1)--> datamono biarim too barname spyder 


Marhale (2)--> preprocessing : yani bayad ba oon ravesh haye pandas
              kamel analysesh konim tamame jahaye khali , ghalat va ... ro hazf konim
             
              
Marhale (3)--> bayad in datamono soton haye x ro brizim dar Yek varibale e X
               va sotooone y ro brizim too yek variable bename Y
               
               
#*** azinja bbad ro sklearn yek folder dare bename dataets mitoni data load koni

               
Marhale(4)---> hala datamono be do bakhsh taghsim konim yek darsadi ro bokonim
               training yekdastaro bokonim test

**gharare model biad az rooye x o y haye Training dataset , rabete ro yad begire
ba in rabete biad x haye Test dataset ro bgire va yek y BENAME Y_PREDICT pishbini 
kone va ba y haye test dataset moghayese kone va in moghayese behesh migan
error, metric , score --> ke neshangare khata va deghate modelemone



Marhale(5)--> Hala yek model entekhab konim ( felan yek modele linearregression
                                             va Logisticregresion baladim)
**ama ma model haee mesle KNN, DT, RF, SVR darim ke hamashon mian az rooye
training dataset rabeteye beyne x o y ro yad migiran va badesh ba oon x e jadid 
migiran va y ro pishbini mkonan
farghe in mdoel ha baham fght dar raveshe yadgiri ee hast k poshte tabashon emal
shode, dar natije hamashoon fght rabeteye beyne x o y ro dr miare


Marhale(6)---> hala in modelemono migim boro fght az training-dataset 
rabete beyne x o y ro dr biar va yad bgir ( kari b test dataset ndshte bash)
va mire o yad migire tamaaaaam!!


Marhale(7)---> hala midonim yek test dataset drim k yekseri x dre yekseri y dre
be y haye in migan true_y yani vageh eie. hala ma fght x e in test dataset ro
midim be modelemon ( modelemon az training dataset , rabete ro yad gerefte)
va hala migim y ro pishbini kon va y ro pishbini mikone va bema yek
y_predicted mide va ma miaym y_predicted va y_real ro baham moghayese mikonim



Marhale(8)-->  Dar marhaleye moghayese ma bayad bedonim he vaghty model
miad az training dataset rabeteye x o y ro dr miare, vaghty hamoon x haro bhsh mdiim
ye y e taghribi mide be ezaye har x, khataye in y haee ke mide ba vaghe e haro
behesh migan deghate fitting ya training_score yani chegahd toneste in rabete ro
dorost mdoelling kone
hala in, marboot be oon x o y haee bood ke dide bood
miaym behesh x_y e test_dataset behehs midim ke nadide va mikhyam bebinim
pishbinish chtore
miad x haro migire va yek y i pishbini mikone va moghayese mikonim va b in migan
train_score

pas kolan yek train_score drim ke namayangare yadgirie model ya fittingo modelingeshe
yek test_score ke neshangare tavanaeeie pishbinie model baraye datahayee ke nadide hast




Age train_score kh paeen bashe --> Underfitting -> yani doros natonese yad bgire
Age train_score kh bala bashe va test_score paeen bashe--> overfitting--> yani
kh dige yad grfte yani ba inke yekseri khata has dar dataha , oon nois ha ham yad grfte
va hamishe in ziad yadgrftn khob nis chon baes mishe natonim datahaye jadid ro
khoob pishbini konim ( behesh migan generalization yani ooomomi sazi)


9999999999999999999999999999999999999999999999999999999999999999999999999999999
9999999999999999999999999999999999999999999999999999999999999999999999999999999
Pas kolan 8 ta marhale darim che baraye regression ch classification
alan mikhaym code nevesisho bgim
**esmashono yad bgirid**



Marhale 1--> (IMPORTING)------------------------------------------------------
miaym az Open() ya pd._read estefade mikonim  ya az dataset haye sklearn k amade hast

Marhale2--> (Preprocessing)------------------------------------------------------
az rasvesh haye cleaning data dar pandas esteafde shavad mesle pd.drop va ...

Marhale3--> (taghsim b x o y)------------------------------------------------------
Kh sade ba ['esme soton'] inaro brizim too dota zarf yeki X yeki Y

Marhale4-->(train test split)------------------------------------------------------
Mitonim az tabeye train_test_split ke yeki az tabe haye ketabkhone sklearn
hast estefade konim k datahamono miad taghdim mikone be test o train
inke chan darsad vardare taghsim kone ham daste mast 


Marhale5--->(Model selection)------------------------------------------------------
Kh sade ba seda kardane oon modeli k mikhaym va rikhtnsh too yek zarf
mitonim azash estefade konim
mymodel=SVR()  ya  mymodel=DecisionTree()
#chra nmiaym mostaghim estefade konim? choon dakhele parantez mitonim yekseri
settinge model ro tanzim konim hamon aval setting ro tanzim mikonim va mirizmsh too
yek zarf, beja inke hey sedash bznim va hey biaym tanzim bechinim

Marhale6-->(training / fitting)------------------------------------------------------
Hala vaghteshe be modeli k entekhab krdim bgim boro az train dataset yad bgir
yani train bbin
kh sade esmesho seda miznim migim fit sho

mymodel.fit(x_train,y_train)

y x_train o y_train drim k hamonaee has k dar marhale 4 taghsimesh krdim
hala migim modelemon k dr marhale 5 entekhab krdim bre az x o y e
training , rabete beyne x  o y ro befahme

Marhale7--->(Prediction)------------------------------------------------------
Hala modelemon yad grfte va kh sade mitonim hamin model ro seda bznim va bgim
felan x ( x i k made nazaremone) behesh bdim va bgim bnzrt y chi mishe? (pishbini)

mymodel.predict(new_x)
in yani mymodel k modele mane k train dide yani yad grfte hala x bhsh midim 
va yek y ro predict mmikone


Marhale8--->(Scoring / Error / Metric )------------------------------------------------------

Hamontor k goftam do no score drim
yek score migan train_score yeki test_score

train_score yani midonim training dataset yek seri x_train dre ye y_train
model yek rabete ee beyne ina peyda krde (rabete he ke 100% doros nis)
yani yechizi beyneshone ( fek konid b oon khate ke beyne noghat rad shode bood)
khob bayad bbinim in model age in x haye train ro bhsh bdim ch y ro predict mikone
yani cheghad khoob toneste model beshe ya fiitt bshe

yedone hasm test_score drim yanii oon test dataset ke negah dashte boodim k pishbinie
model ro bahash besanjim
yek x_test dre ye y_test/ y_test emon dr asl behesh migan y_true yani in vaghe eiate
hala ma in x_test ro midim k modelemon predict kone va bema yek y_predicted
mide va hala ba moghayese krdne y_predicted ba y_true
yani y hayee k model pishbini krde ba y haee k bayad mishode yani entezar dshtim inshe
behesh migan test_score ke neshangare tavanaeeie pishbinie mdoelemone


kafie az code e zir estefade she

model.score(y_true,y_predicted)









Moafagh bashid,
Alipilehvar1999@gmail.com
Ai.Course22.Alipilehvar@gmail.com



'''


#raveshe LR --> Linear regression

#1- chantaa a o b hads mzid
#hey khat haye y=a*x+b ro mikshid
#miomd fadsele noghte haro (datamjono) ba in khat hesab mikrd --> cost function
#az beyen khat ha harkodom cost functione e kami dasht varesh midasht (optimization)
#migof in khate nahaeie mane Y=alpha*x + beta
#yani x bde behem man bht ba in formol y midam
#Khob ino omdn too ye shekrkati bename scikit learen --> sklearn

#in esme tabamone
#ye x o y vorodi migire (datae)--> aziin mikhad yad bgire
def linearregression(x,y):
    
    #200 ta khat misaze
    for i in range(0,200):
        a=np.random() #rndom as misaze
        b=np.random() #rndom b misaze
        #yy=a*xx+b #khatesh baraye harkodom az oon 200 khjat ha
        
    #miad mohasdebe mikone 
    #x haro mizre too in khate yy va miad moghayese mikone ba y 
    #yani noghat ro faseelashono ta oon khatre hesab mikone
    
    #yekseri cost function drim ehtemalan mirize tooye yek list
    #cost_function_list.append(cost_frunction)
    
    #min_cost=min(cost_function_list)
    
    #miad a o b isho vr midre
    
    return #(mige man in a o b ie nahaeime )


#sk learn miad in tabe ro mzire tooye ketabkhonash mige sedam bzn

from sklearn.linear_model import LinearRegression


#kare yek motekhasese hoshe masnoeeie dar algorithme sklearn

#==================================
#first note.......
#tamame dade ha bayad 3 marhaleye aval ejra bshe ama maa
#az sklearn esteafde mikonim
#sklearn yek dataseti dareke miad yek dataye khobo tartamiz
#bemaaaa tahvil mide (ytani bad az marhaleye sevom)




#........... 5 ta model (LR,KNN,DT,RF,SVM).......
#in model ha vase chian ? beehsh migan supervised
#yani ag yemon gosaste bashe --> classificatione masale
#be in model ha migan model classfire --> KNNclassfier

#ag peyvaste bashe ---> migan be masale regression
#b model ha migan KNNregressor


#==========================================================================
#==========================================================================
#==========================================================================
#==========================================================================
#==========================================================================
#==========================================================================

#-----------mesalemono az golhaye IRIS shoroo kon --> sklearn yek data dre be in nam

#mesal chie?
#yek fardi rfte 150 ta gol ro kande ovorde khoone
#pas 150 ta gol drim doone gol 
#in gol ha yekseri golbarg daran yekseri saghe drn 
#hala ham golbarg ham, saghe yekseri tool dre yekseri arz
#pas baraye har gol mitonim 4 tra feature ya vizhegi dr nzr bgirim

#toole golbarg, arze golbarg / toole saghe , arze saghe
#x1,x2,x3,x4

#150 ta radif dre 4 ta soton
#150 ta gol dshtim harkodom 4 vizhegisho nvshtim

#ye y ro ham misazim--->
#kole ina az 3 no tashkil shode avokia, rotsdheld , kalifari
#agha esm sakhte nmifhmam --> A B C --> 1 2 3 frghi mikone mage


#aghaye giahshenas lotdf kon joloye har gol bzn bgo kodom 1 e ya 2 e ya 3


#minvise o mdie behem

#datae k drm chie ?

#150 ta gole 4 ta vizehegi baraye hargol(golbargo sagahsh) va jolosham ye soton k che golie 

#150 ta radif dre , 5 ta soiton k 4 tash x an 1 ish y e


#age ye machin bshe behehs ino bdim yad bgire , badan mitonim y gol nbgirim behsh
#moshakahste in 4 taro ( arz o tole golbargo saghasho bgirim) bdim b in mashin
#mashin bma bge agha in ghole 1 2 3 


#classification......
#data ro az koja biari
#1-ag khodm sakhte bodm yani man moshtaghe gol --> excelesh bas moikrdm
#importesdh mikrdm ba read_csv bad preprocesing bad taghsim b x o y yeksrish too
#vizhegi ha yekseri ....
#2-sklearn omde hamin 3 marghalkaro anjam dade va gofte bia az in data estefade kon



#sklearn yek folder dare bename datsets k koli nemone dare****

from sklearn.datasets import load_iris
#yani boro az ketabkhoneye sklearn , madule (script) e datasets
#tabeye load_iris ro bde

#in yek tabas yani laod miokone pas yek khoroji dre bema data khgoroji 

#ye zarf msiazam bname iris
iris=load_iris()

#chiash mkoheme? #1- data featurenames 2-target target names

iris.feature_names
#['sepal length (cm)',
# 'sepal width (cm)',
# 'petal length (cm)',
# 'petal width (cm)']

iris.target_names
#array(['setosa', 'versicolor', 'virginica'], dtype='<U10')



x=iris.data
y=iris.target


#ch dataset import koni az sklearn ch khodet bayad
#dar nahayat yek x o y dashte bashi (marhale 3)

#pas in datamone ke mikhyam kar konim ( 3 marhale ro rftim)
#hooshe masnooe kolesh --> datmaono preprocess krdim
#omdim tabdilesh krdim b yek zarf x va yek zarf y

#split_train_test --> aval yekseriaro brizim yja test yeseriaro train
#rooyeseria bnamet train yad bgrie badan bbinim testaro doros pishbini mikone ya na

#chijori split konim? khode sklearn man ye3k tabe drm tabamo az dele ketabkhonam bekesh biropn

from sklearn.model_selection import train_test_split

#a=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)

#model selection
#hala vaghteshe brim rooye train dataset --> oonaee kmikhaym roosh train bbinemodel
#model ro fit konim , soal? ch modeli??--> 5 ta model drim
#1-lr , 2-knn , 3-dt, 4-rf, 5-svm
#alan #1-lr
#chijori b mdoel dast resi peyda konim
#model chiakr mikrd? y thricki mizad az x o y yad migrft
#uye tabe hast k x o y ro migire train mibine (class)

from sklearn.linear_model import LogisticRegression

#aval y zrf bsaz bname model
#chra mirizim too zrf va mostaghim estefade nmikonim?
#1- chon ziad estefade mikonimm esmesh toolanie 
#2- yekseri setting dre shayad bkhaym avazesh konim nmitonim hey seda bzni
#hey tosh setting bchini

model=LogisticRegression()

#ychizi drim bname model hamon box 

#1-fit mikonim rooye training dataset 
model.fit(x_train,y_train) #training
#vaghty in omd:Out[58]: LogisticRegression() yani tamom shod yad grf
#yani moadele ro drovord

#mitoni harchi mikhay predict koni tamom

#
import numpy as np
new_gol=np.array([6.2,2.4,4.1,1]).reshape(1,-1)

y_gol=model.predict(new_gol)
print(y_gol) #[1] omdf gof goel 1 e in chizi k kandii....

#sadegii

#soal mikone--> agha az koja man bdonm ras migire ???

#bahse evaluatriopn miad vasat...... score , metric , sanjeshe model
#yadete x_test y_test dashtim , estefade ee azash nkrdim ke ????

test_score=model.score(x_test,y_test)
print(test_score) #1.0
#hamaro doros gof

#scdore agha in chijroi hesab krde
#faseleye noghate pishbini shdoe ro ba noghate avgeh ei ro chijori hesab krde ?



#========================
#accuracy == chan dasrad doroste ? 1 --> 30 taee kd adim bhshsh , 30 taro doros pishbini krd

y_predicted=model.predict(x_test)
#yani x haye oon dadeye test ro ddim b model goftim [sshbini kon
#bema y e pishbini shode ro dad

#bachi moghayesash koni?

#ba y_real y_true y_test

#pas baayd dar asl y+predicted - y_test

#in menha mitone hezaran no bashe 

from sklearn.metrics import accuracy_score

test_score=accuracy_score(y_test,y_predicted)
print(test_score) #1.0

#dar asl bjaye inke inhame kar konm sklearn khodesh anjam mide



#lkare paeni hamon kare baaleie
test_score=model.score(x_test,y_test)
print(test_score) #1.0

#chra khob balaeeie ro yad di

#chon tabeye score fght yejor mire fadsele ro dr miare
#sahayd ma bkhaym az sanjesh haye dg estefade konim



#bbin fk komn az 30 ta 10 tash ghalaty bashe
#vaghty accuracy --> 20 ta doros bode --> 20/30= 0.66 doroste

#dade haye saratani ro ydt bashe
#dota javab ya saratn dre 1 ya ndre 0
#30 --> 10 ta ghalat pishbini krde --> aya inke ch ghalatie moheme? are moheme

#do no ghalat momkene biofte-->
#1- sarartand dare trf ama mige saratan ndre
#2- saratan ndre ama mige saratan dare




y_predicted=model.predict(x_test)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_predicted)



#----------------
y_predicted=model.predict(x_test)
from sklearn.metrics import f1_score
f1_score(y_test,y_predicted,average='micro')


#dr ghesmate evaluationa kamel bhsh miopardazim




#yadete goftm **************
#2 ta score dirm?
#yeki vase training yeki vase test


#ykish train_score yani onae k dide ro chghd fassele dre
#yani nshon midad chghd yad grfteeeee



#yki ham dashtim test _score yanbi onae k nadide --> pishbinio nshon midad



#bayad train_score , test_score bad tahlil koni
#ag train_score paeen basshe --> underfitting--> yad ngrft ekhgob
#ag train_scorre kh bala bashe --> test_score biad paeen-->overrfitiing -->biased --> taasobi rfte genralization 

#bhtrin--> ham train score ham test score bala bashe

#--------------------kole kar ine----------
#1-Logistic regresion-------------------
#----load data
from sklearn.datasets import load_iris
iris=load_iris()
#----taghsim b x o y 
x=iris.data
y=iris.target
#----taghsim b train o test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,shuffle=True,random_state=0)

#entekahbe model
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

#train va fit midimesh rooye trainingemon
model.fit(x_train,y_train)


#evaluation
train_score=model.score(x_train,y_train)
test_score=model.score(x_test,y_test)

print('our train score is :',train_score)
print('our test score is :',test_score)

#our train score is : 0.9666666666666667
#our test score is : 1.0

#tmam --> tahlil --> mige man 150 ta gol bod 120 ta training
#30 taro gozshtim nabine

#Mige az in 120 ta k dadi bhm man modelam mitone holohoshe 96% eshono doros bege
#azoon 30 tae k ndidam --> 30 tasho doros goftm
#pas x_train balast ham x_test --> mdoelemon awlie
#inja accuracy ro bhmon gfote harfi az
#deghato sehatpo ina nazade ag bkhaym bayad x_test haro
#pishbini konim va bzarim too oon formol


#yek new x bssazam
#---pishbini
x_new=np.array([6,2,3,1]).reshape(-1,1)
y_new=model.predict(x_new)

#+ rasm jolo mire


#hrchi goftim modele LR bood
#modele KNN, DT , RF , SVM frgheshon fght onjas k 
#bjaye moidel on mdoelo mizrim
#hjmchi yeksane
#==============================================
#------------KNN----------------------
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
y=iris.target
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,shuffle=True,random_state=0)
#**fght inja frgh dre ke model ro esme on modelemon mzirim

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=5)

model.fit(x_train,y_train)
train_score=model.score(x_train,y_train)
test_score=model.score(x_test,y_test)
print('our train score is :',train_score)
print('our test score is :',test_score)
#ag k=1
#our train score is : 1.0
#our test score is : 1.0

#ag k=10
#our train score is : 0.9666666666666667
#our test score is : 1.0

#k=20
#our train score is : 0.95
#our test score is : 1.0

#k ag kheyli kam bashe --> modelemon kh sade ishe shayad ppishbinish khob dr nayad
#ag k kh ziad bashe --> kh biased mishe --> kh piochide model --> test 
#yechizi beyne hamon 4,5


#x_new=np.array([6,2,3,1]).reshape(-1,1)
#y_new=model.predict(x_new)


#1-----ravesho goftm 
#moshekle model --> complexity bala banabarin 
#test score momkene biad paeen 
#bishtar baraye classsification khobe
#kh cost computational --> tool mikshe 


#yekseri setting dare
#mohemtrinesh n_neighboure --> 
#**** n_neighbour yani chanta hamsaye


# az halghe for estefade kon **gridsearch 


#==============================================
#------------DT----------------------
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
y=iris.target
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,shuffle=True,random_state=0)
#**fght inja frgh dre ke model ro esme on modelemon mzirim

from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(max_depth=3)

model.fit(x_train,y_train)
train_score=model.score(x_train,y_train)
test_score=model.score(x_test,y_test)
print('our train score is :',train_score)
print('our test score is :',test_score)
x_new=np.array([6,2,3,1]).reshape(-1,1)
y_new=model.predict(x_new)

#max depth ro taghir midid vba mibinid kodom bhtre


#complexity

#hartchi omgh bre bala --> hey dare sakht gir trmishe hey dre complex 
#nesbat b dataye ma shayad in khob bashe
#shaya din baES bshe bias bshe yani moteaseb bshe natone predict kone

#mohmtrina........
#max_depth
#min_samples_split
#max_features

#vizhegie in method....
#kh kh khobe baraye classfication ama baraye refgression
#beshedat complex mishe yani bshdt biased 
#tewst_scoee .... 0---> train khob mibine
#kh khgob masalan nazdik b 1 

#test --> 0.3

#yni rfte noise haram yad grfte 

#averag egiri --> 30 ta derkahte--> noise e hazf mishe
#generalization ---> tamim
#



#==============================================
#------------RF----------------------
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
y=iris.target
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,shuffle=True,random_state=0)
#**fght inja frgh dre ke model ro esme on modelemon mzirim

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=20)

model.fit(x_train,y_train)
train_score=model.score(x_train,y_train)
test_score=model.score(x_test,y_test)
print('our train score is :',train_score)
print('our test score is :',test_score)
x_new=np.array([6,2,3,1]).reshape(-1,1)
y_new=model.predict(x_new)

#computational cost



#==============================================
#------------SVM----------------------
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
y=iris.target
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,shuffle=True,random_state=0)
#**fght inja frgh dre ke model ro esme on modelemon mzirim

from sklearn.svm import SVC
model=SVC()

model.fit(x_train,y_train)
train_score=model.score(x_train,y_train)
test_score=model.score(x_test,y_test)
print('our train score is :',train_score)
print('our test score is :',test_score)
x_new=np.array([6,2,3,1]).reshape(-1,1)
y_new=model.predict(x_new)


#kernel

#kernel = linear ---> yani ehtemalan khatie rbaeye x  o y
#kernel = poly ----> gheyre khatie --> degree -->
#kernel rbf

#C ---> control mikone yad girisho yanio harchi bsihtr bSHE BISHTRR YD MIGIRE

#bazi jaha naiz ndrim kh kh yad bgire baya dholo hosh miangin yad bgire

#ma hamashono hey test mikonim




#---kole ravesh yeksane
#1-impoorte dtaa
#2-taghsim b x o y
#3- split b train o test
#4-entekhabe model ( 5 model)
#5- fit krdn rooye train ha
#6- score test o train ro migirim va moghayese mikonim 


#in  5 model rabete x o y ro ba ye thrick yd migiran 
#ma vase classficiation ( yani vcaght y goisaste hast )
#jalase badi regression ro yad midim




#-------baraye alaghe mandan----------------- 


#az sklearn az madule e datasets
#tabeye load_breast_canser ro miarim biron
from sklearn.datasets import load_breast_cancer
#mirizimesh too ye zarf bname cancer

cancer=load_breast_cancer()
#in data omade az 569 ta bimar data grfte
#har bimar 30 ta parametr az azameysheshon ro nvshte

#bad joloye har bimar neveshte 0 ya 1
#ag 0 bashe yani malignant yani badkhim
#ag 1 bashe yani bengin yani khosh khim

#in esme 30 ta vizhegi ro miare
cancer.feature_names

#in nshon mide 0 yani chi 1 yani chi too y ha
cancer.target_names


#khob haala bayad inkararo koni
#b x o y brizidishon
#bad train o test jodashon konid
#bad model entekhab konid
#bad fit konid
#bad test_score va train_score ro hesab konid
#hala vaghty model entekhab krdid 
#hey setting ro taghir bdid

#soali bood email bznid
#Moafagh bashid
#Alipilehvar1999@gmail.com
#ai.course22.alipilehvar@gmail.com



#hamchenin datahaye dg k mitonid estefade konid
#baraye classification

#dar mroede daste bandie nooshidani ha hast
from sklearn.datasets import load_wine

#darmorede dastkhat hast k kheyli sakhte....
from sklearn.datasets import load_digits



#==================================================
#==================================================
#==================================================
#===================L14===========================
#==================================================
#==================================================
#==================================================
#EDAMASH












#==================================================
#==================================================
#==================================================
#===================L14===========================
#==================================================
#==================================================
#==================================================

#POROZHE 3D PRINTING


















