
"""
In The Name Of God
Created on Sun Apr  7 15:01:34 2024

@author: ai.2024.Pilehvar@gmail.com

L12


****1) MANTEGH ( IF , ELSE, FOR ,... , built in python ( open,print))
**2) tarigheye kar ba zarfa , lista , **tedade ziadi tabe haye str (lower upper ) .append
**3) list-->array (tabe goftim [manteghesh ro balad bashim])
**4)pandas ---> dataframe. cleaning method ---> step 0 e karemon

**5)hooshe masnooe (AI)


"""

#**sade tarin kar emomken -->print

print('salam khobi')

#arg -->manetghe -->setting --.dastemon baze
print('salam khoobi')
print('khodafez')


print('salam khobi',end='**')
print('khobi')

#dastam baze



#**numpy--> 10000 function --> mohem trina --> arange , besazim
#man --> 100 ta tadris krdm , 1000
#azoon 100 ta 10 ta hefz 
#-------
#STEP 0 ------>pandas [generatesh msieh np,if else (iteration)]
#Multiple ---> sklearn
#step akhar-->matplotlib
#------
#review pandas----> step 0 
#vorodi data
#1-open --->datafrasm
#----------------------------0.0 IMPORT LIBRARY
import pandas as pd
import numpy as np
#----------------------------0.0- IMPORT DATA
#hadaf-->kole data -->dataframe
#1) generate
a=pd.DataFrame([[1,2],[4,5]],columns=['A','B'])

#cast
a=np.random.randint((2,5))
b=pd.DataFrame(a,column=['Name','NAME'])


#2)Az mycomputer
#2.1
a=open('c://user/ali/data/ftir.txt')

b=pd.DataFrame(a)

#2.2) mostaghim az khdoe pandas
a=pd.read_csv('/Users/apm/Desktop/codha/data.csv')


#directory not found .... path not found
a=pd.read_csv('data.csv')

#3)import from library
from sklearn.datasets import iris_data
a=iris_data()


#4) az website --> 


#**********data ro ma rikhtim too ye zarf b formate DATFRAME



##----------------------------0.  1- CLEANING DATA

#dataee k ovordi momkene perfect nabashe
#cleaning 
# momkene t4 ta naghs dashte bashe

#operation
#access-------
a=np.array([[1,2,3],[4,5,6]])
data=pd.DataFrame(a,columns=['Temp','time','Modulus'])

#numpy bsazi 50 ta radif bashe 2 ta sotoon (50,2)--> 0 ta 100
a=np.random.uniform(0,10,size=(50,3))

data=pd.DataFrame(a,columns=['Temp','time','Modulus'])
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


data.drop(index=4,inplace=True) #emal mikone dg niazi b zarf nis

#chanta naghs hast 
#1-empty cell
#2-wrong format
#3-wring data
#4-duplicated (tekrari)

#1-empty cell------------------------------------
#ghemsnate 0.0
mydf=pd.read_csv('data.csv')
#clean
mydf.info()
mydf.dropna(inplace=True)
#drop nakonid replace konid
mydf.fillna(10,inplace=True)
z=mydf['tem'].mean()
mydf.fillna(z,inplace=True)
#Method ffil 

#2------------
#adadaro b soorate str save krde '1' '2' '3'
s=pd.Series(['1.0','2.0',-3])
b=pd.to_numeric(s)

df['sale date']=pd.to_datetime(df['sale date'])

#3---------
#ye eshkale manteghi dare
#accesss iteratiuon
#bayad beri too dat abegardi ye shart (IF), drop or fill

df=pd.DataFrame([[100],[33],[24],[63],[474],[213],[224],[-2],[21],[13],[4]],columns=['TEMP K'])

#phyisc--> kelvin --> zire 0 nadarim 0 Kelvin
#11 ta nemone hast dmaahahso neevshte
#eshtebah karde datsgahe . operator , eshtebahi
#bayad bri doone doone begrdi tooye datat
#shart bzarei ( age dama zire 0 shod )
#aaction--> hazfesh kon , ya replace

#boro done done radifaro
#drop --> rmeovbe
for x in df.index:
    if df.loc[x,'TEMP K']<0:
        #action
        #2 ta rah
        df.drop(x,inplace=True)
        
