
"""
IN THE NAME OF GOD


Created on Wed Apr 17 16:31:42 2024

@author: ai.2024.pilehvar@gmail.com

L15
"""
#recap--> input/output
#supervised----> classification / regression bar asaszew khoroji k peyvaste bashe y agosaste

#ch baray eclasification
#dch baraye regression haamshhh yekie


#=================================================
#MACHINE LEANRING REGRESSION---------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#=================================================
#0.0.-data improt ( dasti , csv excell , downlaod, import)
#0.1.-cleaning (pandas emthod dropna, duplicated wrong format)
#=================================================
#1-datato --> x o y  [jadvale] input , output
#**agar x et ye soton bod--> reshape estefade
x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])
#=================================================
#2-train test split --> yek bakhsi too train , test
from sklearn.model_selection import train_test_split
#in yek tabast k mige x o y ro bede manm man behet
#4ta adad midam --> 4 ta list ro mirizi to zarf hay emotefavet
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)
#=================================================
#3-model selection-->modeleot entkerhab mikone
#ML LR -->Macxhine elarnin linear regression
from sklearn.linear_model import LinearRegression
model=LinearRegression() #tooye parantez yekseri setting has mitoni tagir bdi k rooye yadgirish tasir dre
#KNN , DT , RF , G, SVR , MLP
#baladi agha
#from sklearn.tree import DecisionTreeRegressor
#model=DecisionTreeRegressor()
#=================================================
#4-fit mikoni roye train data--> oon train dataset
#modelto roosh fit mikoni -->train midi-->
#yani mdoelet ba raveshe khdoesh (LS)-->rabetaro dar miare
model.fit(x_train,y_train)
#=================================================
#5-evaluation , validation --> sanjesh koni modeleto
#**train score and test score
#x test y test 
model.score(x_test,y_test)
#Out[41]: 0.983926883909041
from sklearn.metrics import mean_absolute_percentage_error
y_pred=model.predict(x_test)
score=mean_absolute_percentage_error(y_test,y_pred)
#in tabe he mire ekhtelafe magahdire
#pishbini shode ra ba magahdire vaghe e dar maire

#diff (ekhtealfe pred experiment )
#prediction ,true --> khdoehsono kam mikone

#MAE  mean_absolute_error  y_true - y_pred
#MSE mean_squared_error   y_true - y_pred
#RMSE math.sqr( )
#MAPE mean_absolute_percentage_error y_true - y_pred / y_true

#1--->aval bbinam khob yad grfte ya na
y_pred_train= model.predict(x_train)
train_score=mean_absolute_percentage_error(y_train,y_pred_train)
#khate ma ba train ha cheghadr ekhtelaf dre--->chgdh khoob amozwesh dide
print(train_score) #0.03647472454999043


y_pred_test=model.predict(x_test)
test_score=mean_absolute_percentage_error(y_test, y_pred_test)
print(test_score) #0.02971921644526543


#MAE
from sklearn.metrics import mean_absolute_error
score=mean_absolute_error(y_test,y_pred)
print(' Accuracy : ',score) #20.69999999999996
#modele ma harchi pishbini krd khatash +- 20
    
#MAPE
from sklearn.metrics import mean_absolute_percentage_error
score=mean_absolute_percentage_error(y_test, y_pred)
print(' Accuracy : ',score)  #0.02971921644526543
# 2 az 100 --> 2 dar sad -->2%
#deghate modele ma -->harchi pishbinui kar +- 2.9%
##=================================================
#6-predict --> box behesh vorodi bdi khoroji bgiri
new=np.array([450]).reshape(-1,1)
new_pred=model.predict(new)
print(' baraye  damaye 450 , estehkam pishbini mishavad : ',new_pred)
#549.525
##=================================================
#7-Plot , rasm
import matplotlib.pyplot as plt
x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])
plt.scatter(x,y,label='Experimental')
xx=np.linspace(200,900,10000).reshape(-1,1)
yy=model.predict(xx)
plt.scatter(xx,yy,s=5,label='ML Predicted')
plt.title(f' Accuracy MAPE { score}')
plt.xlabel('Temp')
plt.ylabel('Estehkam')
plt.legend()
plt.grid()
plt.show()





