
"""
In The Name Of GOD


Created on Sun Mar 10 14:21:29 2024

@author: ai.2024.pilehvar@gmail.com

L7

"""

'''
REVIEW + QUIZ
Def takmili
Class
Library --->***
Math
random
time
numpy

'''
#-----STRUCTURE-------
# python --> yek zaban hast 
#yek derakht dar nazar begirim
#harchi minevisim be do shakhe taghsim msihe
#age reserv shdoe bashe --> reserv (rangi) --> 
#1)keyword(banafsh) --> #if , if else , elif, for while
# 2-python built in function (narenji))
#age nabashe --> sefid--> zarf dar nazar migire (typoe 1-number,2-str,3-bool 4-list(set,dictionat, touple)) hgrkodom yekseri tabe dashtan
#**nokteye payani--> az bala b paeen be soorate farsi baraye khjodeton sharhe masale konid
#bad b zabane python translate


#--------------------------QUIZ
#yek text
text='dear student, Welcome to new class regarding Ai'

print(type(text)) #<class 'str'>
newtext=text.upper()


n=text.count('a')
print(n)

newtext=text.split(' ')

#1-----
newtext=text.replace(',','')
new2text=newtext.split(' ')



#2-----
newtext=text.split(' ')
a=newtext[1]
b=a.replace(',','')
newtext[1]=b



a=['user1','user2','user3']
new=input('esmeton chist')
a.append(new)


#rajebe calculator , BMI calculatro ,....

#ta alan shebhe code minevehstim

#---> Def (tabe benevisim)
#box (vorodi migire) calculation (khoroji mide) 
#**print ba khoroji (retrurn) fargh dare

#***** input mamoolan estefade nmishe

#tabe --> vorodi haro () 

#mashin hesab
num1=float(input('adade aval: '))

num2=float(input('adade dovom: '))

amalgar=input('amalgaret chist ? jam,tafrigh,zarb')

if amalgar=='jam':
    c=num1+num2
    print(c)
elif amalgar=='tafrigh':
    c=num1-num2
    print(c)
elif amalgar=='zarb':
    c=num1*num2
    print(c)
elif amalgar=='taghsim':
    c=num1/num2
    print(c)
else:
    print('eshtebah vared kardid')
    


#raise TypeError('eshtebah vared kardid')

num1=float(input('adade aval: '))

num2=float(input('adade dovom: '))

amalgar=input('amalgaret chist ? jam,tafrigh,zarb')

if amalgar=='jam':
    c=num1+num2
    print(c)
elif amalgar=='tafrigh':
    c=num1-num2
    print(c)
elif amalgar=='zarb':
    c=num1*num2
    print(c)
elif amalgar=='taghsim':
    c=num1/num2
    print(c)
else:
    raise TypeError('eshtebah vared kardid')
    


#--------inkar doros nist --> inptu kie chie
#az tabe ha estefade mikonim

#1- input too dele tabe mizaran (karbordi nis)
#2- mian bade if o for o while 
'''
if a>2:
    def
'''

#ma yek shebhe code ro k ghhablan mineveshtimn
#kocholosh krdim too ye box

def calculator(num1,num2,amalgar):
    if amalgar=='jam':
        c=num1+num2
        print('amaliat:',c)
    elif amalgar=='tafrigh':
        c=num1-num2
        print('amaliat:',c)
    elif amalgar=='zarb':
        c=num1*num2
        print('amaliat:',c)
    elif amalgar=='taghsim':
        c=num1/num2
        print('amaliat:',c)
    else:
        print('eshtebah vared kardid')
    
#sakhtar tarif mishe , hich etefaghi nmiofte ta zamani k call


#esmesho seda bezan--> ()

calculator(10,20,'jam')
#print mikone


#tabe ro besoorate khoroji --> khoroji bde
#yani btonim sedash bgeznaim berizimesh too y zarfe dg

#num1=10
#num2=20
#amalgar='zarb'

def calculator(num1,num2,amalgar):
    if amalgar=='jam':
        c=num1+num2
        return c
    elif amalgar=='tafrigh':
        c=num1-num2
        return c
    elif amalgar=='zarb':
        c=num1*num2
        return c
    elif amalgar=='taghsim':
        c=num1/num2
        return c
    else:
        print('eshtebah vared kardid')


zarf=calculator(10,20,'jam')

zarff=calculator(10,20,'zarb')


def BMI(ghad,vazn):
    bmi=vazn/(ghad**2)
    
    if 18.5<bmi<25:
        print('under weight')
    elif 25<bmi<30:
        print('mamooli')
    

BMI(1.9,80)




def new(vorodi1,vorodi2):
    formula=vorodi1*vorodi2/2
    return formula


