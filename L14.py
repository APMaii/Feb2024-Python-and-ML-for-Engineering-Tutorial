
"""
In The Name Of GOD
Created on Sun Apr 14 15:25:30 2024

@author: ai.2024.pilehvar@gmail.com

L14


"""
#Review-----------------------

#tamame masaele jahan ro be vorodi khoroji tabdil konim
#I/O ---> input / output

#mesale sade az
#shoam 3d printing ya harchizi dar nazar bgirid
#Process parameetr -->daste ma hast-->ma mitonim taghir bdim directly (mostaghim)
#quality parameter --> moheme -->arzyabi moafaghita 

#dama --> quality -->estehkam
#x--> dama    y-->estehkam
#midonimd ar jahane vageh ei yek rabete ee beyne
#DAMA VA ESTEHKAM HAST
import matplotlib.pyplot as plt
y=2*x+5
plt.scatter(x,y)
plt.xlabel('temperature')
plt.ylabel('Estehkam')

#GHADIM-----> REGRESSION SADE
#brim too azmayehsgah --> hey damahaye mokhtalef bgirim
#hey y ro dare biarim
import numpy as np
x=np.array([200,300,400,500,600,700,800,900])
y=np.array([300,421,521,590,710,810,890,920])
plt.scatter(x,y)
plt.xlabel('temperature')
plt.ylabel('Estehkam')
plt.show()

'''
dama sorat
0     0
0   50
0   100
50  0
50  50 
50  100
100 0
100 50
100 100



'''
#soalat--> agar dama 250 -->estehkam?
#agar dama 950 -->estehkam chn mishe

#chiakr konim-->too azmayeshgah done done temp 
#zaman bar (ghesmate 1), hazine bar (ghesmnate 2)
#ghesmate 3 (gheyre gahbeel daastres)

#Regresssion (sade)-->rabeteye beyne x o y ro dar miare-->khat
#fek kon ine:
xx=np.linspace(200,900,1000)
yy=xx+100
plt.scatter(xx,yy,s=1)

#hala rahat harchi khasti
#masalan 350 mziri too formol y = x+ 100 --> 135
#tmaom


#regression -->az yek raveshi raft az rooye oon dade ha
#rabete ro darovord
#BOx -->vorodi midi behesh khoroji bht mide

#....
#1-az data yad bgire (yad grrft)-->raveshe hadeaghal morabat
#2-mantegh kasb kone (formoel ro dar miare)
#3-shoma vorodi bhsh bdi --> mziare to formol khoroji mide


#moshkel chie -->nmidonim cheghad in khate ke ma darovordim
#ba oon khate k dar jahane vaghe ei vojod dre chgdh anzdiek?

#bayad brim do se ta tewst bgirim az azmayehsgah baiym



#machine learning
#regression sade --> ML regression
#triN TEST

#MACHINE LEANRING REGRESSION---------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#0.0.-data improt ( dasti , csv excell , downlaod, import)
#0.1.-cleaning (pandas emthod dropna, duplicated wrong format)
#1-datato --> x o y  [jadvale] input , output
#**agar x et ye soton bod--> reshape estefade
x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])

#2-train test split --> yek bakhsi too train , test
from sklearn.model_selection import train_test_split
#in yek tabast k mige x o y ro bede manm man behet
#4ta adad midam --> 4 ta list ro mirizi to zarf hay emotefavet
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)


#3-model selection-->modeleot entkerhab mikone
#ML LR -->Macxhine elarnin linear regression
from sklearn.linear_model import LinearRegression
model=LinearRegression() #tooye parantez yekseri setting has mitoni tagir bdi k rooye yadgirish tasir dre
#KNN , DT , RF , G, SVR , MLP
#baladi agha
#from sklearn.tree import DecisionTreeRegressor
#model=DecisionTreeRegressor()


#4-fit mikoni roye train data--> oon train dataset
#modelto roosh fit mikoni -->train midi-->
#yani mdoelet ba raveshe khdoesh (LS)-->rabetaro dar miare
model.fit(x_train,y_train)


#5-evaluation , validation --> sanjesh koni modeleto
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



#6-predict --> box behesh vorodi bdi khoroji bgiri
new=np.array([450]).reshape(-1,1)
new_pred=model.predict(new)
print(' baraye  damaye 450 , estehkam pishbini mishavad : ',new_pred)
#549.525


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


#hameye mdoel ha
#.fit() --. ba ravehse kahs ekhdoesh train , yad migire --> A, B
#.predict() ---> mzioare tooye y=Ax+B , -=->y box


#====================================================
#====================================================
#--------
#machine learnin
#1-Training ---> train_dataset
#2-Prediction --->test_dataset

#data--->
plt.scatter(x,y)


#train test
plt.scatter(x_train,y_train,label='train')
plt.scatter(x_test,y_test,label='test')
plt.xlabel('Temp')
plt.ylabel('Estehkam')
plt.legend()
plt.grid()
plt.show()

#aspect
# yadgiriiish cheshekli bode--->train score
# pishbinish hala chtor--->test score

#modele ma bayad az aval 
#1-train
plt.scatter(x_train,y_train,label='train')
xx=np.linspace(200,900,10000).reshape(-1,1)
yy=model.predict(xx)
plt.scatter(xx,yy,s=1,label='ML Predicted')
plt.xlabel('Temp')
plt.ylabel('Estehkam')
plt.legend()
plt.grid()
plt.show()