#================================
#classification
#mesalll
#yekseri ghorbaghe
#26 ta ghorboaghe didam
#tool o arze harkdoomo dsarovordm
#dota ghorbaghe darim---> jahande  shabtab
#1-----> 20cm   2cm      jahande
#2
#....
#26 


#data--> se ta soton 26 ta radif
#radifa-->tedade ghrobaghe
#2 sotone aval-->vizhegi (vorodi0)
#3---> target , ouytput ( jhanade 0  shabtab 1)

#refigham mire
#rabteye beyne (tool,arz)---> noe ghorbaghe --> daste bandi

#------
#saratno , ---> 200 bimar , harkdom 10 ta vizhegi
#moshakhseye khone , moshakhaseye phe khone ,
#khoroji--> are ya na
#ya saratan daran y ana 0 1
#industrial--> shekast ndre 0 shekast dare 1

#0---> import datahmo
#0.1. cleane

#1- b x o y tabdil konam
#x -->vorodi-->vizhegi , dasste mae
#y-->target ---> chizi k barmaon moheme , regression-->quality parmaeter , classification-->type

import numpy as np
x=np.array([[ 9.96346605 , 4.59676542],
 [11.0329545 , -0.16816717],
 [11.54155807,  5.21116083],
 [ 8.69289001,  1.54322016],
 [ 8.1062269 ,  4.28695977],
 [ 8.30988863,  4.80623966],
 [11.93027136,  4.64866327],
 [ 9.67284681, -0.20283165],
 [ 8.34810316,  5.13415623],
 [ 8.67494727,  4.47573059],
 [ 9.17748385,  5.09283177],
 [10.24028948,  2.45544401],
 [ 8.68937095,  1.48709629],
 [ 8.92229526, -0.63993225],
 [ 9.49123469,  4.33224792],
 [ 9.25694192,  5.13284858],
 [ 7.99815287,  4.8525051 ],
 [ 8.18378052,  1.29564214],
 [ 8.7337095 ,  2.49162431],
 [ 9.32298256,  5.09840649],
 [10.06393839,  0.99078055],
 [ 9.50048972, -0.26430318],
 [ 8.34468785,  1.63824349],
 [ 9.50169345,  1.93824624],
 [ 9.15072323,  5.49832246],
 [11.563957  ,  1.3389402 ]])

y=np.array([[1, 0, 1, 0, 0, 1 ,1 ,0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0]]).reshape(-1,1)


#vzihegie 1 ro dar barabare vizhegie 2 rasm kon
#har noghte--> yek ghorbaghe

import matplotlib.pyplot as plt
plt.scatter(x[:,0],x[:,1],c=y)
plt.ylabel('Tool')
plt.xlabel('Arz')
plt.show()


#classsification
#KNN-------------
#0.import
#0.1 clean
#1. x oy
#split test train
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)
###6 t aro test

#model 
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=2)
model=KNeighborsClassifier(n_neighbors=5)
model=KNeighborsClassifier(n_neighbors=9)
#train
model.fit(x_train,y_train)

#validation
#test score, train score
#rahat tarin kar mdoel -->score
#az 6 ta chanbtasho doros pishbini mikone
test_score=model.score(x_test,y_test)
print(test_score) #0.5
#0.8333333333333334



train_score=model.score(x_train,y_train)
print(train_score) #0.95
#0.95

#predict
new=np.array([[15,3]])
predshode=model.predict(new)
print(predshode) #[0]



#hyperparameter -->fara paraameter
#LR
#ch baraye regression ch braye clasification
#KNN , DT , RF, SVR , MLP
#parametr--> tasir mziaran rooyer yadgirishon
#va ma ham bayad entkehabeshon kjonim
#beshini done done 
# for


score_list=[]
for k in range(1,11):
    model=KNeighborsClassifier(n_neighbors=k)
    model.fit(x_train,y_train)
    score=model.score(x_test,y_test)
    score_list.append(score)

xx=np.arange(1,11)
plt.plot(xx,score_list)
plt.ylabel('Accuracy')
plt.xlabel('N_ NEIGHBOUR')
plt.show()

#neighbor 
#metric -->mohem tairnan
#hyperparameter