#besoorate default
new(10,20) #100
new(10,20,30) #TypeError: new() takes 2 positional arguments but 3 were given

new(10) #TypeError: new() missing 1 required positional argument: 'vorodi2'

#default sazi

def new(vorodi1,vorodi2=100):
    formula=vorodi1*vorodi2/2
    return formula





#ag taraf vorodi 2 ro dad bzar jaye vorodi 2
#age nadad bezar 100 

new(10,20) #Out[59]: 100.0
new(10) #Out[60]: 500.0

# moshkele kam kardan ro doros mikone
#ag ziad bde

new(10,20,30)


def new(*vorodi):
    formula=vorodi[0]*vorodi[1]/2
    return formula

new(10,20,30)

def new(*a):
    formula=a[0]*a[1]/2
    return formula

new(10,20,30)
new(10,20,30,40,50,60,70,80,90,100)


#f=m*a
def force(mass,acc):
    f=mass*acc
    return f

#m=2 a=3 --> f=6

#call --> do no mitoni beri jolo
force(2,3)

force(mass=2,acc=3)
#in do ta yekian



#--------moratab kardan--> ghanon gozari
#agar khasti too tabe faghat jaye vorodi adad bzaran taheshon ,/
def force(mass,acc,/):
    f=mass*acc
    return f
force(2,3) #Out[71]: 6

force(mass=2,acc=3) #TypeError: force() got some positional-only arguments passed as keyword arguments: 'mass, acc'
    

#------
#fdght taraf bayad esm benevise *,
def force(*,mass,acc):
    f=mass*acc
    return f

force(2,3) #TypeError: force() takes 0 positional arguments but 2 were given

force(mass=2,acc=3) #Out[75]: 6

#kholse

#posshte / ---> fagaht adad
#bad az * --> faghat arg benevisi
#----tarkibi
def force(a,b,/,*,c,d):
    formula=a+b+c+d
    return formula

force(2,3,6,1) #errrorrr

force(a=2,b=2,c=6,d=1) #errrorr

force(2,6,c=10,d=20) #Out[79]: 38




#tedads bala shod ---> default ro akahre kar
#ghalat
def new(vorodi1,vorodi2=100,vorodi3):
    formula=vorodi1*vorodi2/2
    return formula
#doroste
def new(vorodi1,vorodi3,vorodi2=100):
    formula=vorodi1*vorodi2/2
    return formula





#-----------------------------------
#kheyli kheyli lotfan tamrin konid k error haro bekhonid

#ye liste englisi --> pdf dade shdoe tooye file ha

#mohemtarin error haro neevshtim

#sysntax-->  fasele , : kam gzoashti, ziad gozashti ,m jabej gozashti

# ' ' is not defined --> az yz arfi estefade krdi k asan tarf nkrdi


#str hamchin tabe ee-->

def tabe(vorodi1,vorodi2,vorodi3):
    
    
#@vorodi 1 mitone str, int , ....

#dota vorodie aval adad bashe

def tabe(vorodi1,vorodi2,vorodi3):
    c=vorodi1+vorodi2
    
    
#str aksaran baraye shart ha estefade mishe



    

#-----------------------------------
#newtonian ya non-newton
#a--> 1 a--->2

def Velocity_In_Pipe(p1, p2, mu, R, r, l, newtonian):
    
    if newtonian=='yes':
        a=1
    if newtonian=='no':
        a=2
    
    jadid=p1*p2*mu
    jadidtar=jadid*r*R*l
    final=jadidtar*a
    
    return jadidtar

#aksaran vorodi ro str migiran ag sharti bekhan bzaran

Velocity_In_Pipe(10,20,30,40,60,60,'yes')
Velocity_In_Pipe(10,20,30,40,60,60,'no')


def Velocity_In_Pipe(p1, p2, mu, R, r, l, newtonian):
    
    if newtonian=='true':
        a=1
    if newtonian=='false':
        a=2
    
    jadid=p1*p2*mu
    jadidtar=jadid*r*R*l
    final=jadidtar*a
    
    return jadidtar

Velocity_In_Pipe(10,20,30,40,60,60,'true')
Velocity_In_Pipe(10,20,30,40,60,60,'false')


def Velocity_In_Pipe(p1, p2, mu, R, r, l, material):
    
    if material=='newton':
        a=1
    if material=='non-newton':
        a=2
    
    jadid=p1*p2*mu
    jadidtar=jadid*r*R*l
    final=jadidtar*a
    
    return jadidtar

Velocity_In_Pipe(10,20,30,40,60,60,'newton')
Velocity_In_Pipe(10,20,30,40,60,60,'non-newton')