#replace      
for x in df.index:
    if df.loc[x,'TEMP K']<0:
        #action
        #2 ta rah
        df.loc[x,'TEMP K']=20
              
#4----duplicated
df.duplicated()
#false--> nist -->tekrari nist --> ag tekrari bashe
#fahmidm bkham hazf konm drop konm
#iteration
df.drop_duplicates(inplace=True)



#---->Data ee toye 0.0 import krdim , 0.1 cleaning --.CLEAN
#tamize tamzi va mishe azash baraye hoosh emasnooe estefade krd
#===================================================
#===================================================
#===================================================
#===================================================
#===================================================

#data----> #dar mohandesi --> data frame chnata RADIF , soton dare
#radif -->tedade nemone (number)
#sotoon-->feature (vizhegi , property)

#data --> excell , csv , [Table]--> literature,dastgah , measurement 
#ax , film, seda , signal , movie --> table

#Data frame ---> CLEAN

#HOOOSHE MASNOOE CHIE? --> yade ye robot nayoftadid

#2 generation --->

#Genration 1---> sade  --> if o else --> automat
#direct insta --> 10 ta gozine gozahste hrkodomo bzani y javb mide
#if else 
#support customer
if text=='salam':
    print('salam')
    
#salaaam 
if text=='salam' or text='salaaam':
    print('salam')

#computerr--->(mashin hesabe sade) --> shabihe ensan rftar kone
#nnasle 1



text=input('you: ')

if text=='gheymat':
    print('Gheymat ha update msihe farda')


text=input('you: ')
if 'gheymat' in text:
    print('Gheymat ha update msihe farda')


#inteligent ---> hooshmand tar konan
#dar nahayat 0---> if o else


#CNC ---> COMPUTER NUMERICQLAL CONTROL
# G , apt , ...-->python

#for x -->y -->signal motor

#hooshmand 

#robot ---> hooshmand tar shodan
#sensor bzarim dore ssareewesh
a=import
'''
fasleey beyne robot ta oon object 200 300


'''


#100 ta ghete
for i in range(0,100):
    
    if a<5:
        break
    #
    #
    #x--Y
    #y--c
    #coolant
    #
    #
    #
    
#robot --> hamon cnc ie fghht ag kasi nazdik tar az 5 metr shod
#break mikone--stop

#threshold--.astane

#**AUTOMATION
#co-robot --->interaction


#----------------
#nasle 2----> Mashinemon (computer, robto,model,algorithm , ml,tabe)
#for (tekrar) , if (shart sensitive)
#mikhamm---->'YAD BEGIRE'

#ensan --> vorodi (gooshashe, cheshamshe, damagh , maze)---> BOX (MAGHZ) -->khoroji (ba dastamon)

#data --->video youtube --> tardasti yad mdie
#mire --BOX9amghz)--.yad migire
#khoroji --> ba dastam (medchanici)


#machine man --> maghz (box)----.YAD BEGIRE YAD BEGIRE
#LEARNING -->YAD GIRI

#------------
#ROBOT (cnc + sdensitive snesor approximation)
#footbal bazi kjone
#sensor mziarna kamaresh --> if force>50 -->signal bfrs
#for if else
#hamishe yek karo mikone
#nahayat stop kone
#ama mavarede nashenakhte bashe hang mikone

#rooo shikam boikhore na na
#behtaram
#yadgiri---> pre-programmed (az ghabl barname nevisi shode)



#MOSHKELE NASLE 1:
    #---->KHEYLI BAYAD codee bzni 1000000 
    #---->hamishe sabete-->yadgiri ndre--> behtr nmishe, msaele nashenakhteva jadid --.error
    
    
    
#nasle 2 ---> yadgiri dashte bashe 
#ARTIFICIAL INTELIGENCE ROBOT
#yekbar trainesh midi
#bad yad migire
#code kamtari nvshtim
#in hamvare behtar mishe 
#yek chize nashenakhte etefagh biofte--error mide
#ai robot--.error -->handle mikone -->yad grfte



#ENSANN---------------------------
#DATA ---> yad migiire ---> AMAL MIKONETASMIM MIGIRE)

#1)train ( LEARNING)--->yad migire
#2)mantegh kasb mikone ( relastionship)
#3) Action ( decision making ) -->tasmim migirre bar asase on mantegjhi k kasb krde

