
"""
In The Name Of GOD

Created on Wed Mar 13 14:36:36 2024

@author: ai.2024.pilehvar@gmail.com

L8

"""

'''
import ---> avale safe ye codemon mikonim 
xx vasate safe ziad monaseb nist
xx b hich onvan vasate tabe , dar badaneye if ..

#def -------- if , while for

def joda estefade mishe--> box -->if , for 
dakhele if o for --> def estefade nmishe kard

if o for dakhele ham duige mishe estefade krd


'''
#---------
#chnata ketabkhone maroof
'''
3 no mitonim import konim


import name

'''
import math
import time
import random
import statistics



#baraye estefade bayad esme ketabkhone ro bezanim
#dot bznim jolosh --> boro tooye in ketabkhone
#ketabkhoen chi dare ? --> adadaye sabet, class, tabe

math.e #adade sabet
math.sin() #tabe mikhay ()

#-----
#class ---> too delesh koli tabe hast

random.SystemRandom.choice()
#ketabkhoenyee random
#.--> bnoro dakhelesh
#boro clase systemrandom
#az dakhelesh in tabe ro bde (choice)



#--------
#------------------STep haye sakhte tabe-----------

#soale mohem****
#fek konim yek tabe ee bsazxim ke betone moadele daraje 2 ro baramon hal kone
#esmesh --> gam_root2

#1-avalin akr --> tabe bekhaym mikham
#esme tabe at ro bzar
def gam_root2

#2- tabe chi bod? ye box . vorodi khorji
# 2*x**2 + 3*x+4=0 -->x hareo bde

#2.1. voroodi
# a * x**2   + b * x + c =0
# 2*x**2 + 3*x+4=0  --> a=2 b=3 c=4
#4*x**2 + 8 =0 ---> a=4 b=0 c=8

def gam_root(a,b,c):
    


#2.2.khorojiii

#rooot --> yek risheye ye in maodel
#ya print kone (khoreoji ndrim)
#ya mikhay harja sedash zadim bma adad bargardone



#3- bebin ensan chikar mikone--> b zabone farsi bego
#farsi ro translate tooo zabane python (italy)

#a*x**2 + b*x + c=0
#---noskhe farsi-----
#-----نسخه فارسی-------
#delta = b**2 + 4*a*c
#migoftim agare delta manfi javab ndre
#ag 0 bashe ye javab dare --> - b /2a
#ag mosbat bashe delta --> -b +- radical delta/2*a

#*** agar ----> if if e elso
#*** tekrar ---> agar mahdodeye tekraro --> for ag payan msohakahs nis while
#ag bkhaym varresii --> for, while
def gam_root2(a,b,c):
    delta=b**2 + 4*a*c
    
    if delta<0:
        print('javabi nadarad moadele')

    
    if delta==0:
        root=-b/(2*a)
        print('moadele yek javab darad : ' , root)

    if delta >0:

        r1=(-b+math.sqrt(delta))/(2*a)
        r2=(-b-math.sqrt(delta))/(2*a) 
        print('moadele do javab darad: ',r1,',',r2)
        
# 2*x**2 + 3*x+4=0  --> a=2 b=3 c=4     
gam_root2(2,3,4) 
#fght print mikone
a=gam_root2(2,3,4) #none



def gam_root2(a,b,c):
    delta=b**2 + 4*a*c
    
    if delta<0:
        root=None
        return  root
    
    if delta==0:
        root=-b/(2*a)
        return root

    if delta >0:

        r1=(-b+math.sqrt(delta))/(2*a)
        r2=(-b-math.sqrt(delta))/(2*a) 
        return r1,r2
# 2*x**2 + 3*x+4=0  --> a=2 b=3 c=4     
a=gam_root2(2,3,4) #none      
    




#noskhe takmili
def Gam_Root_2(a,b,c):
    '''
    For example:
        2*x**2 + 3*x + 4=0
        a=2 b=3 c=4
        
        
    This function are designed to solve second equation
    Parameters
    ----------
    a : int
        The first coeff
    b : int
        the second...
    c : int
        second

    Returns
    -------
    The root of equation

    '''
    
    if a==0:
        raise TypeError('Please insert the secondary equation')
        
    else:
        delta=b**2 + 4*a*c
        
        if delta<0:
            root=None
            return  root
        
        elif delta==0:
            root=-b/(2*a)
            return root

        elif delta >0:

            r1=(-b+math.sqrt(delta))/(2*a)
            r2=(-b-math.sqrt(delta))/(2*a) 
            return r1,r2
        else:
            raise TypeError('Something went wrong')
    
