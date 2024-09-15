
'''
In The Name Of GOD

Created on Sun Apr 21 15:18:53 2024

@author: ai.2024.pilehvar@gmail.com

L16 ( payani)

'''
#ARTIFICIAL INTELLIGENCE ---. ML (MACHINE LEARNING 70-80 %)
#tamame masale haye jahan ro --> I/O input/ output

#-------SUPERVISED (tahte nezarat) (regression , classification)

#framework----------
#import lib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.svm import SVR
#-------0--Import data
#cleaning
#1-x o y
x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])

from sklearn.model_selection import KFold
#2- bejaye train test --> kfiold
fold=KFold(n_splits=5,shuffle=True,random_state=0)

#3-model **harchi mikhay bzar *regression, calssificato
#LR , KNN , DT , RF, SVR , MLP
#MODEL regressor    model classifier
#setting dare
model=SVR(C=10,kernel='linear')

#4- fit o score baham anjam 
from sklearn.model_selection import cross_val_score
score= cross_val_score(model,x,y,cv=fold,scoring='neg_mean_absolute_percentage_error')
#https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter

#neg_mean_absolute_error --->ekhtelafe motlagh
#neg_mean_squared_erro
#neg_root_mean_squared_error
#neg_mean_absolute_percentage_error --->darsad

#----------------------------
#frameworke asli---------------------
#soal--.agha ma az koja bedonim ch setting (hyperaparemetr)
#entekhab konim baraye mdoelemon?
#ye range bayad entekhab sbeh baarayu ehyperparameter
#bre doone doone hesab kone

x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])
fold=KFold(n_splits=5,shuffle=True,random_state=0)
score_list=[]

for i in range(1,20):
    model=SVR(C=i,kernel='linear')
    score= cross_val_score(model,x,y,cv=fold,scoring='neg_mean_absolute_percentage_error')
    score_list.append(score)


#miangiensho bde
x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])
fold=KFold(n_splits=5,shuffle=True,random_state=0)
score_list=[]

for i in range(1,1000,100):
    model=SVR(C=i,kernel='linear')
    score= cross_val_score(model,x,y,cv=fold,scoring='neg_mean_absolute_percentage_error')
    score_list.append(np.mean(score))

#search --> grid grid --> best hyperparameter 
#bejay einakra -->sklearn man ye tabe vasat skahtam
#gridsearchCV


#==============================framwork
#ajdide va aslie ine
#train test ----> cros validation--->gridsearch CV
#import data
#cleaning
#x o y
x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])
#train test-->kfold
fold=KFold(n_splits=5,shuffle=True,random_state=0)
#model-->har modeli *8setting neminevisi
model=SVR()
myparams={ 'C' : [1,100,200,300,400,500] }
#
from sklearn.model_selection import GridSearchCV

gs=GridSearchCV(model,param_grid=myparams,cv=fold,scoring='neg_mean_absolute_percentage_error')

#hich etefaghi nmiofte
gs.fit(x,y)

#hala chiakra mitoni koni
zarf_result = gs.cv_results_

gs.best_params_ #{'C': 500}
#beyen c haewe k dadi --> C:500 bhtrin bood
#agar ba in C ma bgirimn --> scoremon msihe in paenie

gs.best_score_  #Out[33]: -0.0712971479359135


#=======================
x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])
fold=KFold(n_splits=5,shuffle=True,random_state=0)
model=SVR(kernel='linear')
myparams={ 'C' : [1,100,200,300,400,500] }
gs=GridSearchCV(model,param_grid=myparams,cv=fold,scoring='neg_mean_absolute_percentage_error')

gs.fit(x,y)

zarf_result = gs.cv_results_

gs.best_params_ #Out[37]: {'C': 300}
gs.best_score_  # -0.044484777934885034

#=========================fght ye parameter na
x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])
fold=KFold(n_splits=5,shuffle=True,random_state=0)
model=SVR()
myparams={ 'kernel':['linear','poly','rbf'],
          'C' : [1,100,200,300,400,500] }
gs=GridSearchCV(model,param_grid=myparams,cv=fold,scoring='neg_mean_absolute_percentage_error')

gs.fit(x,y)

zarf_result = gs.cv_results_

gs.best_params_ #{'C': 300, 'kernel': 'linear'}
gs.best_score_  #  -0.044484777934885034

