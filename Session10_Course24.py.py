
"""
Created on Sun Mar 17 14:31:45 2024

@author: apm


L10

"""
#ma dar python koli ketabkhoen darim
#har ketabkhone koli adade sabet, function , class(chanta function)
#ke banabar applciatenesh ma miaym CALL esh mikonim va use

#-----------
#math
#statistics
#random
#4 ta ketabkhone
#numpy--->mohasebat
#matplotlib---> rasm
#pandas--->kar ba data 
#sk learn ---> Machine learning

#moghadame
#tensorflow 
#keras

'''
==============================
'''
#nahveye download va installe ketabkhone
#pip install libname --> ba search dar google + pip
#CMD --> environment --> copy paste --> enter 

'''
#3 tarigheye import kardane

import libname

import libname as mokhafaf

from libname import felan_function



-----mohmtrin importa
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

**ketabkhoanro ro avale safeye code import konid
#yekbar import kardan kafiee


#call-->tarigehye estefase

esmesho seda miziani, ye dot mizani yani
boro dakhelesh, oon functioni k mikhyaop mikeshi biron

libname.adad

libname.tabe()

libname.cllss.tabe()

'''

import numpy as np
#imort kon ketabkhoenye numpy ro esmesho bezar np ---> harj agoftam np bedoni manzooram chie

#listt
#numpy -----> array --->
#man miam 50 barabar sarti tar va n dimention
a=np.array([1,2,3,4])
#asssign ,. access--> change , iteration , method

#dakheley eyd --> Moroor beshe
#https://numpy.org/doc/stable/user/absolute_beginners.html
#hamishe be bode numpy arrayt deghat konid
#dar do bodi --> RADIF , SOTON [toye dastresi, method]

#-----Ketabkhoneyematplotlib
import matplotlib.pyplot as plt
#in ketabkhone ro import kon esmesho bzar plt, ke harja plt sedsh zadma bfhmi manzoram chie

#sade tarin mesal --> review jalase
#ma do ta noght edashtim
#list, set , touple, numpy array , dataframe
#**vase hame chi mitoni rasm koni
#pas ma choon array darim dg kamtar az list estefade mikonim
#**tahe codet hamishe plt.show() bezan

#(0,0)  (6,100) do ta noghte

x=np.array([0,6])
y=np.array([0,100])
#fghht y ---> ejbarie
#baghie--> tanzimat

#fght line----
plt.plot(x,y)
plt.plot(y) #x ro 0 ....

#fght noghte---
plt.plot(x,y,'o') #fahghat noghte

#ham noghte ham line
plt.plot(x,y,marker='o')
plt.plot(x,y,marker='*')
plt.plot(x,y,marker='p')

#size noghte
plt.plot(x,y,marker='o',ms=20)

#dore point
plt.plot(x,y,marker='o',ms=20,mec='r')

#tooye point
plt.plot(x,y,marker='o',ms=20,mfc='r')

#ham dor ham too
plt.plot(x,y,marker='o',ms=20,mec='r',mfc='r')

#baragrd az aval
plt.plot(x,y)
#------LINE-------

#stylesho --> noghtechin
plt.plot(x,y,ls='-') #default
plt.plot(x,y,ls=':')
plt.plot(x,y,ls='--')
plt.plot(x,y,ls='-.')

#rangam avaz konm
plt.plot(x,y,color='r')
plt.plot(x,y,c='r')

#andaze khato
plt.plot(x,y,linewidth=20)


#vaghty az plot khjasti estefade koniii
#fght bayad x,y ro bdi behsesh baghiash optionale
#baraye tanzimate delete

x=np.array([0,6])
y=np.array([0,100])

plt.plot(x,y) #---> defaulte default
#khodet mikhay ezafe kon-->
plt.plot(x,y,marker='+',mec='r',ls='--',c='g')
plt.show()
#baz yechizi kame
#dar edamash
#1-plt.plot(...)
#2-taghirat -->title, grid, ...
#3-plt.show()



#1-
plt.plot(x,y,marker='+',mec='r',ls='--',c='g')
#2
plt.title('Nemoodaram')

#3-
plt.show()

#ya
#1-
plt.plot(x,y,marker='+',mec='r',ls='--',c='g')
#2
plt.title('Nemoodaram')
plt.xlabel('MOKHTASAT')
plt.ylabel('porosity')
#3-
plt.show()



'''
rasm koni
1-dakhele shekl (tanzimat)
2-Tanzimate koli ( birone shekl+dakheleshekl)
3-plt.show()
'''

