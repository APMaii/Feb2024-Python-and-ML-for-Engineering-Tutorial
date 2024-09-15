
"""
In the name of GOD

Created on Thu Apr 11 12:05:09 2024

@author: apm

L13

"""

'''
Machine learning:
Ma mikhahim yek mdoel besazim
1) az data ha 'yad' begire
    2)mantegh kasb kone
        3)bar tebghe manteghesh amal kone (decision tasmim giri)
    
ML Regression 



**Regression sade --> ml nIS

'''

'''
Tamame masaele jahano --:>input-output
vorodi khoorji
rabete ee beyne vorodi khorji hast **(bayad)
**assumption: rabete ee vojod dare

...
Regression

*yek rabete e vojod dare beyne vorodi va khorojimon
in rabete --> Fgahat khdoa midone (nature tabiat)
** ma nmidonim



'''

import numpy as np
x_arange=np.arange(0,100)
x=np.linspace(0,100,1000)

y=2*x+5

import matplotlib.pyplot as plt
plt.scatter(x,y)

#in rabete e k beyne vorodi khorji has
#mitone yek khat bashe --> y= a* x + b .**a taghir kone shib taghir mikoen b taghir kone bala paeen mishe
#mitone daraje do bashe , daraj ebalaatr
#exponential , loagrithmy

#rabettaro jnemidonim -->mikhaym ke modelemon dar baire


#3D printing -->dastgahi hast --> ostyokhone masnoee mikhay
#yeseri powder dakhelesh mriizm 
#setting--> Temp --> 200 
#tolid (print) --> mibrim azmayehsgah modulus : 100
#modul-->estehkamemon cheghadre
#modulus bishtar bashe ---> estehkam bishtare


#chio ma mitonim taghir bdim-->temp (process parameter)

#harmoghe tagir midi --> estehkame ham tagir
#quality parameter ( barat moheme --> direct nmitoni taghir bdi danodne)



#temp -->taghir bdi-->estehkam ham taghir mikone
#pas ye rabete ee beyne temp va estehkam hast

# Estehkam = F (temp)
#esthekam -->Y     temp--->x
#y= jhsfkuhljo  X [pdsir[]]
#fght khoda midone ma nmidonim

#chiakr mitonim konim?-->mirim azmayeshgah va chanta migirm





x=np.linspace(0,100,1000)

y=2*x+5
plt.scatter(x,y)
plt.xlabel('temperature')
plt.ylabel('Estehkam')


#--> 200 ----> 300
#--->300 ----> 421

x=np.array([200,300])
y=np.array([300,421])
plt.scatter(x,y)
plt.xlabel('temperature')
plt.ylabel('Estehkam')

#ba do nogth enmitonim begim
#**object--> rabete ro dar bairim
#pas bayad yekari konim


#soale aval-->agha chra nmishe ba 2 ta nogthe bedast ovord-->
#dar edame momkene trend taghgir kone
#masalan yeho kahesh yabe

#afzayeshie y = +x  --> ta kioja
#2 noght enmishe javab dad

#aya mishe gof man damaro 100 ta ziad konam estehkam chnat aziad mishe
#shibesho bgirm? --> na nmishe


#10 ta azmayesh grftim

x=np.array([200,300,400,500,600,700,800,900])
y=np.array([300,421,521,590,710,810,890,920])
plt.scatter(x,y)
plt.xlabel('temperature')
plt.ylabel('Estehkam')
plt.show()
xx=np.linspace(200,900,1000)
yy=xx+100
plt.scatter(xx,yy,s=1)

#moshkel
#1- error -->dastgah ,  random error--> 

#** farze avalkie-->hamechi sabete , damaro fght taghir

#dalile inke noghatea azmayeshgahi dar oon line
#daghigh nemiofte --> ine ke ma koli errordarim



#rabete ee ke jahane hasti baraye ma tarif krde hamone sabete
#ma oono mikhaym

#ma donbale khat narenji em.



