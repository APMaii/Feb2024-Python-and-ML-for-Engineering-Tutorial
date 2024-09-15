
"""
In The Name Of God


Created on Wed Apr  3 15:13:38 2024

@author: ai.2024.pilehvar@gmail.com


L11

"""

#REVIEW------
#Python-----? harchizi benevisid ---> sefid --> reserve nashode--->Variable 
#rangi --> 1)Narenji ( Python built in (print,input, len,type,open))
#2)banafash --> if , if else, for while ,....

#sefid---> esme yek zarfe (avriable)----> 1.number (int,float,complex)
#2.bool(True,False) 3.str
#assign(megdhardehi) , access (index) -->1.change 2.iteration (for , if), function (str.lower())

#age bekhaym chna no value zakhire dare yek zarrf --> LIST

a=[1,2,3,4,5]

#access --> ** index az 0 shoro mishe
a[1]

#change
a[1]=20

#iteratiio

for i in range(0,len(a)):
    if a[i]<5:
        a[i]=0

#yekseri tabe ham dashtim
a.append(40)



#review ham bar numpy ham bar matplotlib
import random
#baraye sakhte random

#random int between ranges
a=random.randint(0,10)
print(a)


#random Float between 0 , 1 
a=random.random()
print(a) #0.21451371920668105
print(a) #0.6945273228515103




#Float  between range() 0 ta 10  10 ta 20
#0 ta 10
# chghd shas dare 4 entekhab she ya 5 ya 6 .....
#faravani
#distribution (tozi)

#2 --> distribution --> 1.uniform 2.normal (gaussian)

#======pak kon too zhenet
#soale-->agah y adad beyne 0 ta 10 entekhab kon bde behm
#int 
a=random.randint(0,10)
print(a)

#float
a=random.uniform(0,10)
print(a) #4.231171763773856
#dar nahayat y adade ashari beyne 0 ta 10 beht mdie
#maa inke chijori az beyne 0 ta 10 entekhab krde
#unifrom bode sitribution--> hamonghd k 1 shans dashte
#5 ham shansd dashte


a=random.gauss
#mu-->mean (oona dad vasate k bishtarin ehtemalo dare)
#sigma-->dispersion(parakandegi) az vasat ta 0 --> 3 ta sigma
a=random.gauss(5,2)
print(a) #5.397340894367682


a=random.choice([1,2,3,4])
a=random.shuffle([1,2,3,4])
#seeed--->dane


#vaghty bahse 1 adad boood yedone adad mikhasti
#numpy--> too delesh yechi b esme random dasre

#int beyne 0 ta 100
import numpy as np
a=np.random.randint(0,100)
#hamon kare randint krd
a=np.random.randint(0,100,size=(5))
a=np.random.randint(0,100,size=(2,3)) #2 ta radif , 3 ta sotoon

#adade int bood
#float between 0 1
a=np.random.rand()
a=np.random.rand(100)


#normal
#shabihe gauss
#loc--Mu  Scale-->sigma  size
a=np.random.normal(loc=5,scale=2,size=(100,))
import matplotlib.pyplot as plt
plt.hist(a)


a=np.random.normal(loc=5,scale=0.01,size=(100,))
plt.hist(a)


#unifrom

a=np.random.uniform(0,100,size=(100,))
plt.hist(a)

a=np.random.uniform(0,100,size=(1000,))
plt.hist(a)


#arraye besazid
#khdoeton manual (dasti)
#arange
#zero 

#random-->INt, float ( unifrom , normal)




#------LIST
#2 moshkel dare list--> mikhaym sari tar bashe, do bodi (radif , soton)
#numpy
#list
a1=[1,2,3,4]
import numpy as np
a2=np.array([1,2,3,4])
#do bodi #radifo sotoon
a22=np.array([ [1,2,3] , [4,5,6]])
a22[1,1]

#----Pandas --> man yechi mese array daram
#shoma mitoni baraye sotoon hat esm bzari
#**tamame dade ha -->Marsoom
#sotoona --> esmi daran --> temperature, time, modulus
import pandas as pd
#hamon array0-->sotonaro nam gozariu koni
#do no daram --> 1D (Series) 2D(DataFrame)
a3=pd.Series([1,2,3,4])

a3=pd.Series([1,2,3,4],index=['a','b','c','d'])


a33=pd.DataFrame([[1,2,3],[4,5,6]])


a33=pd.DataFrame([[1,2,3],[4,5,6]],index=['a','b'])
#aksaran index haro taghir nmidsan bishtar column haro taghir mdian
a33=pd.DataFrame([[1,2,3],[4,5,6]],columns=['Temp','time','Modulus'])


#aksare data ha insheklian
#Dataframe --.2D --> radifo sotoon daran
#radifo-->Tedad nemone ha ya tedade dat ahastan
#sotoon-->Vzihegi hastan --> esm daran
#halate standarde yek data
data=pd.DataFrame([[1,2,3],[4,5,6]],columns=['Temp','time','Modulus'])