a=[10,20,30,40]
#dictionary
#ye zarf mizari --> esm midi 
#toosho bpor
'''
hello : سلام
play : بازی

**list, set , touple , dictionary -->
#iterable 
#oomadan chanta joz ro dakheleshon ja bedan




tarife dictionary --> { }
'''
zarf= { 'hello' :'salam'  , 'bye':'khodahafez' }

a={ 'user1':'ali'  , 'user2':'hamid' ,'user3':'vahid'     }
#dota frghi ndre fght baraye ghabele khondan

a={ 'user1':'ali'  ,
   'user2':'hamid' ,
   'user3':'vahid'  }

#ma por bokonim
font={   'family' :      ,
         'color' :       ,
            'size' :      }


plt.plot(x,y,marker='+',mec='r',ls='--',c='g')
plt.title('Nemoodaram')
plt.xlabel('MOKHTASAT')
plt.ylabel('porosity')
plt.show()

#family --> kdom font , rangesh , sizesh

font1={   'family' : 'serif'     ,
         'color' :   'red'    ,
            'size' :   20   }


plt.plot(x,y,marker='+',mec='r',ls='--',c='g')
plt.title('Nemoodaram',fontdict=font1)
plt.xlabel('MOKHTASAT')
plt.ylabel('porosity')
plt.show()


#-----fonte done donashono b delkhah taghir bdi

font_title={   'family' : 'serif'     ,
         'color' :   'red'    ,
            'size' :   20   }


font_x={   'family' :  'serif'    ,
         'color' :   'blue'    ,
            'size' : 15     }

font_y={   'family' : 'serif'     ,
         'color' :   'black'    ,
            'size' : 15     }


plt.plot(x,y,marker='+',mec='r',ls='--',c='g')
plt.title('Nemoodaram',fontdict=font_title )
plt.xlabel('MOKHTASAT',fontdict=font_x)
plt.ylabel('porosity',fontdict=font_y)
plt.show()


#loc
plt.plot(x,y,marker='+',mec='r',ls='--',c='g')
plt.title('Nemoodaram',fontdict=font_title ,loc='left')
plt.xlabel('MOKHTASAT',fontdict=font_x)
plt.ylabel('porosity',fontdict=font_y)
plt.show()


plt.plot(x,y,marker='+',mec='r',ls='--',c='g')
plt.title('Nemoodaram',fontdict=font_title ,loc='left',pad=20)
plt.xlabel('MOKHTASAT',fontdict=font_x)
plt.ylabel('porosity',fontdict=font_y)
plt.show()

plt.plot(x,y,marker='+',mec='r',ls='--',c='g')
plt.title('Nemoodaram',fontdict=font_title ,loc='left',pad=40)
plt.xlabel('MOKHTASAT',fontdict=font_x)
plt.ylabel('porosity',fontdict=font_y)
plt.show()

#title, xlabnel, ylable--->< baraye label hamonan
#hamashon yek tabe an --> parantez --> taghir
#paranteze --> 1-neveshteye label 2- fontdict-=--> fonte oon neveshte
#yechizi dar ebename loc--> location ro mitonim, pad--> fasele oon neveshte nesbat b tasviremon

#ta alan gfotam-----> PLOT
plt.plot()



# 2 ta khat bekeshi......
x1=np.array([0,6])
y1=np.array([0,100])
x2=np.array([0,6])
y2=np.array([20,60])


plt.plot(x1,y1)
plt.plot(x2,y2)

plt.title('Nemoodaram',fontdict=font_title ,loc='left',pad=40)
plt.xlabel('MOKHTASAT',fontdict=font_x)
plt.ylabel('porosity',fontdict=font_y)
plt.show()




#miad avali ro default

#plt.plot()  ---> YES
#plt.scatter()
#plt.bar()
#plt.hist()
#plt.piechart()

#========================
x=np.array([0,6])
y=np.array([0,100])
plt.plot(x,y)


#bay default--> rasme noghte nabood--> line miomad keshid
#miomadim khodemon dastakri mikrdim tanzimato
plt.plot(x,y,'o')


#scatter---> point ro neshon bdid
x=np.array([0,5,10,15,20,25,30])
y=np.array([0,23,43,58,74,87,92])
plt.scatter(x,y) #by default 

#kolan ba point --> nogat saro kar drim
plt.scatter(x,y,color='r')

#bejaye inke begi hamaro gehrmexz kon
#biay begi agha ye nesbati midam b in ensbat ranga mizi kon
#baraye har noghte ye daraje gozashtam
cc=np.array([0,20,30,40,60,80,100])
#rangasho nesbat b 
#bejaye inke too color begam ahamro gehrmez kon
#miagm agha bar asase array CC --> shedati rangesh kon
#0 -100 --> 0 ch rangi bashe 100 ch rangi bashe
#cmap
plt.scatter(x,y,c=cc,cmap='cividis')