#clc ---> az avla  clea
#3d printing hast 
#ma hamechio sabet dar nazar migirm joz temp
#temp -->khdoemon taghir mdiim -->x

#y --> estehkam (quality parameter)
#meyare tasmim girite


#to donable chi ee? 
#donable rabete beyne x va y

xx=np.linspace(200,900,1000)
yy=xx+100
plt.scatter(xx,yy,s=1)
#dfar jahane hasti vojdo dare
#ama ma nmidonim
#ma hichi nmidonim
#rabet ehe kahtie ? shibesh chgdhre
#arz az mabda (shif b bal paeen
#daraje 2 , 3 ,,4 45,
#chand jomle ee
#algorit
#logar
#exopent

#vali ma mirim dakhele azmayehsgah va taghir mdiim damaro
#hey migirim y (resulkto)
#dar nahayta ma data darim
#data chie
#ye x darim ye sotoon 
#y sotoon y
x=np.array([200,300,400,500,600,700,800,900])
y=np.array([300,421,521,590,710,810,890,920])
plt.scatter(x,y)
plt.xlabel('temperature')
plt.ylabel('Estehkam')
plt.show()
#tanha chizi k dairm in noghate
#ma rabete he ro ndrim fght khoda midone
#va ma donabel rbaet e hastim
#rabte b ch drd ikhore


#man 200,300,40,500,600,700 inaro drm
#mikahm brm 250 ro bbinm , 450 ya 423 ya 1200
#ag rabete ye vageh ee ro dashte basham
#y = f (x)
#yani x ro mizari toosh -->y ro bht mide
#tasviri mikjhay bfhmi?

#bargardim az aval

#fghto fghto fght
x=np.array([200,300,400,500,600,700,800,900])
y=np.array([300,421,521,590,710,810,890,920])
plt.scatter(x,y)
plt.xlabel('temperature')
plt.ylabel('Estehkam')
plt.show()

#fek kon rabet ekhatie (hamsihe kahti nis)
#yek khat
#y = a*x + b
x=np.linspace(0,10,100)
#a=1 b=0
y=x
plt.scatter(x,y,s=1)
plt.show

#a=4, b=0
y=4*x
plt.scatter(x,y,s=1)
plt.show

#a--> tagir midi shib ziad msihe
#b -->
#a=1 b=10
y=x+10
plt.scatter(x,y,s=1)
plt.show


#yek khat ro shoma fght ba a o b mitoni hzarta khat bsazi


#hala brgrdim aghab
#in datahamone
x=np.array([200,300,400,500,600,700,800,900])
y=np.array([300,421,521,590,710,810,890,920])
plt.scatter(x,y)
plt.xlabel('temperature')
plt.ylabel('Estehkam')
plt.show()


#ma donable ye rabete
# estehkam = ? temp
#rahat temp --> too in maodele -->estehkam bde


#man az taarfe tabiat miam bht migam khatie in rabete
#y = a * x + b
#estehkam = a* temp + b

#a o b chande?

x=np.array([200,300,400,500,600,700,800,900])
y=np.array([300,421,521,590,710,810,890,920])
plt.scatter(x,y)
plt.xlabel('temperature')
plt.ylabel('Estehkam')

xx=np.linspace(200,900,1000)
#a=1 b=0
yy=xx
plt.scatter(xx,yy,s=1)
plt.show()



x=np.array([200,300,400,500,600,700,800,900])
y=np.array([300,421,521,590,710,810,890,920])
plt.scatter(x,y)
plt.xlabel('temperature')
plt.ylabel('Estehkam')

yy=xx+100
plt.scatter(xx,yy,s=1)
plt.show()

#ba farzo hads nahayat shabihesh btonim bgim

#ensan chikar mikone?
# a o b random gofti
#bad hey gofti gofti
#


#faseley kole noghat ta khate --> 5  khatashe enherfaesh
#
# yer a op b dgh dar nazar migiri

#oon fasele he b kmatarin brese


#yek machine --> yek algorithm
#chijori regression