a=Gam_Root_2(2,3,4) 

b=Gam_Root_2(0,3,4) 

c=Gam_Root_2(0,0,0) 



c='2*x**2 + 3*x + 4'
#--------qekhtiari__pishrafte___
#Root_2(c) ---> root



#=====================================

import numpy


#kolan zarf--> number, str , bool
#chnataee --> list (set,touple,dictionary)

#----sakhtare darsimon yeksan bood
#1- assign (meghdardehi)
#2-access (dastressi b ajza dashtebashim)
#3-change+
#4- iteration ( chijori berim dakhelesh varesi konim)
#5-method ( tabe haye dakhelie str , list ,...)


#--flash abck mzianam b list
#1-assign
a=[3,4,5,612,23142,432432,2]
b=list((1,3422,2552,35543,356456))

type(a)
len(a)
a=['hamid','reza']
a=[32,223,'ahmid',321231,True]

type(a)

#2access
#[] ba beraket ** index az 0
a[2]

#dastresei bartaye chi?
#3change
a[2]='reza'


#4-iteration

for i in a:
    print(i)
   
a=[3,4,5,612,23142,432432,2]
for i in a:
    if i>10:
        print('salam')
     
for i in range(0,len(a)):
    if a[i]>10:
        print('salam')
#in dota yeksanand

#5-
a.append('salam')

#ina khoroji nmidad --> emali
#yani roye khode a emal mishodan

#1- tabe haye str --> emal nemishod khoroji midad --> zarf
#2- list ---> khoroji nmidad pas chikar mikrd --> emal mishod



#list ha 2 ta moshkel daran
#1- sorateshe --> list -->khode python --> zzabane kondi --> sooratesh
#bad ha mikhay 10000 value brizi too list + - mohasebat --> kondi onja neshon mide


#2-yek sotone
#chnata soton mikham
#chanta radif mikham
#matrix
#vector
#ye jadval mikham 

#....koli---> list faghat 1 bodie
#man shayad bod haye bishtari naiz daram



#----------------
#Numpy --> man yek class(chiz) kare listo mikone ama 2 maziat dare
#50 barabare list sari tare

#shoam mitoni chan bodi bashi 2 bod 3 bod 4 bod ....

#zarf
#number,.str, bool

#chantasho mikjhyam --> list

#list ----> array (numpy)

import numpy

#1- assign (meghdardehi)
#2-access (dastressi b ajza dashtebashim)
#3-change+
#4- iteration ( chijori berim dakhelesh varesi konim)
#5-method ( tabe haye dakhelie str , list ,...)



a0=list((1,2,3,4,5))
#1-assign
#dota parantez dare
#behet khoroji mdie --> zarf
a1=numpy.array((1,2,3,4,5))
a2=numpy.array([1,2,3,4,5])
a3=numpy.array(a0)

false_array=numpy.array(1,2,3,4,5)

type(a1) #Out[35]: numpy.ndarray

#daram migm mesle liste

a1=numpy.array((1,2,'hamid',5))



#----bod--> dimention

#----0D array ( 0 bodi)-----------
#0 bodi --> vghhty fght ye adad mizni
a=numpy.array(14)


#mikhay bgi y radifi az adad ha darma , chand joz darma
#----1d ( 1BODI)-------------
#lista insheklian
a=numpy.array((43,47,234,765,24))

a2=numpy.array([1,2,3,4,5])  #man tarjih midam


#-----2d-------
#radif o sotooon (jadval)

b=numpy.array(  [1,2,3] , [4,5,6]         )
b=numpy.array( [  [1,2,3],[4,5,6]    ]  )
#paranteze k roosh eyani baraye array
#ye beraket bzarim
#hala har beraketi k tarif mikonim yek radife

c=numpy.array( [   [1,2,3], [4,5,6] , [7,8,9]    ]  )

#fasdele mohem nis
d=numpy.array([[1,2,3],[4,5,6],[7,8,9]])

#samte rast ro negah kon
#name--> esme zarf
#type--> jense cfhizi k too zrafe --> array
#size---? ( )  tedad adadi k dakheel paranetz --> bod D

    
#rooye zarfetr mitoni ndim bzni

d.ndim #Out[43]: 2
a.ndim  #Out[45]: 1

#shape hamon size
d.shape





#---Ndim #SHAPE

a=numpy.array([1,2,3,4])
b=numpy.array( [  [1,2,3],[4,5,6]    ]  )