#nokte--> yerang koni--<> sehdati rnag koni

#1-dakhel 2-tanzimat 3-show

#---nemone
#1-
x=np.array([0,5,10,15,20,25,30])
y=np.array([0,23,43,58,74,87,92])
cc=np.array([0,20,30,40,60,80,100])
plt.scatter(x,y,c=cc,cmap='cividis')

#2-
plt.title('Nemoodare ziba')
plt.xlabel('darsade khoon')
plt.ylabel(' SHadabi index')
#colormap
plt.colorbar()
#3--------
plt.show


#size haram taghir bdim
plt.scatter(x,y)
#ssize e hame ziad shod
plt.scatter(x,y,s=100)
#done done ham
ss=np.array([100,20,20,20,20,100,100  ])
plt.scatter(x,y,s=ss)

#saye o roshanesh

plt.scatter(x,y)
#default --> alpha 1 e
#0 ta 1
plt.scatter(x,y,alpha=0.5)

plt.scatter(x,y,alpha=0.1)

#shedati ham koni
alphaa=np.array([1,0.2,0.2,0.2,0.2,0.2,1])
plt.scatter(x,y,alpha=alphaa)

#scatter----> plt.scatter(x,y)
#c --> color , s-->size noghat , alpha--> kamrangi porrangi
#ya hamaro mitonesi taghir bdi , y ay list, np atrif mikrdi va 
#done done noghateto customize

#----mesallll
#1-
x=np.array([0,5,10,15,20,25,30])
y=np.array([0,23,43,58,74,87,92])
cc=np.array([0,20,30,40,60,80,100])
ss=np.array([100,20,20,20,20,100,100  ])
alphaa=np.array([1,0.2,0.2,0.2,0.2,0.2,1])
plt.scatter(x,y,c=cc,s=ss,alpha=alphaa)

#2-
plt.title('Nemoodaram',fontdict=font_title ,loc='left',pad=40)
plt.xlabel('MOKHTASAT',fontdict=font_x)
plt.ylabel('porosity',fontdict=font_y)
plt.colorbar()
#3--
plt.show()

#grid , legend ---> 2--tanzimat 
plt.grid()
plt.legend()



#----->grid bandi
#1-
x=np.array([0,5,10,15,20,25,30])
y=np.array([0,23,43,58,74,87,92])
cc=np.array([0,20,30,40,60,80,100])
ss=np.array([100,20,20,20,20,100,100  ])
alphaa=np.array([1,0.2,0.2,0.2,0.2,0.2,1])
plt.scatter(x,y,c=cc,s=ss,alpha=alphaa)
plt.title('Nemoodaram',fontdict=font_title ,loc='left',pad=40)
plt.xlabel('MOKHTASAT',fontdict=font_x)
plt.ylabel('porosity',fontdict=font_y)
plt.colorbar()
#*** taghir dadam
plt.grid()
plt.show()

#dastet baze --> khode grid ro taghir bdi
x=np.array([0,5,10,15,20,25,30])
y=np.array([0,23,43,58,74,87,92])
cc=np.array([0,20,30,40,60,80,100])
ss=np.array([100,20,20,20,20,100,100  ])
alphaa=np.array([1,0.2,0.2,0.2,0.2,0.2,1])
plt.scatter(x,y,c=cc,s=ss,alpha=alphaa)
plt.title('Nemoodaram',fontdict=font_title ,loc='left',pad=40)
plt.xlabel('MOKHTASAT',fontdict=font_x)
plt.ylabel('porosity',fontdict=font_y)
plt.colorbar()
#*** taghir dadam
plt.grid(color='green',linestyle='--',linewidth=0.5)
plt.show()



#----
#=================LISTE RANG HAYE MOHEM ====================
#----ranh ha / color-------
'''
'b' - Blue --> default
'r' - Red
'g' - Green
'c' - Cyan
'm' - Magenta
'y' - Yellow
'k' - Black
'w' - White

'''

#---- Shekle marker ha / marker style-----
'''
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline


'''
#----- Shekle khat / line style -----
'''
'solid' (default)	'-'	
'dotted'	':'	
'dashed'	'--'	
'dashdot'	'-.'

'''



#=================================
#=================================

#pie chart--------------
#harfe darsad dar mioon abshe
# 35% , 25 % , 25 % , 15%

y=np.array([35,25,25,15])
plt.pie(y)
plt.show()

#hichi ndre