#hooshe masnoe
#1)az data yad bgire (ba ye raveshi)
#2)mantegh kasb kone ( y = a*x + b) a o b ro dar baire
#3)vorodi bdm (x)---> BOX -->y
#**BOX --> y = A*x + B

#Linear Rgeression 

#-----pip install sklearn
#import libname
#import libname as mokahfaf

#bazi ketabkhone ha kheyli hajiman
#va ma b hamash niaz ndrim

#from libname import felan_class_taba
#fght felan_class_taba 

import sklearn
#ma inakro nmikonim


from sklearn.linear_model import LinearRegression

#az ketbkhoneye sklearn, linear_model(safe chat script)
#az in import kon 

#shoma hamishe ye zarfi b esme model bsaz
model=LinearRegression() #k azaash estefade konim
#-->mokhafaf , settingato inja taghir bdi

x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])
plt.scatter(x,y)
plt.xlabel('temperature')
plt.ylabel('Estehkam')
plt.show()


model.fit(x,y)
#yad begir , train bbin , moadele ro


#hamchio too dele mdoel zakhri emikone

#yekseri tabe dare
#yekseri adade sabet
#mitoni baraye pishbini 
#x o midm behet y ro bde
new=np.array([550]).reshape(-1,1)
predicted_value=model.predict(new)
print(predicted_value)
#[645.25]


xx=np.linspace(200,900,1000).reshape(-1,1)
yy=model.predict(xx)
plt.plot(xx,yy)

x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])
plt.scatter(x,y)
plt.xlabel('temperature')
plt.ylabel('Estehkam')
plt.show()


#shib --> a
model.coef_ 
# arz az mabda-->b
model.intercept_

# y = 0.913*x + 142.
# estehkam = 0.913* Temp + 142

#=====================
#linear regression ( sadfe ml**)
x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])
#datamone
#x--dama y-->estehkam
#rabeteye beyne y o x k dar jhjahan vojdo dare va ma nmidonim
from sklearn.linear_model import LinearRegression
model=LinearRegression()

model.fit(x,y)
#y=a*x + b koli khat bsazi 
#miad rNdom a o b ro mizne hey khat msiaze
#hey cost functgion misaze vase har khat(faseleye khat) error
#khati k kamtarin lost function dare(nazdik tre behame)
#y = A*x + B yani A o B ro drovorde

#mikhay bbini A chie B chie
#estehkam = A*Temp + B

A=model.coef_
print(A) #[0.91333333]
B=model.intercept_
print(B) #142.91666666666686
#Y= 0.913 * x + 142

#hadafe az rabete --> ye x i bdi behesh 
#y ro bde
new=np.array([623]).reshape(-1,1)

y_pred=model.predict(new)
print(' Y emon baraye x e 623 hast :',y_pred)
# Y emon baraye x e 623 hast : [711.92333333]


#rasm koni khoshgel
xx=np.linspace(200,900,1000)
yy=A*xx+B
plt.scatter(xx,yy,s=1)
plt.scatter(x,y)
plt.show()


xx=np.linspace(200,900,1000).reshape(-1,1)
yy=model.predict(xx)
plt.scatter(xx,yy,s=1)
plt.scatter(x,y)
plt.show()



#===============================
#jadid
x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])
xx=np.linspace(200,900,1000).reshape(-1,1)
yy=model.predict(xx)
plt.scatter(xx,yy,s=1,label='Predicted')
plt.scatter(x,y,label='Experiemntal')
plt.xlabel('Temp')
plt.ylabel('Estehkam')
plt.legend()
plt.show()


#az koja betonam begtam ke
#IN KHATI k man darovordm daghighan hamnonie ke 
#dar jahane hasti vojod darad?

#chegone valdiate konam?

#bdehtarin rha--> berim etst konim
#ma akhob man k kari nakardm baz pamon baragsht b azmayeshgah

#kssi ide ee dre ke chiak rkonim