#18 hbar ba cO KERNELA motefavet midaze
#va bhtbehatrin resulto mide 
#cross valodiation sscore


#===================
#notes:
#preprocessing - Feature engineering
#x et hamishe khob nis k mostaghim bre vase train
#model ha mese svr , mlp -->hasasan --.dataharo kochikeshon

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import Normalizer

#rahat tar train (zaman kotah), eghat mnire bala


scaler=MinMaxScaler()
scaler.fit(x)
new_x= scaler.transform(x)


#baghie raho bejaye inek rooey x kare kon
#shoam yechid ari bname new_x

from sklearn.preprocessing import PolynomialFeatures
#rabete he khati nis
#SVR , MLP --> naizi b in ndre -->ravabete gheyre khati ro dar biare
#DT , KNN , LR
poly=PolynomialFeatures(degree=3)
poly.fit(x)
new_x=poly.transform(x)
#daraje balatar


#selectbest ---> 20 fdeature vorodi 20 soton 
#best 
#masalan df

df.corr()

#aya vroodi bar khoroji tasir gozar hast ya nis
#onaee k hasto to ok
#onae k nsito hazf mikoni



#===========================================
#MLP-------

x=np.array([200,300,400,500,600,700,800,900]).reshape(-1,1)
y=np.array([300,421,521,590,710,810,890,920])
fold=KFold(n_splits=5,shuffle=True,random_state=0)
from sklearn.neural_network import MLPRegressor
#modele dt, rf, mlp 
#hidden_layer_size=( 10,20,10)
model=MLPRegressor(random_state=0)
myparams={ 'hidden_layer_sizes': [ (10,) ,(20,) , (10,10) , (20,20)] ,
          'solver':  [ 'adam','sgd'  ],
          'alpha':[0.0001,0.001,0.01]}
gs=GridSearchCV(model,param_grid=myparams,cv=fold,scoring='neg_mean_absolute_percentage_error')

gs.fit(x,y)

zarf_result = gs.cv_results_

gs.best_params_ # {'alpha': 0.0001, 'hidden_layer_sizes': (20, 20), 'solver': 'adam'}
gs.best_score_  #Out[58]: -0.08582440627199514


# hlz 10 , solver adam alpah 0.0001
# hlz 10 , solver adam alpah 0.001
#hlz 10 , solver adam alpah 0.01
# hlz 10 , solver sgd alpah 0.0001
# hlz 10 , solver sgd alpah 0.001
#hlz 10 , solver sgd alpah 0.01

#/// 6 tash hlz (20)


#============================
#dar akhar vaaghty valdiate kardi
#gs dar kole data

gs.predict(np.array([550]).reshape(-1,1))
#array([626.15813284])

#---------adad --->tasvir
from sklearn.datasets import load_digits
data=load_digits()
x=data.data
y=data.target
fold=KFold(n_splits=5,shuffle=True,random_state=0)

from sklearn.neural_network import MLPClassifier
model=MLPClassifier(random_state=0)
myparams={ 'hidden_layer_sizes': [  (20,20),(100,)] ,
          'solver':  [ 'adam','sgd'  ],
          'alpha':[0.0001,0.001]}
gs=GridSearchCV(model,param_grid=myparams,cv=fold)

gs.fit(x,y)

gs.best_score_ #0.9744026617146394

new=x[14,:]
pred=gs.predict(new.reshape(1,-1))
print(pred) #[4]

#orodi ye ax 
#input / output

#khoroji---> (ye adade)
#Model rabeteye beyne ax va adad ro bfhme
#ax bndi -->  kodom tashkhis bde
#==============================
#3D printing
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error


from  sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import PolynomialFeatures


from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.ensemble import GradientBoostingRegressor


from sklearn.pipeline import Pipeline


from sklearn.model_selection import KFold


from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict

f_path='final data.xlsx'
data=pd.read_excel(f_path)

data.info()
#null nist
#float

#removing columns and rows
data.drop(columns=data.columns[0],inplace=True)
#data.columns
data.drop(columns=data.columns[0],inplace=True)
#data.columns
data.drop(columns=data.columns[0],inplace=True)
a=data.loc[4]
data=data.set_axis(a, axis="columns")



data.drop(index=0,inplace=True)
data.drop(index=1,inplace=True)
data.drop(index=2,inplace=True)
data.drop(index=3,inplace=True)
data.drop(index=4,inplace=True)