def heat(initial,up,down,left,right,time,sabete_hararti):
    
   #masalan silvero mikahd bbine 
heat(20,100,100,20,20,60, 149)

#mane ali mikham tabe am rahat tar bashe


#troo dele tabe
if material=='silver':
    a=149
if material=='gold':
    a=127
if material=='copper':
    a=113
if material=='alminium':
    a=97.5
if material=='iron':
    a=22.8
if material=='mercury':
    a=4.7
if material=='marble':
    a=1.2
if material=='ice':
    a=1.2
if material=='concrtee':
    a=0.75
if material=='brick':
    a=0.52
if material=='glass':
    a=0.34
if material=='wood':
    a=0.13
    
#esme tabe ro avaz mikonam
def heat(initial,up,down,left,right,time,material):

heat(20,100,100,20,20,60,'silver')



#-------------------------------------------------
#class ha ----> ejbariii---->

class
#basnafshj mishe
#mesle tabe ha
def


#class----> yekchizi hast ke daraye 1)yekseri adade sabet 2)yekseri tabe
#class--> too delesh kooli adade sabet, tabe dare

#choon bazi vaghta ma dar bazi karbord ha nemitonim az tabe ha
#estefade konim --> class (too delesh koli tabe hast 0 ---1000)





#----------------------------
#yeki az dalayeli k python--> ketabkhoone hashe
#yekseri anjoman ha, sherkjat ha yek ketabkhone sakhtan
#ketabkhone ha --> class ( tabe)--> koli tabe daran
#va ma mitonim az tabashon estefade konim


#baraye inke estefade konim

#pas baraye estefade ghadame aval--import

import math

import time



#nadfarimeshoon--> aval ketabkhone ro -->download




ai_calculator() #NameError: name 'ai_calculator' is not defined

#aval ketabkhone he ro import konam
#bad az delesh tabe he ro bekesham biron

#importesme ketabkhone

import aicourse

#dastressi
#ketabkhoneye aicourse yek tabe ee dare
aicourse.ai_calculator(10,20,'jam')
#Out[91]: 30
aicourse.alpha_silver #Out[92]: 130
#1--> adad bood
#2--tabe clas ()


#madule sakhtam

#------------------------------
#3 ta ghadam----
#0-downloadesh koni
#1-import name_lib
#2-name_lib va roosh dot bznm yani boro intooo
#3-oon tabe ya classs () ya adad sabete ro bekesham biron
import aicourse

aicourse.ai_calculator(10,20,'jam')



#dar nahyat --> az ketabkhoone tabe hasho mikeshim biuroon estefade mikonim



import dft
#ModuleNotFoundError: No module named 'dft'

#ketabnkhone haee hast k besoorate 
import math

#ag ovord ok ag nayovord bayad download koni


#radical begiram
# az 25 radical bgirm?


#ey kash yeki ye tabe ee misakht
#vorodi az man adadamo migrf beman khoroji (radikalesho)


#math --> man ye ketabkhonam in tabe ro daram

math.sqrt(25)

radical=math.sqrt(25)

math.pi




import aicourse


aicourse.ali_p #Out[101]: 3.141592653589793


#math

import statistics

a=[10,20,30,40,50]


def mianging(vorodi):
    s=0
    for i in vorodi:
        s=i+s
        
    n=len(vorodi)
    
    miangin=s/n
    
    return miangin

mianging(a) #Out[106]: 30.0

#statistic --> mean
#yebar import koni kafie
import statistics
        


statistics.mean(a) #Out[108]: 30

statistics.mode(a) 

statistics.stdev(a) #Out[111]: 15.811388300841896
statistics.variance(a) #Out[112]: 250



def cos(a):
    #donbale 
    return d

cos(0)




#bejaye

math.cos(0) #Out[113]: 1.0





import numpy  #mohasebat matrix (matlab)
import pandas  #kar ba dade ha (data)
import matplotlib #barayew rasm


import sklearn



#by default nadari --->

#-------------
#0-che ketabkhon ee mikhay?--> esmesho pip .... google kon .. oon neveshteye samte chapo ( pip install name) copy 
#1-bayad beri anaconda ro baz koni
#2-beri too environmentet (hatman environmenti k dari kar mikoni)
#3- cmd.exe
#4-install kon
#5-roosh click kon bazesh kon --> safe siah maire
#6-paste kon + entero bezan 


import numpy
#import numpy


#ai.2024.pilehvar@gmail.com

#dafe ye badi
#mitoni samte chap menu -->search koni cmd.exe (esme environemnte)
#safe siah miare --> pip install pandas


#hatman numpy install shode bashad







    
    
    