#in darsada darsayae 'mivas'
#label

lab=['Apple','banana','cher','daa']
y=np.array([35,25,25,15])
plt.pie(y,labels=lab)
plt.show()

#color haro
lab=['Apple','banana','cher','daa']
mycolor=['black','green','red','blue']
y=np.array([35,25,25,15])
plt.pie(y,labels=lab,colors=mycolor)
plt.show()

#bekeshi biron
lab=['Apple','banana','cher','daa']
mycolor=['black','green','red','blue']
ex=[0.2,0,0,0]
y=np.array([35,25,25,15])
plt.pie(y,labels=lab,colors=mycolor,explode=ex)
plt.show()


#documentation
#




#==============================
#==============================

#==============================
#==============================


#dade haye sotooonii
x=np.array(['A','B','C','D'])
y=np.array([3,8,1,10])
plt.bar(x,y)
plt.show()



#develop

x=np.array(['A','B','C','D'])
y=np.array([3,8,1,10])
plt.bar(x,y)
plt.title('Nemoodaram',fontdict=font_title ,loc='left',pad=40)
plt.xlabel('MOKHTASAT',fontdict=font_x)
plt.ylabel('porosity',fontdict=font_y)
plt.show()



#---barh
x=np.array(['A','B','C','D'])
y=np.array([3,8,1,10])
plt.barh(x,y)
plt.title('Nemoodaram',fontdict=font_title ,loc='left',pad=40)
plt.xlabel('MOKHTASAT',fontdict=font_x)
plt.ylabel('porosity',fontdict=font_y)
plt.show()

#----ranga
x=np.array(['A','B','C','D'])
y=np.array([3,8,1,10])
plt.bar(x,y,color='r')
plt.title('Nemoodaram',fontdict=font_title ,loc='left',pad=40)
plt.xlabel('MOKHTASAT',fontdict=font_x)
plt.ylabel('porosity',fontdict=font_y)
plt.show()


#andaze
x=np.array(['A','B','C','D'])
y=np.array([3,8,1,10])
plt.bar(x,y,color='r',width=0.1)
plt.title('Nemoodaram',fontdict=font_title ,loc='left',pad=40)
plt.xlabel('MOKHTASAT',fontdict=font_x)
plt.ylabel('porosity',fontdict=font_y)
plt.show()


#==============================
#==============================
#=============================
#==============================
#==============================
#---------HISTOGRAM---------
#---------distribution-------
x=np.random.normal(170,10,250)

#koli data haye tasadofi darim
#250 ta adade tasadofi sakhtim

#choon mikham faravanie adad haro bbinm
#distribution--> tozi shodan
#histogram


plt.hist(x)
plt.show()




#khoshegl
plt.hist(x)
plt.title('Distribution',fontdict=font_title )
plt.xlabel('Number (x) ',fontdict=font_x)
plt.ylabel('faravani',fontdict=font_y)
plt.show()



#-------------
#number,str,bool
#chantaee --> set,touple,dictionaey
#list
#Numpy array ( azin bejaye list estefade mishe)
#pandas ham omd goft--> 

#----------
'''
psudocode , tabe 

1-vorodi [dataee]
2-badane (body)
3-khoroji (print, plot, return)

....
vorodi  (too prantez migire, assign)
yekseri data ro brizim too ye zarf

1.1-assign
1.2-input
1.3. file ro [ azmayeshgah , maghale, simulation, ] 


file--> chijropi eestefade konam??
aval --> yejor biarish too in safe
esme baranamon --> spyder
filemon k too desktop --> bairimesh inja
va vaghty ovordim---> berizimesh too zarf


'''


#python--> built in function 
#open()
#open dota chizi migire tooye parantez
#yeki addrese file, yeki inke chiak rmikhay koni bahash

open(  ' ' , ''   )

#miri file morede nazar roosh click property --> info
#address copy mikoni
#Miay inja paste mikoni va / --> \\
#esme file man hast --> ress  
#format --> .txt .csv .docx 

open( 'C:\\Users\\apm\\Desktop\\Project\\Polito\\Semester 2\\material forming\\non metal\\ress.txt' , ' ')

'''
f_loc='C:\\Users\\apm\\Desktop\\Project\\Polito\\Semester 2\\material forming\\non metal\\ress.txt'
open( f_loc, )
'''

'''
1---> fght file ro bekhooni --> r
2--->mikhay benevisi ---> w
3--->mikhay b tahehs chizi ezafe koni --> a [file vojod ndshte bashe misazatesh]
4--> filet vojod ndshte va bkhay chizi efaze , error bht bde --> x



open( 'C:\\Users\\apm\\Desktop\\Project\\Polito\\Semester 2\\material forming\\non metal\\ress.txt' , ' ')







'''
open('Users\\apm\\Desktop\\ress.docx','r')