#soale yek
#yad migire? az chi ?? az data
#data-driven model


#--------------------------
#cls clc

#kole jahan hameye jahano ---> b yek masale ee bename
#input-output (vorodi khoroji) tabdil konim

#box
#AI

#yechizi midi
#vorodi behesh bdim ( harf bzni, data pishbini, data tashkhis, film , text bg)
#(too box (AI))
#azash khoroji(harfm mikhay, adasdo , ax , ax , film   )



#stepeeeeee 2* (use)
#input -->BOX ---> Output
#bayad in hosh amsnoe ayd grfte bashe box train

#1* (traiuning)
#data (input ., output) --> BOX -->rabeteye beyne inpuit-output darmiare



#1*-->train  2*use (action)
#2*--> behesh ax bdim (vorodi)--> rabtearo -->horoji mdie



#MASAELE JAHAN
#input , output
#hooshe masnooe rabeteye beyne vorodi va khoroji ro dar miare (train)
#VORODI 
#RABETE RO DRE
#KHOROJI MIDE

#soala
#vorodi khoroji chie? 
#rabetey beyneshon ro chijori dar miare?
#khorojiamon chian 

#REGRESSION------------------------------------------------
#hooshe masnoe nist ******


#voroodi ----rabete----- khooorji 


#3d printing---------(cnc , unconbventional)
#mavade avalie --jesmi mide ( estehkamesh )

#quaklity parameter ( parmaetere keifiat --> khoorji)

#dastgah -->koli setting dare
#speed
#melt temperature

#speeed 0  -->daste toe (khdoet taghir)
#speed=20

#har tagiri k rroye speeed bdi -->khorojitam tagir mike
#0 ---> estehkame 100
#10 --->estheka 80
#30--->estehkam 60

#vorooodi--->ma mitonim taghir bdim ( speed)
#khorojim-->quality aprameter--estehkam

#yek rabeteye ee beyne voorodi va khoroji hast -->spped on modulus

#BOX ---> in rabetasro yad bgire
#vorodi (speed) ---> estehkamo bde



#azmayeshgah 
#5 ta speedd--> 10 20 30 40
#hardafe ham azmayesh 900 800 700 600

a=np.array([[10,900],[20,800],[30,700],[40,600]])

#momekne ya az web, article, dastgah ..-->data (dataframe)
data=pd.DataFrame(a,columns=['speed','estehkam'])

import matplotlib.pyplot as plt

plt.scatter(data['speed'],data['estehkam'])
plt.title('3D PRINTING DATA')
plt.xlabel('Speed ')
plt.ylabel('ESTEHKAM')
plt.show()


#yek khat

#Y = A*X + B
x=np.arange(100)

a=1
b=0
#y=x

y=a*x+b
plt.scatter(x,y)
plt.xlabel('x ')
plt.ylabel('y')
plt.show()



x=np.arange(100)

a=2
b=0
#y=x

y=a*x+b
plt.scatter(x,y)
plt.xlabel('x ')
plt.ylabel('y')
plt.show()




x=np.arange(100)

a=1
b=0
#y=x

y=a*x+b
plt.scatter(x,y)
plt.xlabel('x ')
plt.ylabel('y')
plt.show()


x=np.arange(100)

a=1
b=10
#y=x

y=a*x+b
plt.scatter(x,y)
plt.xlabel('x ')
plt.ylabel('y')
plt.show()


#yek khat --> ba a o b mitoni 

#a b 



a=np.array([[10,970],[20,830],[30,713],[40,540]])

#momekne ya az web, article, dastgah ..-->data (dataframe)
data=pd.DataFrame(a,columns=['speed','estehkam'])

import matplotlib.pyplot as plt

plt.scatter(data['speed'],data['estehkam'])
plt.title('3D PRINTING DATA')
plt.xlabel('Speed ')
plt.ylabel('ESTEHKAM')
plt.show()



a=np.array([[10,970],[20,830],[30,400],[40,300]])

#momekne ya az web, article, dastgah ..-->data (dataframe)
data=pd.DataFrame(a,columns=['speed','estehkam'])

import matplotlib.pyplot as plt

plt.scatter(data['speed'],data['estehkam'])
plt.title('3D PRINTING DATA')
plt.xlabel('Speed ')
plt.ylabel('ESTEHKAM')
plt.show()