#complexity


#complexity -->kam bashe-->bikhial--.ayd nmigire -->train score paen -->etst score mnid paen
#ag kh complex ---> ziad bashe--> kh biased--> taasob-->noise ham yad grfte-->train score-->test_score (pishbini)-->paeene


#model haye ma yekseri hyeprparameter drn
#bayad bnri bbini 


from sklearn.neighbors import KNeighborsRegressor

#----------
#=================================
#=================================
#dt, rf, mlp
#0 42 120


#Decision treee
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)
###6 t aro test

#model 
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(max_depth=3,random_state=0)
#hyperparameetr-->p[ichidegio
#max_depth
#min_sample_split
#max_leaf


#train
model.fit(x_train,y_train)

#validation
test_score=model.score(x_test,y_test)
print(test_score) #0.8333333333333334

#predict
new=np.array([[15,3]])
predshode=model.predict(new)
print(predshode)

#=================
#=================
#=================
#=================
#decdision tree -->random
#max , min ,
#in derakhte
#dah abr run konm -->yekdomesh behtar bshe
#derakhte bartarin kodome?

#Random forest jangale tasadofi

#bia data hamo
#
#DRandom forest
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)
###6 t aro test

#model 
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=100,max_depth=7)
#n_estimator
#bishtare -->behtar
#1000 --.computational cost 
#100 ta derakht
#har derakht --> mhdood --> max_depth

#train
model.fit(x_train,y_train)

#validation
test_score=model.score(x_test,y_test)
print(test_score) #0.8333333333333334


#predict
new=np.array([[15,3]])
predshode=model.predict(new)
print(predshode)

'''

from sklearn import datasets

#https://scikit-learn.org/stable/datasets.html#datasets

data1=datasets.load_iris()
data3=datasets.load_breast_cancer()
data4=datasets.load_linnerud()
data5=datasets.load_wine()
data6=datasets.load_diabetes()
data7=datasets.fetch_california_housing()

'''


#================================
#iris()
from sklearn.datasets import load_iris

dadeh=load_iris()

#yek model dashte bashim
#ye gol didim
#fght 4 ta vzihegisho , tool o arze sepal patal
#behemon 0 1 2 ide--> bema mige
#golemon kodomk no hast

#frghesh ba ghabli
#clasification
#2 ta vizhegi nadare
# 4 ta vizhegi dr

#0.import
#0.1.cleaning

#1.x o y
x=dadeh.data
y=dadeh.target

import matplotlib.pyplot as plt
plt.scatter(x,y)

#vzihegi haro dar barabare ham mikeshi

plt.scatter(x[:,0],x[:,1],c=y)



#gol haye iris

#DT======================================
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)


#model 
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=20,max_depth=7)
#n_estimator
#bishtare -->behtar
#1000 --.computational cost 
#100 ta derakht
#har derakht --> mhdood --> max_depth

#train
model.fit(x_train,y_train)

#validation
test_score=model.score(x_test,y_test)
print(test_score) #0.8333333333333334


#predict
new=np.array([[5,3.4,1.5,0.19]])
predshode=model.predict(new)
print(predshode)



#SVM
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)
###6 t aro test

#model 
#svc --> support vector classifier
from sklearn.svm import SVC
model=SVC(C=20,kernel='rbf')
#linear-->
#b tavani ---> poly 
# pichide --> rbf


#train
model.fit(x_train,y_train)

#validation
test_score=model.score(x_test,y_test)
print(test_score) #0.8333333333333334
#1.0

#predict
new=np.array([[5,3.4,1.5,0.19]])
predshode=model.predict(new)
print(predshode) #[0]

#-----------
from sklearn.datasets import load_breast_cancer
dadeh=load_breast_cancer()

x=dadeh.data
y=dadeh.target

print(dadeh.feature_names)

print(dadeh.target_names)
#malignant ---> 0 badkhim
#benign --> 1 khoshkhim


#500 ta bimar darim
#ye mdoel besazim

#badan taraf biad oon 30 ta vzihegio bde
#in baar ma hesaab mikone k taraf sarataesh khosh khime ya badkhime
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)
#114 -->test biamri k nadide