a.ndim #1 --> 1 bod--> hamon liste
b.ndim #2--> 2bod --> jadvale --> radifo soton 

a.shape #Out[50]: (4,) --> agar yek bodi bnashe in mige chnat tooshe
b.shape

#******************
#( radif   , sootooon)

#Out[51]: (2, 3)

#2 ta radif 3 ta soton

#---------------------------
#3d------
a2=numpy.array([[1,2,3],[4,5,6],[7,8,9]])
                
                
a3=numpy.array([[  [1,2,3],[4,5,6],[7,8,9 ]],
                [  [10,11,12],[13,14,15],[16,17,18 ]] ])


#===========================================
#ravaeshe dovome import

'''
**yekbar import krdn kafie

#standard
import libname

#mokhafaf krdn
import libname as mokhafaf

#hafeze
from libname import felan_tabe

'''
import numpy
new_arr=numpy.array([1,2,3])


import numpy as np
new_arr=np.array([1,2,3])

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
a=np.array([10,20,30,40])

a.ndim #1
a.shape #(4,)


#baraye list a[ adade index]

a[1] #Out[68]: 20

a[2] #Out[69]: 30
#tooye acces--slice
a[0:2] #avalio dovomio mide 
#a[start:end]--> start ta end -1 1 donme 1 done
#a[:end]
#a[2:]
#a[start,end,2]
a=np.array([10,20,30,40,50,60,70])
a[2]
a[1:5]

a[0:5] 
a[:5]


a[2:7]
a[2:]

a[1:6:2]

#baraye do bodi
#radifo soton
#har radifeto ye beraket bezan to assign
a=np.array([ [1,2,3] , [4,5,6]   ])
a.ndim#Out[71]: 2
a.shape  #Out[72]: (2, 3) 2 ta radif 3 ta sotoon

#masalan 3 ro mikham
#radif , soton
#chandomin radif , chandomin soton
#3 ---> radife 0 ome , sotone 2 vom
'''
arr[radif , soton]
'''
a[0 , 2] #Out[73]: 3

a[0 , 1:3 ]
a[0:2 ,1 ]

#chra acces/??--> 3.1. change 3.2.iuteration


#3-change
a=np.array([10,20,30,40,50,60,70])

a[3]=100

a=np.array([ [1,2,3] , [4,5,6]   ])

a[1,1]=100


#4-iteration.............
a=np.array([10,20,30,40,50,60,70])

for i in a:
    print(i)


#ghalat
for i in range(0,len(a)):
    print(i)
    
for i in range(0,len(a)):
    print(a[i])
    
    
    
    
for i in a:
    if i>30:
        print(i)



#---2d

a=np.array([ [1,2,3] , [4,5,6]   ])

for i in a:
    b=i
    print(i)

    
    
#aval i ro mizare radie 1
#bad i ro mziare radife 2


#nemire dakhele radif


#--->nested for
#***********8

for i in a:
    for j in a[i]:
        print(a[i,j])
        

for i in a:
    for j in a[i]:
        print(j)


#dorost
for i in a:
    for j in i:
        print(j)


#5--method.......
a1=np.array([1,2,3,4])
a2=np.array([4,5,6,7])

a3=a1+a2
a3=a1-a2


#------tabe haye riazi------
arr1=np.array([1,2,3,4])
arr2=np.array([4,5,6,7])
newarr=np.add(arr1,arr2)

newarr=np.subtract(arr1,arr2)
newarr=np.multiply(arr1,arr2)
newarr=np.divide(arr1,arr2)
newarr=np.power(arr1,arr2)
newarr=np.absolute(arr1)

#round
arr=np.array([-3.166,3.66])

#ro be paen
new=np.floor(arr)
#ro b abla
new=np.ceil(arr)


#max , min , sum
arr1=np.array([1,2,3,4])
b=arr1.mean()
b=arr1.max()
b=arr1.min()
c=arr1.sum()



#----split
a=np.array([1,2,3,4,5,6])
new=np.array_split(a,3)


#---where
x=np.where(a==2) #index
x=np.where(a==5)

#+ - * /  %

b=10%2

#baraye zoj fard
x=np.where(a%2==0)

listt=[]
for i in a:
    if i%2==0:
        listt.append(i)
        
        
        
        
#------------
#reshape
a=np.array([1,2,3,4,5,6])
# 2 ta radif 3 ta soton

a.shape #Out[140]: (6,)


b=a.reshape(2,3)







#--------------
#@copy view

arr=np.array([1,2,3,4])
arr2=arr