#aga rinakro konm---> REGRESSION SADE --> R**2
#--->daghigh yek score va in relaiable ( gahebele etemad)


#ghabl az harchiizi datato train tes


#======================================
#model --1)Modele ML LR
#0-data import (open),web,
#data-->dataframe
#0.0cleaning -->dataframe gahbeel esteafde

#yekseri radifo dsoton--> x o y taghsim konim
#berizi too x berrizi to y
x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])

#1-> train test split -->
#bejaye inke bhri train bdi roo kolesh badan bri azmayeshgahy
#dotar chantaro vardar bgo inaro ndrm

from sklearn.model_selection import train_test_split

A=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)

#miad x o y ro migire 4 gehsmat mikone
#kle dta aro --> train , tes
#khdoe dat x y ----> x train y train , x test y test
'''
plt.scatter(x_train,y_train,label='Train')
plt.scatter(x_test,y_test,label='tETS')
plt.legend()
plt.show()
'''

from sklearn.linear_model import LinearRegression
model=LinearRegression()
#dg rooye x o y nmizne
#dght rooye oon shish t a a mikhay bzni
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

from sklearn.metrics import mean_absolute_error
score=mean_absolute_error(y_test,y_pred)
print('ekhetalf (khatey nemoone) hast:',score)
#ekhetalf (khatey nemoone) hast: 20.69999999999996
#+- 20 ta barat pishbini mikone

from sklearn.metrics import mean_absolute_percentage_error


score=mean_absolute_percentage_error(y_test,y_pred)
print('darsade ekhetalf (khatey nemoone) hast:',score)

#darsade ekhetalf (khatey nemoone) hast: 
    #0.02971921644526543
#yani 2.9 darsad khata dare modele

score=model.score()
#r2

x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])
xx=np.linspace(200,900,1000).reshape(-1,1)
yy=model.predict(xx)
plt.title('MAPE of LR model:0.0297 ')
plt.scatter(xx,yy,s=1,label='Predicted')
plt.scatter(x,y,label='Experiemntal')
plt.xlabel('Temp')
plt.ylabel('Estehkam')
plt.legend()
plt.show()



#kole ML hamin workflow
#fght fagrh ine
#har mdoel b ye ravesh joda rabete ro dar miare (capture)
#non linear ro capture mitone
#gheyre gkhatio

#kolasn hamine
#fght oonaj k mineisi model
#model=LinearregressioN()
#MODEL=svr()


#chiz hae k goftam --_.REGRESSION--> y emoon peyvaste


'''
ADAD HAA:
    1)PEYVASTE--.1.3223 2.32 3 45 
    2)GOSASTE__chanta ee (afrade dakheel kelase) 30.2 30.5

dar hooshe masnooe
tamame mosheklate jahano--> x -y 
vorodi khoroji
khoroji ----> peyvaste----> Rgeression
khoroji-->gosaste ---> jozve kodom daste-->daste bandi _-->classification

hamechi yekie

Machine learning ----> 
Supervised[ regression , classification]
Unsupervised


'''


'''
pip install sickit-learn
sklearn

x--> 
y--->
x--.speed
y-->

--> x o y
---> train test
--->model LinearRegresion fit
---.score---
-->rasmesh kon


Ai.2024.pilehvar@gmail.com


'''


import numpy as np
x=np.array([1,2,3])
(3,)

x=np.array([1,2,3]).reshape(-1,1)
(3,1)


#yadet bashe yeseri setting
class LinearRegression():
    
    def fit(x,y):
        #while
        cost_function=[]
        for i in range(0,100):
            
            a=np.random.uniform(1,10,size=(1,))
            b=np.random.uniform(100,1000,size=(1,))
            y_pred=a*x+b
            
            cost_function.append(sum((y-y_pred)**2))
            
            for i in cost_function:
                best_line=min(cost_function)
                A=a
                B=b
            rint('finish')
    self.A=coef_
    self.B=intercept_
    
    def predict(new):
        y_predict= A*new+B
        return y_predict
                