#........
#1-assign
data=pd.DataFrame([[1,2,3],[4,5,6]],columns=['Temp','time','Modulus'])

#casting-->numpy--> pandas
a=np.array([[1,2,3],[4,5,6]])
data=pd.DataFrame(a,columns=['Temp','time','Modulus'])

#numpy bsazi 50 ta radif bashe 2 ta sotoon (50,2)--> 0 ta 100
a=np.random.uniform(0,10,size=(50,3))

data=pd.DataFrame(a,columns=['Temp','time','Modulus'])


#2-access
#3 noo --> row , column , element
#row-------------
data.iloc[2] #radife 2
data.loc[2]

#chanta bkhay
data.iloc[0:3]


#column-------------
data['Temp']
#2 ta bkhay
data[['Temp','Modulus']]

#***acces vaghty mikonim --> mitoni masalan columne temp ro begiri berizi too y zarfe dg
data.iloc[ : ,0  ] #tamame radif ha , felan soton


#elemeent------------------
data.loc[2,'Temp'] #radife 2 , sotoone temp
#mese gahdim bkhay adad bzari --> index--->i
data.iloc[2,0]


#----Operator----
df1=pd.DataFrame([1,2])
df2=pd.DataFrame([3,4])

c=df1+df2



#---Tabe -->function
data.max() #kodom radif bsihtarino dre

data.max(axis=0) #boro too radif ha

data.max(axis=1)





#aksarasn barat moheme k bdoni kodom sotoon kodom adad toosh bishtre
data['Temp'].max() #Out[111]: 9.786222347505731

#bayad brizi dakheley yek zarfe jadid
b=data.sort_values(by='Temp')
#harkair anjam midi momkene index ha beham brize


#joining
df1=pd.DataFrame([1,2])
df2=pd.DataFrame([3,4])
zarf=pd.concat([df1,df2])


#******--------------------------
#remove--------------
a=np.random.uniform(0,10,size=(50,3))

data=pd.DataFrame(a,columns=['Temp','time','Modulus'])

#** -->kole tabe ha too pandas --> returni emal nmikone
#time maskhare bazie
data.drop(columns='time')

#bayad brizi too zarf
zaarf=data.drop(columns='time')
#data dast nakhrodaas

data.drop(columns='time',inplace=True)
#hamashon yehci bname inplace dare--> ag true bzari
#miad rooyer khdoe data anjam mide va naizi b zarf nuis



zaarf=data.drop(index=3)

data.drop(index=3,inplace=True)


#tahe hame taghirastetoon*****

data.reset_index(drop=True,inplace=True)



data.reset_index(inplace=True) #index gahblairo miare


#================ANALYSIS DATA=======================
#YEK STPE GHABL AZ MACHINE LEARNING HAST-------------
#Data --> az site, azmayeshgah , maghale , 
#open --> open --> Pandas (open)

#zarf
#csv , excel
#radif , sotoon
#radif-->tedad nemoone
#sotoon-> vizhegi ha

import pandas as pd
mydf=pd.read_csv('/Users/apm/Desktop/data.csv')

#data ye mano (excel, csv)---> data fram

type(mydf) #Out[138]: pandas.core.frame.DataFrame


mydf.head() #5 ta
mydf.head(10)

mydf.tail() #5 ta
mydf.tail(10)

#mohem trin kar
mydf.info()

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 169 entries, 0 to 168
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   Duration  169 non-null    int64  
 1   Pulse     169 non-null    int64  
 2   Maxpulse  169 non-null    int64  
 3   Calories  164 non-null    float64
dtypes: float64(1), int64(3)
memory usage: 5.4 KB




#data fram hast
169 ta radif dare k az 0 ta 168 shomare gozari shode

4 ta soton ( column)

null--> value wrong

#colories 164 non-null . 5 ta null hast 


Ma hamishe data hamon ro k mairim gharar nis hamashon doros bashan

-----CLEANING------

*(8drop--> vaghty mikhayt dasti chziio hazf koni)


'''
#Naghs dar data momkene bashe
#1-empty cell (khali bashe)
#2-wrong format
#3-wrong data
#4-duplicated


#road----> 1.find 2.action

#---------1-empty cell-------------
#NAN -->Not a number---> dar transfer 
#khdoe dastgahi record -->kharab
#NAN --.empty

#moshkel ijad mikone

mydf.info()
#null --> felan sotoon inghad null


#action --> 1. hjazf konid ( kole radif hazf mishe --> data)
#case 1--> data aye ziad dahste bashi va bgi eb ndre hazfesh kon

mydf.dropna() #behet yek dataframe jadid ba hazfe empty cell ha mide -->brizi too zarf
#harchi khalie ro hazf kon

mydf.dropna(inplace=True)

mydf.info()
#Index: 164 entries, 0 to 168
#5 ta radif ro hazf krddee

'''
 0   Duration  164 non-null    int64  
 1   Pulse     164 non-null    int64  
 2   Maxpulse  164 non-null    int64  
 3   Calories  164 non-null    float64