#yadet bashe --> brizish toye zarf

a=open('//Users//apm//Desktop//ress.docx','r')



a=open('//Users//apm//Desktop//ress.txt','w')

#r ---> read
#w ---> wrtiting
#a---> tahesh ezafe


#rooye khode file

a.read()

#5 ta characte rbkhone
a.read(5)


#ye line
a.readline()



#------baraye neveshtan
#w ya a
a=open('//Users//apm//Desktop//ress.txt','w')
a.write(' salam b enethaye jomle')


#---******** hjatman hatman
#yadet anre karet tamom shod
a.close()



#oon file ro hazf koni

import os
os.remove('//Users//apm//Desktop//ress.txt')




#--------
#read--> khondan
f_loc='//Users//apm//Desktop//Project//Hojjat Emami//Span network//Compact zip file//open that//experimental//f5.xlsx'
data=open(f_loc)



#******
#---->pandas
#tooo dele ketabkhoen yechjiozi daram k barat mitonm file haro bekhonam
#kar ba data (dade)
import pandas as pd

#list
a1=[1,2,3,4,5,6]

#numpy--> array ( sai tare)
a2=np.array([1,2,3,4,5,6])

#pandas ---> Series , DataFrame  (label bezani,sotone 0 , )
#Pandas---> function -->esme bzoorg shoro


a3=pd.Series([1,2,3,4,5,6])

a4=pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])

#series --> numpy array 1D --. indexesho avaz konm

#3 mikhaym
a2[2] #Out[133]: 3
a4['c'] #Out[135]: 3

#Numpy array 2D---------
#b radifa (chapa)--> index
#b balaha --> soton ha --> label (column)

b=np.array([ [1,2,3] , [4,5,6] ])
b[1,2] #Out[137]: 6

c=pd.DataFrame([ [1,2,3] , [4,5,6] ] ,
               index=['dama','feshar'])

#**bishtar ssoton haro taghiur  midan
c=pd.DataFrame([ [1,2,3] , [4,5,6] ] ,
               columns=['dama','feshar','zaman'])

#access---> 
#sotoon
arr_d=np.array([ [4,20],[5,23],[6,24],[7,28],[10,30],[21,45]  ])
data=pd.DataFrame([ [4,20],[5,23],[6,24],[7,28],[10,30],[21,45]  ],
                  columns=['N','Temperature'])

#dastresi 24
#numpy
#kodomr adif kodom soton
arr_d[2,1] Out[143]: 24
data[2,1] #errrorr




#yeki dastresi --> be kole soton
data['Temperature']

data['N']

#aga man yek radi ro khastam
#index ro 
data.loc[0]








#----------
#yek raveshi dare k open----> OPEN
pd.read_
#formataro neevshte


#OPEN FILE HAYE CSV , EXCELL , ...
#yek zarf besazi

a=pd.read_csv('ADRESS')



data=pd.read_excel('//Users//apm//Desktop//Project//Hojjat Emami//Span network//Compact zip file//open that//experimental//f5.xlsx')

#data ro khoonbd b shekel data fram

#dastressi

#ag soton ro bekhay

data.columns


b=data['Wavenumber  (cm -1)']



#dataye ma hamishe ghashango gahbele estefade nist
#DATA --> PREPROCESS , CLEAN, --> ready for Machine learning




#l11
#------random---->numpy



#-------PROJECT 2-------------------


'''
DEADLINE : 

subject:
A2_Project_Name_lastname

Email:
ai.2024.pilehvar@gmail.com

respond: Daryaft shod


#-------TABE -----
2 ta tabe besazim
#1-tozihat dashte bashe
#2- esmesh daghighan bozorg Stress_Curve

tabe ma bayad file ro bgire 
fek konid file e ma --->



esmetabe( data, kar)





'''

'''
Stress - strain 


'''


data=pd.read_excel('adress')

        
data.columns


def Stress_Strain( data, kar):
    #yani sotoone data ee k migirer ro
    #miad array mikone
    '''
    
    '''
    
    a=np.array(data['Wavenumber  (cm -1)'])
    b=np.array(data['Wavenumber  (cm -1)'])
    
    
    if kar=='max':
        c=a.max()
        return c
    
    if kar=='plot':
        plt.plot(b,a,c='r')
        plt.title('Stress strain')
        plt.show()
    
    


#kar --> calcualtion
#plot
        

    
Stress_Strain(data,'plot') #Out[164]: 4000