data.drop(index=15,inplace=True)
data.drop(index=16,inplace=True)
data.drop(index=17,inplace=True)

data.reset_index(inplace=True,drop=True)

data.columns

data['Nozzle size']=pd.to_numeric(data['Nozzle size'])
data['Infill Percentage']=pd.to_numeric(data['Infill Percentage'])
data['Raster Angle']=pd.to_numeric(data['Raster Angle'])
data['Pore size (mm2)']=pd.to_numeric(data['Pore size (mm2)'])
data['porosity(%)']=pd.to_numeric(data['porosity(%)'])
data['Modulus(MPa)']=pd.to_numeric(data['Modulus(MPa)'])
data['Strength(MPa)']=pd.to_numeric(data['Strength(MPa)'])
data['Specific Strength(MPa/g)']=pd.to_numeric(data['Specific Strength(MPa/g)'])

data['NEW PORESIZE']=pd.to_numeric(data['NEW PORESIZE'])
data['SHAPE FACTOR']=pd.to_numeric(data['SHAPE FACTOR'])


#cleansing
'''
import seaborn as sns

plt.figure(figsize=(10, 6))  # Set the figure size (width: 10 inches, height: 6 inches)
plt.rcParams["figure.dpi"] = 600 
plt.rcParams['font.family']='Arial'

correlation = data.corr()  

sns.heatmap(correlation,cmap="coolwarm",annot=True)
plt.tick_params(labelsize=16,pad=12)
'''



#x  o y
x=pd.concat([data['Nozzle size'],data['Infill Percentage'],data['Raster Angle']],axis=1)
y=data['porosity(%)']

#kfold
fold=KFold(n_splits=6,shuffle=True,random_state=42)

#model
model = MLPRegressor(random_state=42,max_iter=10000)
pipe_model = Pipeline([('poly',PolynomialFeatures()),("scaler", StandardScaler()), ("model", model)])

#yani pipe model -->hamon modele + yeseri preprocesing
'''
myparams={ 'hidden_layer_sizes': [  (20,20),(100,)] ,
          'solver':  [ 'adam','sgd'  ],
          'alpha':[0.0001,0.001]}

'''
myparams={ 'model__hidden_layer_sizes': [  (20,20),(100,)] ,
          'model__solver':  [ 'adam','sgd'  ],
          'model__alpha':[0.0001,0.001]}


gs=GridSearchCV(pipe_model,param_grid=myparams,cv=fold,scoring='neg_mean_absolute_percentage_error')

gs.fit(x,y)

gs.best_score_ # -0.14657143604815914

#85 % --> shoma behem ag in settingo bdi
#man migamn onchizi k ba 3d printinget mitroni chap koni
#darsad takhalkholesh cheghadre --> +- 15 


#dalilesh-------------------------------------------
x=pd.concat([data['Nozzle size'],data['Infill Percentage'],data['Raster Angle']],axis=1)
y=data['porosity(%)']

#kfold
fold=KFold(n_splits=6,shuffle=True,random_state=42)

#model
model = MLPRegressor(random_state=42,max_iter=10000)
pipe_model = Pipeline([('poly',PolynomialFeatures()),("scaler", StandardScaler()), ("model", model)])

#yani pipe model -->hamon modele + yeseri preprocesing
'''
myparams={ 'hidden_layer_sizes': [  (20,20),(100,)] ,
          'solver':  [ 'adam','sgd'  ],
          'alpha':[0.0001,0.001]}

'''
myparams={ 'poly__degree':[2,3],
          'scaler':[ StandardScaler() ,MinMaxScaler(),RobustScaler()],
    'model__hidden_layer_sizes': [  (20,20),(100,)] ,
          'model__solver':  [ 'adam','sgd'  ],
          'model__alpha':[0.0001,0.001]}


gs=GridSearchCV(pipe_model,param_grid=myparams,cv=fold,scoring='neg_mean_absolute_percentage_error')

gs.fit(x,y)

gs.best_score_ # -0.07292670673415098 ---> 93%
#conclusion : porosity of PLA FDM-printed was predicted with MAPE error of 7%


def generate_bumpy():
    a1_values = np.arange(200,600, 10)
    a2_values = np.arange(10,100, 1)
    a3_values = np.array([60,90,120])

    a3, a2, a1 = np.meshgrid(a3_values, a2_values, a1_values, indexing='ij')

    result = np.column_stack((a1.flatten(), a2.flatten(), a3.flatten()))

    return result