#dar physic shimie ghaazi --> farayand ---> x o y 
# ESTEHKAM = A * speed + B



x=np.arange(100)
x=np.arange(0,51,10)
a=2
b=0
#y=x

y=a*x+b
plt.scatter(x,y)
plt.xlabel('x ')
plt.ylabel('y')
plt.show()
xx=np.array([0,10,20,30,40,70,90])
yy=np.array([0,22,45,54,76,148,190])
plt.scatter(xx,yy)
plt.show()



'''
SUMMURY:
    
hooshe masnooe chist?--> HOOSH + MASNOOE
ARTIFICIAL INELLIGENCE --> MASNOOE + HOOSH
yani shabihe maghe ma bashe

maghze ma mage chijorie? --> maghze ma mitone yad begire 'learning'

do nasl az hooshe masnoee bod
1st generation: in ha hamoon if o else boodan ke masalan Direct
e insta, customer support, cnc, robota va ... amd ina hamashoon hamsihe
pre-programmed boodan yani az gahbl barname rizi dashtan
naghseshoon in bood ke --> kheyliii bayad barname minevehstim
bayad hamechio az ghabl pishbini mikardim va faghta ina ejra mikardan
pas yani age yek chize jadid (unseen, unkown) pish miomad error midad
va imporve (behtar nemishod) choon faghede vizhegie 'yadgiri' bood

pas goftan bia yechizi besazim ke yad begire
2nd Generation: Machine learning--->yani in computeremon
ke yek mashin hesabe sadas k az koli 0 o 1 tashkil shode betoone
'yad begire'-->injori ba code e kamtar mitone bhtrin amalkardo neshon bede
dar movajehe ba yek condition va vaziate jadid o nashenakhte
error nemide balke choon yad grfte mitone handle kone.

pas daghighan mesle yek esnan chnat step dare:
    
    1)az daata ha yad begire (learning)
    2)yani mantegh kasb kone (relationship)
    3)bar asase in mantegh action konde(decision making ya tasmim giri)
    
khod hamantor ke goftim in ravehs ha bar payeye dade hastan ya 
behatre begim data-driven methods. pas niaz b data darim

data chie?--->tamame masaele jahan ro ma mitoonim b input-output
ya behtare begim vorodi-khoroji tabdil konim
pas dataa aye ma yek data fram has k yekseri vorodi dare yekseri khoroji
va bnayad mdoele ma roosh yad begire.

in vorodi mitone table bashe, adad bashe , ax bashe , seda bashe
ama 

hamantor ke goftim bar asase noe khoroji k az mdoelemon mikhaym,
mitoonim hooshe masnooe ro be chanta zir majmooe taghsim konum
yeki az zir majmoe hash ML regression hast.


Ghabl az inke varede ML regression beshim bayad bebinim ke
khode regression e sade (na ML REGRESION) balke khode regression che mikone?


------regressione sade--------
Bebinid hamishe beyne vorodi va khoroji yek rabete ee hast k
fagahto faghat khoda midooonatesh.
masalan rabete yek x ba y has y=2*x+3
ino faghat khdoa midone ma nemidonim hcihhki nemidone
masalan rabeteye beyne metrazhe khoone ba gheymatesh ehtemalan
yechizi mesle in moadele hast --> gheymat = 100 * metrazh + 20
masalan, ma nmidoonim vaghena k in formol chiee
mesle --> rabeteye beyne tedade khordne pitza dar sal ba feshar ekhon
masalan shayaad in bashe --> feshare khoon = tedad / 30 + 11
masalan ag ye fard dar sal 60 ta pitza bokhore 60/30 mishe 2 and +12
mishe 13. 
ya masalan yek dastgah dar nazar begirid (harchii, 3d prinitng,
                                          milling, casting harchizi)
fek konid yekseri mavad mirizim troosh va ye settingi dare ke mitone
dama bashe , sorat bashe ya harchize takahsosi tar
biayn dasr nazar begirid faghat sorat bashe
yai vaghty mikhayn yek made ro tolid konid bayad sorat ro tanzim
konid va har dafe tolid mishe mirid modul ya hamon estehkam ro
andaze migiri va ye adad beyne 100 ta 1000 hast. harchi balatgagr
behtar.
khob dar donyaye vaghe ei ( dar tabiat ) hatman yek rabete ee
beyne sorat va estehkame oon made hast ke fght khdoa midoone va ma 
nemidonim.

khob ma mitonim har dafe berim sorat ro yechizi bezarim
va tolid konim va berim bebinim estehkam chie.
ba in kar mitonim berim chnata nemone besazim va andaze giri konim
ama bekhatere 'zaman', '  hazine' va ..--> nemitonim berim
done done hame sorat haro hesab konim.
pas dar nazar begirid berim 5 ta sorat begirim 10 20 30 40 50
bad done done har sorat ro mirim migirim y jesm sakhte mishe
done done har jesm ro mirim estehkam ro migirim va b tartib
mishe 120 240 310 401 520.
khob dar asl in data moon hast yani vortodimon has sorat ke
ma mitoonim taghir bdim (x)---> be in migan voorid
khoroji-->onike moheme o mikhaym bedonim --> keyfiatemone
parametere nahaeimone --> estehkam.
khob ba negah fght behesh mitonim begim ke yek rabete 
y=10*x hododan has yani estehkam=10*sorat
yanichi? yani ma donbale ye rahi hastim ta oon moadele he ke
fagaht khoda midone ro peyda konim. hata oon moadele y=10*x nis
balke yechizi hast injori y=a*x+b yani a o b nashenakhte hast
pas ma bayad ye raveshi pedya konim k betone ba estefade az in 5 ta 
nemoone ke darim biad va in a o b ro bedast biare
ag ma bedoonim k rabete beyne estehkam ba sorat masalan ine:
    
    estehkam = 10*sorat + 20
    
onmoghe ma tonestim **rabeteye beyne vorodi va khoroji ro dar bairim
yani mitonim sorat3 60 masalan nadashtimesh bayad miuraftum
too azmayeshgash v bedast miovordim. alan mitonim bezarim too moadele
estehkam= 10*60 + 20 = 620 
va haal kheyli sade dg mitoonim biaym edea konim begim in rabete he
rabeteye beyne vorodi khorojie va dg azin estefade konim.

Inja model(hooshe masnoe) hamoon BOX e hast
yani ye box hast k aval behesh migim 1**) in data ro train bebin
    datamoon ye vorodi dasht (oon 5 ta sorat) va ye khorojie
    (5 ta estehkam)
hala migim ke azin train bbin yani rabeteye beyneshon ro dar biar
2**) vaghty in rabete ro darovord(mantegh kasb krde bar hasbe dade ha)
mitonim be in box (model) vorodi jadid bedim va miad
vorodi ro migire mizare too formol va bema khoroji mide.

B hamin sadegi.



HALA YEK SOALE KHEYLI KHEYLI MOHEM.
midonim hameye masaele jahano mishe be vorodi khoroji ( x o y ) 
tabdil kard. khob too in masale masalan midonestim k 
y=10*x + 20 hast.
dar morede masaaele dg az koja bedonim ke rabetey beyne
vorodi khoroji ( rbateey beyne x o y) chie??
model(box)-->machine learning model --> miad va az rooye data haye 
mojod (yani oon 5 ta x o y ) --> Ba yeki az ravesh haye amari
oon rabete ro bedast miare.

Dar inja ma yeki az in ravehs haro migim k esmesh has
regression.
koli raveshe dg vojod dare ke dar edame migim.


Pas dar nahayat:
1)Yekser data darim ( yek data frame az x o y hast) k dar donyaye
    vaghei yek rabete ee beyne x o y hast k ma nemidoni,
2)mdiimesh be mdoelemon k mitone rabete x o y ro dar baire 
    (az tarigeh yek raveshe amari)
3)sepas mantegh kasb mikone yni mige (y= felan*x + felan)

4)hala ke 'yad gereft' mitonim estefade konim azash yani ye 
    vooorodi jadid midim va bema khoorji ro mide (pishgbini mikone)
    yani maid mizare too oon formol va bema y ro mide
    kodom formol?-->hamon formoli k az data ha yad grfte
    
    
**hALA YADETON BASHE IN YEK REGREESSION SADE BOD
frghe regression ba yek ML regression ( yek modele hoshe masnoe) chie?
jaalse badi kamel toizh dade mishe
Moafagh bashid


'''