arr[0]=100


print(arr) #[100   2   3   4]
print(arr2) #[100   2   3   4]

#har tagiri rooye arr anjam bdi chon
#bala gofti mosavie arr2 e ta tah inkaro anjam mdie

#view copy

arr=np.array([1,2,3,4])
arr2=arr.view()

arr[0]=100


print(arr) #[100   2   3   4]
print(arr2) #[100   2   3   4]
#har tagiri rooye arr anjam bdi chon
#bala gofti mosavie arr2 e ta tah inkaro anjam mdie

#view a2=a1




#copy
#yani mikham y copy bgirm k dar ayande
#roye ye motegahyeri tagir iajd krdm roo onyeki anjam nashe
arr=np.array([1,2,3,4])
arr2=arr.copy()

arr[0]=100


print(arr) #[100   2   3   4]
print(arr2) #[1 2 3 4]







#------------------
#----Join----
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])

#na mikhay + koni na copy na hichi
#mikhay bchasbooni

#mohemtrin tabe
#2 ta parantez
# b do no msihe chasbond
#ya dota radif roye ham
#ya do ta soton kenare ham


#axis

#axis=0

new=np.concatenate((arr1,arr2))
new=np.concatenate((arr1,arr2),axis=0)


new=np.concatenate((arr1,arr2),axis=1)
#AxisError: axis 1 is out of bounds for array of dimension 1


#axis --> baraye do bodi ---> radifi beham bechasboni ya sotooni



#harkodom b yek goone beham michasbonand
#join mdian
np.concatenate()
np.stack()
np.hstack()
np.dstack()

#baraye do bodi ha yechizi bename axis daran k
#taeen mikone radif be radif ya soton b sotoon





#---------QUIZ
#L8_Ali_pilehvar_meibodyu



arr1
arr2
arr3


#100 khat code

#tamame tabe haee k gofte shode estefade


#assign
#dastressi
#iteration ba for
#iteration ba for o if
#iteration ba if

np.where()
np.copy()
np.view()
np.concatenate()
np.stack()
np.hstack()
np.dstack()

np.sort()






#--------------------Class------------------
'''
tabe ha 
box
(vorodi ---> khorooji)


C ---> yek moshkel dasht --> object -oriented

C++ ---> C + object-oriented


python --> object -oriented

shey --> Object

application ( web , bank , data , ketabkhone)
--> tabe ha javab goo nistan


#yekseri magahdir ro negah daran
#shey ee besazim
#update konim
#yek tabew ye jadid besazim k khasiate tabeye ghablio dahte bashe




'''

#bank account
#pool brizam
#bad bewhem bege cheghadr pool daram 

def bank(money):
    global m
    m=money
    print('you total balance is: ',money)
    

bank(1000)

print(m)

def add(new):
    global total
    total=new+m
    print('you add', new, ' you total is: ',total)

add(200)

add(400)


#ba global , local 
#chanta tabe bsesazam
#chanta zarf besazimmm.....



#-----CLass-----

#class---> chanta adade sabet, chanta tabe tooshe

#object

'''
def name(vorodi):
    body
    return khoroji





'''
#cxlass----> asdad haye sabet , tabe

#shabihe maduel k azash adado tabe mikeshidam biron


class bank:
    new_zarf=5
    
    
    
#class-->yek chizi has k ma shey misazim azash
#seda nemizani banko
#tabe--> box bod --> call
#ewsmesho migofti ( vorodi)--> adad midadf





#classs---> miay azash shey msiazi


a1=bank()

#bank object of __main__ module --> yek bank objetc sakhtam


#in a1 chie? -->  shey 
#shey(object)  az koja ?  az class bank

#in shey ----> yekseri adad dare --> property | 
#             yekseri tabe dare --> method


type(a1) #Out[178]: __main__.bank yek sheye


a1.new_zarf #Out[179]: 5



class bashgah:
    ghad=180
    vazn=80
    
    
#classss --> property / method
#az roosh object misazim

a1=bashgah()

a1.ghad #180
a1.vazn #80

#mitoni chanta object bsazi
a2=bashgah()

a2.ghad
a2.vazn


#nemikhaym yek clas bsazim k hame objectash shabihe ham bashan


#---------------
#-----sahihe nevehstan
#esme class
#yek tabe bename init 
#toosh minevisi sewlf
#bad chiz haee k az shey mikhay frgh kone ro minevisi

class bashgah:
    
    def __init__ (self,ghad,vazn):
        self.ghad=ghad
        self.vazn=vazn
        