#model 
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=20,max_depth=7)
#n_estimator
#bishtare -->behtar
#1000 --.computational cost 
#100 ta derakht
#har derakht --> mhdood --> max_depth
model=SVC(C=100,kernel='rbf')


#train
model.fit(x_train,y_train)

#validation
test_score=model.score(x_test,y_test)
print(test_score) 
#RF=  0.956140350877193
#SVC= 0.9736842105263158
#SVC ba c=100 --> 0.9824561403508771

#bimar oon 309 ta vzihegisho bzare---> mige 0 e (badkhime) ya khosh khime
#ba cheghadr deghat--->95%

score_list=[]
for i in range(1,300):
    model=SVC(C=i,kernel='rbf')
    model.fit(x_train,y_train)
    test_score=model.score(x_test,y_test)
    score_list.append(test_score)
#100 ta mdoel misaze #SVC --> c hash frgh mikone



xx=np.arange(1, 300)
plt.plot(xx,score_list)
plt.ylabel('accuracy')
plt.xlabel('C for svc')

#================================================
#================================================
#================================================
#================================================
#================================================
#================================================
#================================================
#================================================
#--------REVIEW
#tamame masalee jahano-->input / output konid
#outpute peyvaste -->regression
#gosaste -->classification


#model *mantegh ha hamone

#REGRESSOR 
LinearRegression(), KNeighborsRegressor()
DecisionTreeRegressor() , RandomForestRegressor()
SVR()
#Classifiction
KNeighborsClassifier()
DecisionTreeClassifier()  , RandomForestClassifier()
SVC()

#mantegh hamoone
#framwork hamone
#x , y
#slit train test
#model $
#fit
#score (validation)
#predict
#plot

#$--> mdoel haro inja mizarim -->ahrkdom ye manteghi dre


#***dast 

#-------NOTE---------------
#***
from sklearn.svm import SVR
x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])

plt.scatter(x,y)

#train test
#2 ta ro random -->mziashtim test k dar akahr valid konim (test_score)

#momkene in randomaro shansi bge--> reliable 
#momeken masalan az tahe range vardashte bashe

#KFOLD
#score-->gahbeel etemad tar msihe-->kazeb nis
#too train test--> test_size= 0.20 , shufle random state

from sklearn.model_selection import KFold
fold=KFold(n_splits=5,shuffle=True,random_state=0)




#1-x o y
x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])

#2- bejaye train test --> kfiold
fold=KFold(n_splits=5,shuffle=True,random_state=0)

#3-model **harchi mikhay bzar *regression, calssificato
model=SVR(C=10,kernel='linear')

#4- fit o score baham anjam 
from sklearn.model_selection import cross_val_score
score= cross_val_score(model,x,y,cv=fold,scoring='neg_mean_absolute_percentage_error')



#MAE --> ekgtelafe motlageh pishbinio vagehi
#neg_mean_absolute_error

#MSE
#neg_mean_squared_error

#RMSE
#neg_root_mean_squared_error

#MAPE
#neg_mean_absolute_percentage_error


#scoring:
#https://scikit-learn.org/stable/modules/model_evaluation.html
    
    
    
print(score)
#[-0.04077412 -0.07348319 -0.08016102 -0.01716049 -0.01084507]


#5 ta laptab
final_score=np.mean(score)
print(final_score) #-0.04448477794402932

#train_test_split -----> 
#CROSS_VALIDATION


#ye moshkel hast---->hyperparametra nafahmidm
# mdoelarma fhmidm
#framworke jadiam fahmidm
#hyperaparameter

#----------------
#LR , KNN, DT , RF, SVC --->classification code zdm

#datamone
#dama o estehkame 3d printing-->regression

x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])



##LR , KNN, DT , RF, SVR -->mdoel ha regression (hyperparametram khdoeton dasti entkehab konid)
#cross validation score barye har model--> behtrin mdoel kodome






'''
QUIZZZZZZZZ*****************************8

DATA HARO DARID
az 5 ta model begid kodom model behtare 
behem Cross validation score elam konid.
word --> LR --> 2.5 % 


behtrin model ro fhmdiid kodome
berid roo kole data fit bdid va rasm konid 


ai.2024.pilehvar@gmail.com

'''