input_space = generate_bumpy()


#fir kardm gs
#10 8000
l_yp=gs.predict(input_space)
# 10 800 --> setting zbaram brm azmayeshgfah
#pishbini krd

yp=pd.Series(l_yp)
yp.name='p'
data=pd.concat([pd.DataFrame(input_space),pd.Series(yp)],axis=1)


d=data['p']
angle='60'
if angle=='60':
    xx1=input_space[0:3599,0]
    xx2=input_space[0:3599,1]
    yy3=d[0:3599]
#vase zavie haye 60 to joda krdm

fig = plt.figure(figsize=(12,10))
norm = plt.Normalize(yy3.min(), yy3.max())

ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(xx2,xx1,yy3, c=yy3, cmap='viridis', marker='o', norm=norm)

# Set labels
ax.set_xlabel('Infill Percentage')
ax.set_ylabel('Nozzle Size')
ax.set_zlabel(f'porosity')
# Add a colorbar
cbar = fig.colorbar(scatter, ax=ax, pad=0.1, shrink=0.8)
cbar.set_label(f'porosity')

# Show the plot
plt.show()




angle='90'
if angle=='90':
    xx1=input_space[3600:7199,0]
    xx2=input_space[3600:7199,1]
    yy3=d[3600:7199]
    
fig = plt.figure(figsize=(12,10))
norm = plt.Normalize(yy3.min(), yy3.max())

ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(xx2,xx1,yy3, c=yy3, cmap='viridis', marker='o', norm=norm)

# Set labels
ax.set_xlabel('Infill Percentage')
ax.set_ylabel('Nozzle Size')
ax.set_zlabel(f'porosity')
# Add a colorbar
cbar = fig.colorbar(scatter, ax=ax, pad=0.1, shrink=0.8)
cbar.set_label(f'porosity')

# Show the plot
plt.show()


#unsupervised-------------------
#classfiication (clustering)
#msoahkahs akrdim -->label -->barchasb zadim
#y---> saratan darad nadard

#isekroa, ...

#greeen , yellow

#defect 

#0 1, 2 3

# sag gorbe

#Khorojimon nvshte shode

#Big-data
#BESHINI DONE DONE jolo datahat benevisi label bzni
#y ro msohakahs koni

#y nadaran
#fght x daran


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names


#momkene 100000 ta bashe
#man nasheste basham bnvism kodom kodom nis hat
#y nadahste bashe-->bnarchasb nadahste -->label nabahste -->supervsied nadahste
#unsupervised

#daste bandi -->clsutering
#hatm,anm anjam bdid



import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Generate synthetic data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Plot the data
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title('Original Data')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

#fght x darim
#sago gorbas 2 ta
#4 tae
#valu abrchasb nzdim-->dat ha ziad 

from sklearn.cluster import KMeans

model = KMeans(n_clusters=4)
model.fit(X)

# Getting cluster centers and labels
centers = model.cluster_centers_
labels = model.labels_

# Visualize the clustered data
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5)
plt.title('Clustered Data')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

# y iu nist
#as crabete x o y ro dr nmaire
#mire too dele x , rabet ee dar maire -->ekhtelafa , shabahata misanje

#kemans-0--> k e to mdioni


#pichide tare ---> xpattern 
#k ro midan --> ehtemalan 3 4



#semi-superviseddd
#reinforcmeent 




#PROJECT-------------------------

import pandas as pd
import numpy as np


data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)


data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]



#data---> X
#target---> y


#506 ta khonhe has
#ha rkhoen yekseri moalwefatesho varadashtan
#metrazhesh , darsade jormo jenayat

#12 ta maolefasho abraye 506 tas khone
#gheymat b herzar dollar


#----------------------------
#A3_PROJECT_NAME_

#yek file e word 
#pythn code


#tgoye file e wordet 
#english, farsi

#introduction
#boston data chie va chi nist
#yek tozihe 2 khati az mdoel ha
#yek tozih az inke framwork ()

#result and sdiscussion 
# 5 LR, KNN, DT , RF ,SVR , MLP
#gridsearchcv mizanid
#jadval
#MAPE --> 5 mdoel 
#MAE----> 5 model

#va natiej begirid kodom yek az model ha bartarine
# rasm konid pishbinio

#ai.2024.pilehvar@gamil.com


#=================================================



