#yek class b esme bashgah sakhtam
#clas be ma ejaze mdiad shey bsazim
#bia y shey bsazim

#harmogeh khasti yek shey bsazi bayad
#onnae k too tabeye __init__ taruif krdi ro estefade koni


a1=bashgah(180,80)
        
#sad ta shey

ali=bashgah(180,83)

mohsen=bashgah(200,100)

#hezaran hezar shey besazi

#badan yadet mire


mohsen.ghad #Out[195]: 200

ali.vazn #Out[196]: 83

    
##review----> classsss -->property , method dasre

#classs vasew chi?---> mikhaym shey bekeshim biron (appliocation)

#har shey in property o method haro dare


class bashgah:
    
    #property ha injas
    def __init__ (self,ghad,vazn):
        self.ghad=ghad
        self.vazn=vazn
        
        
    #inja method ha
    
    def welcome(self):
        print('salam bar ozve jadide aziz ba ghade ',self.ghad )
        
        

a1=bashgah(180,80)

#in object ro skaht
#class---> 1- property
#2- method

#1------property 
#esme object ro bzn dot bzn
a1.ghad #Out[199]: 180
a1.vazn #Out[200]: 80

#2-method
a1.welcome()


#yek skahtare dg

class bashgah:
    
    #property ha injas
    def __init__ (self,ghad,vazn):
        self.ghad=ghad
        self.vazn=vazn
        
        
    #inja method ha
    
    def welcome(abc):
        print('salam bar ozve jadide aziz ba ghade ',abc.ghad )
        
        


#bank---->

class bank:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def welcome(self):
        print('khosh amadid ',self.name)

a1=bank('Ali Pilehvar Meibody',25)


a1.age

a1.welcome()



class bank:
    def __init__(self,name,age,initial):
        self.name=name
        self.age=age
        self.initial=initial
        
    def welcome(self):
        print('khosh amadid ',self.name)
        
        
    def balance(self):
        print('TOTAL BALANCE: ',self.initial)
       
a1=bank('ali pilehvar meibody',25,1000)
b1=bank('doostan',23,2000)
a1.welcome()
b1.welcome()


a1.balance()

b1.balance()


class bank:
    def __init__(self,name,age,initial):
        self.name=name
        self.age=age
        self.initial=initial
        
    def welcome(self):
        print('khosh amadid ',self.name)
        
        
    def balance(self):
        print('TOTAL BALANCE: ',self.initial)
       
        
    def deposit(self,amount):
        self.initial=self.initial + amount
        print('success')
        print('your total balance is',self.initial)
        
        
        
a1=bank('ali pm',25,1000)

#clas--> property , method

#property
a1.name
a1.initial


#method
a1.welcome()

a1.balance()

a1.deposit(200)


a1.balance()


a1.deposit(400)

a1.balance()



class bank:
    def __init__(self,name,age,initial):
        self.name=name
        self.age=age
        self.initial=initial
        
    def welcome(self):
        print('khosh amadid ',self.name)
        
        
    def balance(self):
        print('TOTAL BALANCE: ',self.initial)
       
        
    def deposit(self,amount):
        self.initial=self.initial + amount
        print('success')
        print('your total balance is',self.initial)
        
    def ATM(self,getting):
        self.initial=self.initial - getting
        print('success')
        print('your total balance is',self.initial)
        
    
    #def vam(tarikhe vam , megdhare vam)
    
    
    #def vaziate vam(mah)
    
    
a2=bank('alipm',25,1000) 

a2.age


a2.balance()

a2.deposit(2000)


a2.balance()

a2.ATM(300)

a2.ATM(500)

a2.balance()






#---------

#shoma mitoni yte class e dg besazi
#va ers bordan -->


class bank2:
    a=2
    
b1=bank2()

#agar man bkham y class jadid besazam ktamame tabe haye
#classe ghablio dashte bashe chi? --. ers


#class esme_jadid ( classi k mikhay ers borde she azash)
#1- ravesh
class bank2(bank):
    def __init__(self,name,age,initial):
        bank.__init__(self,name,age,initial)
    
#2-raveshe
class bank2(bank):
    def __init__(self,name,age,initial):
        super().__init__(name,age,initial)



a2=bank2('ali pm',25,1000)


a2.welcome()

a2.balance()



class bank2(bank):
    def __init__(self,name,age,initial):
        super().__init__(name,age,initial)

    def jadid(self):
        #kjukuhdskuhdsli
        
    def jadidtar(self):
        #kudhakuadsh
        