plt.scatter(x_test,y_test,label='test')
xx=np.linspace(200,900,10000).reshape(-1,1)
yy=model.predict(xx)
plt.scatter(xx,yy,s=1,label='ML Predicted')
plt.xlabel('Temp')
plt.ylabel('Estehkam')
plt.legend()
plt.grid()
plt.show()

#
#test_score---> ghodrate pihsbini cheghadre 


from sklearn.metrics import mean_absolute_percentage_error
#y_train
#y_test

#1--->aval bbinam khob yad grfte ya na
y_pred_train= model.predict(x_train)
train_score=mean_absolute_percentage_error(y_train,y_pred_train)
#khate ma ba train ha cheghadr ekhtelaf dre--->chgdh khoob amozwesh dide
print(train_score) #0.03647472454999043


y_pred_test=model.predict(x_test)
test_score=mean_absolute_percentage_error(y_test, y_pred_test)
print(test_score) #0.02971921644526543





#------ validation aydet abshe
#ghablan fght test score ro dar nazar miugrdftim
#ama dorostesh

#train score---> cheghad khoob yad grfter
#test score---> cheghad khoob pishbini mikone


#trade-off

#overfitting
#kheyli kheyli ghavi yad bgire -->  overfitting
#yani hata noise haye dakhele data ro yad grfte
#bias (taasob dare)-->geenral--> nmitone pishbini khob kone
#train_score paeen (khataye kami drim) -->overfitting-->monjar mishe k test_score ziad (khate ziade)


#underfitting


#DT --Model
y_pred_train=model.predict(x_train)
train_score=mean_absolute_percentage_error(y_train,y_pred_train)
print(train_score) #0.0 --> haamro awli yad grfte -->overftiiing

y_pred_test=model.predict(x_test)
test_score=mean_absolute_percentage_error(y_test,y_pred_test)
print(test_score) #0.20543385824462626

#train score ag kh kam bashe (kh khob yad bgire)
#rafte noise haham yad grfte --> overfitting
#test_score bala (bad bashe)-=-->pishbini khob nabashe
#underfitting
#train-score -->bala -->bad yad grfte bnashe
#bad yad bgire--> test_score miad paeen 



#dar valdiation-->fght test_score ro nasanj
#train_)score besanj
#trrain_score 

#test_score bad she--> moehme k bdoni
#aya yad grfte nashdoe dalil
#

#================
#peyvaste--> 32378 
#gosaste--> chantaee 2 tae , tedade afrade 44.5
#444.23
#===========
#-----> input/putput
#model -->fit , predict

#output--> PEYVASTE --> 345 , 543 (estehkam) --->REGRESSION MODEL --> Regressor
#output--->gosaste ---> 2 ta, 3 ta -->daste bandi (classification MODEL) -->classifier
#SUPERVISED LEARNING

#mesal ha
#daste bandi sago grobe
#saratn , tashkhis --> 0 1 
#detection ,
#quality --> 0 1 
#daste gol --> 1 2 3

#------
#LR  Linear Regresssion
#KNN K nearest neighbor
#DT Decision tree
#RF random forest
#SVM support evctor machine
#MLP multi layer perceptron

#ham regresssion , classification
#arz 
#toool
#Green_TO
#Yellow_To

#8 ta derakhto arzo toolesho dr ovordm
#barchasb zadam (label)--> gt , yt


#HADAF
#BOX 
#behesh tool o arze derakhtaye in kochamon
#behem bege green to , yelow to
#daste bandi=-->jozve kodom dastas
#yad bgrie aval--.data

#x ---> tool arz 
#y --->

x=np.array([[1,10],[1,12],[1.2,13],[1.5,14],[3,20],
           [3.2,40],[4,32],[3.5,38]])
y=np.array([0,0,0,0,1,1,1,1]).reshape(-1,1)

y=np.array([['G','G','G','G','Y','Y','Y','Y']]).reshape(-1,1)

xx=pd.DataFrame(x,columns=['ARZ','TOOL'])

#vzihegi , soton haro dar barabare ham
#input ha vorodi a

plt.scatter(xx['ARZ'],xx['TOOL'],c=y)
plt.xlabel('ARZ')
plt.ylabel('TOOL')
X=np.linspace(1,4,100)
YY=-10*X+40
plt.scatter(X,YY)

#chanta doros gofte
#az test a k behemk dadei
#chanta doros goftm



#LR --> linear regression-->regresssion 
#hezarat khat msiakht a , b
#midid oon khat ch fasele ee drn --> ekhtelaf --.cost function
#cost function-->lamtarin -->nazdik tarin bod
#A o B --> LS
#fit beshe rooye noghat

#logistic regression--> Classification
#A o B hey hey
#va maid 
#khate threshold (astane) jhdoa kone
#joda kone --> daste haro


#model haye dg 
#bejaye a o b #az ravesh haye dg mian

#darnahayt mdoel ha-------------------------

#hame ye masaele jahan--> iNPUT/OTPUT

#output
#peyvaste ---> 3234,32.43--> regressor
#gosaste , chanta 1 ta 2 ta --> classification


#regressor --> fit mikonan
#classifier --> khate vaset mizaran

#doros fit krde?
#doros jdoa krde


#train_test --> rooyte train ha fit konim , test haro chijori pishbini mikone
#TRAIN_TEST-->rooye train joda mikone , test haro mdian bbinan dforos dast ebandish (pishbini)


#score-->ekhtelafe pishbini
#score---> chanta doros


#------------------------
#IRIS.data