'''


#2.age dsatahamon kam bashan , hasas bashan --> hazf konim
#replace

mydf=pd.read_csv('/Users/apm/Desktop/data.csv')
mydf.info()
#hamaro bia bzar 0
mydf.fillna(0,inplace=True)
#yani harja empty cell didi boro 0 bzar jash
mydf.info()


#169

'''
 0   Duration  169 non-null    int64  
 1   Pulse     169 non-null    int64  
 2   Maxpulse  169 non-null    int64  
 3   Calories  169 non-null    float64
'''
#momkene empty cell hat tooye soton hayemokhtalef bashe
#temp --> 2 ta khali drte
#time -->< do ta khali

df['Temp'].fillna(0,inplace=True)
df['time'].fillna(10,inplace=True)



#**noktye: ya mitoni inakraro rooye kole datafram anjam bdi
#ya ddooone doone ro har kodom az sotoona
#bvehtar
mydf=pd.read_csv('/Users/apm/Desktop/data.csv')
mydf.info()
mydf.columns


a=mydf['Calories'].mean()
#a=mydf['Calories'].mode()
#a=mydf['Calories'].median()


mydf.fillna(a,inplace=True)


#----
#16-300
#17-->Nan
#18-3233
mydf.fillna(method='ffill',inplace=True) #17-300
mydf.fillna(method='bfill',inplace=True) #17-3233
#tartibi bashe-->method ha


#---------2-wrong format-------------
#str neveshte adad hato
s = pd.Series(['1.0', '2', -3])


b=pd.to_numeric(s, downcast='float')

b=pd.to_numeric(s, downcast='int')


#-------Time
to_datetime
'14-30-20'




#-------3-Wrong data----------
#dama ha bar hasb ekelvine ----> manfi 
#bazi jaha manfi hast 

#--->Iteration

#yek column dar ebe esme temp

for i in mydf:
    if mydf.loc[i,'temp']<0:
        mydf.loc[i,'temp']=0
        

    
#-------4-duplicated---------
#tekrari hast
a=mydf.duplicated()
#true 

for i in mydf:
    #fillna 
    #dropna ---> 
    
    
    
#*****
mydf.reset_index(drop=True,inplace=True)

mydf.columns
x=mydf['Duration']
y=mydf['Pulse']

plt.scatter(x,y)




#ya
mydf.plot(kind='scatter',x='Duration',y='Pulse')


#=======================================
#DATA -----> AMADE HAST -----> vASE INKE VAREDE MACHINE LEARNING MDOELEMON BSHE
'''
Computer --> machine hesabe pishrafte -->Ghoveye 'yadgiri ' nadarad

dar tooole in chansale kahri tamame taalshemonc in boode ke beotnim



#GENERATION 


#1 GENERATION----> hooshe masnooe besazam ---> automation , robotic, bot
#ba estefade az if o else ha shoro mikrd yejori mikhas intelligence


'''


resp=input(' ')

if resp=='salam':
    print('salam')
if resp=='khoobi':
    print('manam khobam to chetori')




print('1- gheymat chande')
print('2-shoamre tamas')
print('3-tablighat')
a=input('lotfan entekhab konid soleton ro')


if a=='1':
    print('gheymt ha b shekle zir hast lebas = 250')
elif a=='2':
    print('shomareye man 0-0393281689763 ')
elif a=='3':
    print('gheyamte tabglighat har story 1 m')
    
elif a=='salam':
    print('salam janam')
elif a=='khoobi':
    print('')


#1-kheytliii tolane
#2- asan malome inteligent
#3- yad nmitone bgire (behbood , yad bgire)


#drirect --insta --> support bot
#bot ha
#$Hooshmandi , yadgiri 


#machien robot 
#CNC ---> if , for daqstoora

#sensor

if a>20:
    Stop
  
    
#intelligent -_> hoshamnd tar mishe --> javab bde
#automation , sensitive sensor ---> Yad nemitoen begire

#hamishe b 20 brse onkaro
#hamishe oon fotbalo hamoonjori k abrname nevisi shode anjamk mide





'''

***yad begire ---->manteghi kasb --_> bar asase oon tasmim bgire va anjham bde


#1-Yad begire (asz chi ? --> data)
#2-mantegh kasb kone
#3- bar asase mantegh --> tasmim bgire (amal kone)

shoroesh yad grftne

'''


#Generation 2 --> hoosh masnoooe
#hooshe masnooe --> 1- namadin 2-amari 3-ziranmadin

#amarii --_. Machine leaning --> 70% hooshe masnooe ro machine learning 


#mano shoma mitonim bnvism
#chi kam darim

#




















'''
QUIZ........

DATA FRAME --> 100 (50,2) --> esm gzoari konid , random
tabe haro tdakhelesh bzarid

estefade konid
dropna
duplciated
to_numeric
shart bzari
filna bzarid
reset_

tamam




'''







































