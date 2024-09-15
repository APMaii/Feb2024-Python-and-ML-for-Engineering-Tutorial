
"""
In The Name Of GOD


Created on Fri Mar 15 16:38:38 2024

@author: ai.2024.pilehvar@gmail.com

L9


"""
#---------review
#-----python--? yek zaban --> kalamat + grammer
#--> kalamate ----> 1) reserv shodan (python msihnase) rrangu
#2)nemishnase --> reserve nashode ( esme zarrf miudoni)


#reserve--> tabe haye dakheli (narenji , print(),input(),;en(),type(),open())
#banafsh ha --> if , if else, for , while , and or , as import


#reseerve an shdo ebashe --> sefid --> esme zarf
#zarfe --> variable ( moteghayer)
#dakhelesh --> 1)adad [ int, float, complex] 2)str 3)bool (True , False)
#agar bkhaym y zarf bsazi chanta joz dashte bashe , chanat number , chnata str , chanat str o number
#--> list
#list ---> (set, touple , dictionary)
#list 2 ta moshkel dare ---> 1)konde baraye mohasebat 2) fght yebodie ( y radife) jadval (radif o sotoon) matrix , 


#numpy--> omad gfo man ye ketabkhonam yechizi daram
#be esmee array ---> jaye list estefadash kon
#mazaya --> 1) 50 barabra sari tare (mohasebat)
#2)0D , 1D , 2D, 3D


#ketabkhone ro import mikonim
#** hatman balaye safe import konid
'''
import libname
import libname as mokhafaf
from libname import felan_function

'''
#1)sade tarin
import numpy
#vase estafde bayad benveisi numpy.

#2) rahat taresh kon
import numpy as np
#vase etsfrade minevbisi np.

#3)yue tabe e bekeshi biron ebja inke kole ketabkhonaro impor tkoni
from numpy import array
# array seda bzni



#--------marsooome:
import numpy as np
#ketabkhoen ha chi daran? 1)adade sabet daran
#2) yeseri tabe daran #3)class[koli tabe o adade saabet tooshe]

import math

math.e #na parantez dare na hichi

math.sqr() #yek tabe mikeshdma biron ()

#gahi vagghta ye class miham bkshm biroon
#shoma ba tabe ee daron e class kar dri
math.mosalasat.sin()




#baragrdim b numpy---> mohasebat avalin ketabkhone ee ma yad migirim

#flash back bezanid doostan
#str, int
#list
#chnata step mirftim
#1- assign ( megdhardehi )-->atrifesh konim
#2- access ( dastressi b joz ha dashte bashim)
#3-change
#4-iteration ( ba for o if o ina brim tooye oon liste becharkhim)
#5- tabe dashtan --> method (.uppert() --> str | .append() --> list)

#numpy---> man ychi mese list daram k sari taro kahfan tare
#ghablia migoftim list
#bn in migim array

import numpy as np
#esme zarf
#0D-----
a=np.array(20)

#1D------
a=np.array((1,2,3,4,5))
a=np.array([1,2,3,4,5])

b=[1,2,3,4,5]
a=np.array(b)
# 3 ta ravehshe assign bood



#2D-------
#yedone parantez
#yesone beraket
#bad begoo chnata radif har dadif chia bashe

#har radifo toye ye beraketbzar
#radif haro comma bzn

a=np.array([ [1,2,3] , [4,5,6]  ])


b=np.array([ [1,2], [3,4,5]     ]) 


#ndim
#shape

#rooye zarfet mitoni ino bzni va bht shape va bodesho mide
a=np.array([1,2,3,4])
a.ndim
a.shape
#1
#(4,) --> yek artraye 1 bodi k 4 ozv dare



b=np.array([  [1,2,3], [4,5,6]         ])
b.ndim #Out[18]: 2 ham soton dairm ham radif (jadval )--> 2 bodi
b.shape #Out[19]: (2, 3)
#( radif , soton)  #aval radif bad soton


#ag man bkham az 1 ta 100 bnvisam bayad done done
#???
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

#numpy--> man yek tabe daram barat
#arange

a=np.arange() # az start ta stop , step step misazam 

a=np.arange(10) #az 0 ta 10-1 dad
a=np.arange(0,10)

a=np.arange(2,10)


#hala in ydone ydone mire jolo
#yeki darmion , dota darmion, se ta dar
a=np.arange(0,20,2)




#----soale aval chijori ta 100 
#besooratye default start =0 , step= 1

a=np.arange(101)
a=np.arange(0,101)


#mikham tabe ye chan bodi bsazm
#2 bodi
a=np.arange(0,100)
### chanta radif , chanta sotoon
#2 ta radif , 50 ta soton
b=a.reshape(2,50) 
#injoori --> 2 bodi mikonish
#fght bad az arnsage

#gahi vaghta hart numpy ro ba reshape mitoni shapesho taghir bdi


#-------
#yek numpy misazam k kole araye ha 0 bashan
#cxhnata assigne dg yad bdm
a=np.empty(20)
#ya
a=np.zeros(20)
#do ta radif 10 ta soton
b=a.reshape(2,10)

#miad az 1 misaze
a=np.ones(20)
b=a.reshape(2,10)
#c
c=2*b
d=123*b




#2-dastresi--ACCESS

a=np.arange(1,11)
a[2] #Out[44]: 3 daghigahn mese list


#2 bodi bod chtor
a=np.arange(1,11)
b=a.reshape(5,2)
#masalan 8
#soale aval --> kodom RADIF , kodom SOTOON
#index az 0
#radie 3 soton 1
# esme_araye[ kodom radif , kodom soton ]
b[3,1] #Out[47]: 8



#agha accersss kardim k chi beshe ?--->
#2.1. change  2.2.iteration (for)
#3- change

b[3,1]=100 #--> chnaghe

#iteration
'''
for i in b:
    #if 
    #dastoor
    #haerkariii
    '''
    
#+ - * 
# mohasebate matrisio dare

a=np.arange(1,11)
b=np.arange(11,21)

c=a+b
d=a-b
e=3*a

#ya mitone az taabsh 
new_c=np.add(a,b)
new_c=np.subtract(a,b)


#**khdoetono darfgir ejoin nakaonid felan
#join---->
'''
np.concatenate((a1, a2, ...))


np.stack()
np.hstack()
np.vstack()
np.dstack()

1- dot array kmikhay bchasbooni chan bodie

2-mikahy az kodom samt bhm bchasboni --> axis

'''
# libname.tabe(  )
#  esme_mpoteghayer.esme_)function()


a=np.arange(1,11)
b=np.arange(11,21)

c=np.concatenate((a,b))

d=np.concatenate((a,b),axis=1)
#AxisError: axis 1 is out of bounds for array of dimension 1

#axis baray 2D
a2=a.reshape(5,2)
b2=b.reshape(5,2)

c=np.concatenate((a2,b2))
#dar rastaye radiif gozasht rooye ham

#defaultesh axis=0
c=np.concatenate((a2,b2),axis=0)
#axis=0 --> dar rastaye radif


#dar rastaye sotonn--> axis=1
d=np.concatenate((a2,b2),axis=1)



#--------------------------------------------
#faghat araye ye numpy
#na word, na file , na excell 
#save---->
# np.save( 'esme_file',kodom_array )

np.save('arraye_khodam',a)
#biroone computer
#rast file ro bbin

#load koni
#az koja --> computeret
#yja baya dbrizi --> naiz b zarf dari
#1--shod
b= np.load('arraye_khodam')


#2-shod
b= np.load('arraye_khodam.npy')

#3-->nashod
b= np.load('C//User/ali/arraye_khodam.npy')

#-----------------------
#shoam mikhay 
a=np.arange(0,11)




#boro yek array 1 bodi doros kon k 10 ta ozv dashte bashe
#10 tasho random bzar


#Random assign


#ketabkhone------
#esmesho search bezan

#---> donable documentation ( balaye tolbar, apen chap rast)
#getting start , 



#--------MATPLOTLIB---> RASM ---> tasavir
#matplotlib --> plot, scatter, bar, histogram , piechart , ....
#numpy , pandas , sklearn ---> hamashon yechi pa smdiadsn-->zarf mizashtim
#matplotlb ---> rasm mikone
#fght ejraa



#aval import
#------
#pip install matplotlib
#pip install matplotlib.pyplot


import matplotlib as mlp


import matplotlib.pyplot as plt

#do ta noghte 
#(x,y)
#( 1,5)  (2,10)

x=np.array([1,2])
y=np.array([5,10])

#ketabkhoneye plt , yek tabe dare bename plot

#plt.plot(x,y)


plt.plot(x,y)


#ag x nadi --> x ahro default mige az 0 shoro mikone
#x ro khodehs maid z 0 b bala
plt.plot(y)


#base base baseee
#dastresisho mdie
#in tabe he koli vorodi dare

#vorodie aval x hato y hat hast
#vorodi haye badit---> settingete

#1---> nokte eshare kon
#do ta nopghte ro beham chasboonde

plt.plot(x,y,'o')
#x o y rto rasm kon , noghte bzar

#ye listi darim --> liste marker ha
plt.plot(x,y,'*')


#ham khat mikshe ham noghte mziare
plt.plot(x,y,marker='o')




#----------------
#default --> abi

#fght noghte
plt.plot(x,y,'o')
#fght khat
plt.plot(x,y)
#ham khat ham noghte
plt.plot(x,y,marker='o')



#marker size --> ms
plt.plot(x,y,marker='o',ms=20)

plt.plot(x,y,marker='o',ms=40)

plt.plot(x,y,marker='o',ms=15)


#mec--> dorewsho rnagi kon
#rang---> list 
#r--> red
plt.plot(x,y,marker='o',ms=15,mec='r')

#mfs--> tooye point
plt.plot(x,y,marker='o',ms=15,mfc='r')



#ham doresh ham toosh
plt.plot(x,y,marker='o',ms=15,mec='r',mfc='r')

plt.plot(x,y,marker='o',ms=15,mec='r',mfc='r')
'''

def plot( a,b,c,d,e,f):
    sda
    adadsf
    fsadfa
    affa

plt.plot(x,y,mec=r)
#NameError: name 'r' is not defined
plt.plot(x,y,mec='r')
'''


#line ---> taghir bdm chikar konm
#line style ---> ls

plt.plot(x,y,marker='o',ms=15,mec='r',mfc='r')

plt.plot(x,y,marker='o')

plt.plot(x,y)

#har setash ye khati (line) darim

#line style-->LS--->list
plt.plot(x,y,ls='-') #default
plt.plot(x,y,ls='--')
plt.plot(x,y,ls='-.')
plt.plot(x,y,ls=':')



plt.plot(x,y)

#range khdoe khato mikham taghir bdm
#color

#c
plt.plot(x,y,color='r')
plt.plot(x,y,c='r')

#hala tarkibi
plt.plot(x,y,ls=':',c='r')


#------andaze line
plt.plot(x,y)
plt.plot(x,y,linewidth=20)

plt.plot(x,y,linewidth='20')


#-------
#point ( shekle point) , andaze point
#range doresh , range dakhelesh
#khat bodan ya nabodan
#style khat, range khat , andaze khat

#harkodomo k bkhay tagir bdi bayad dar 
#tabeye plt.plot benevisim

plt.plot(x,y)

plt.plot(x,y,marker='o',c='r')

#---------
#https://matplotlib.org/stable/gallery/color/named_colors.html

#---
#green- 'g'
#red---> 'r'
#
plt.plot(x,y,marker='o',c='g')

plt.plot(x,y,marker='x')

#----
#=================LISTE RANG HAYE MOHEM ====================
#----ranh ha / color-------
'''
'r' - Red
'g' - Green
'b' - Blue
'c' - Cyan
'm' - Magenta
'y' - Yellow
'k' - Black
'w' - White


همچنین برای رنگ ها کافیه برید سایت زیر
sitte e zir rangaro keshide va jolosh esmeshon
yani masalan bejaye 'r' kafie esme onaro bnvisid va rnagesh zaher mishe
https://matplotlib.org/stable/gallery/color/named_colors.html



#baraye colour map ha --> oonaee ke rangaye shedati hast
#yani bayad shedat bedid ham mitonid berid paeen begid
masalan az 0 ta 100 / biad gehrmez ba abi ya masalan zard b sabz ya ....

https://matplotlib.org/stable/gallery/color/colormap_reference.html


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


#=======================
#yek formulaa
#y=4*x

x=np.arange(0,100)
y=4*x

plt.plot(x,y)

#ina k didi 
#dakhelesh mitooni
#tamame tanzimate rango , shap e, style ro taghir bdi


x=np.arange(0,100)
y=x**2
#y=np.power(x,2)
plt.plot(x,y)

plt.plot(x,y,ls='--')
plt.plot(x,y,ls='-.',c='c')
plt.plot(x,y,ls='-.',c='c',linewidth=7)


#================
#******
#OPTIONAL
import math
a=np.arange(0,100)
b=math.sin(a) #tabeye sinous fght yek adad migire naa array


#doone doone toosh , vase harkodom sin hesab konm
#doone done raftan --> varresi--> iteration (for)
new_list=[]
for i in a:
    new_list.append(math.sin(i))
    
plt.plot(a,new_list)


c=np.array(new_list)
plt.plot(a,c)




#-----
x=np.linspace(0,100,1000) #assign
#mige az start ta end --> b n ghesmat taghsim benevis --Z>ashari

y=2*x

#---------------





#---QUYIZ 8 , 9 --> PAYTAN SAL 
#HAMOON QUIZ 8--> tamame oon tabe haee k gfote shode boood + arange + zeros , ones
#.....-->10 khat kod
#dar netheash rasmeshonam kon



#plot--->nakafie --> naghese
#title --> nadare


#xlabel , ylabel , title 



x=np.arange(0,100)
y=x**2

#title, xlabel, ylabel hame ekhtiarie

plt.plot(x,y,ls='-.')
plt.title('Nemoodare man')
plt.show()


plt.plot(x,y,ls='-.')
plt.xlabel('Infill rate')
plt.ylabel('porosity')
plt.show()


#kamel tarin
# x o yeto mdii, tanzim mikoni rnago pointo hamechito
#label gozari
plt.plot(x,y,ls='-.')
plt.title('Nemoodare man')
plt.xlabel(' TANZIMATE VOORDI')
plt.ylabel(' MODULUS')
plt.show()

#------------

x=np.random.randint(0,100,(200,))


plt.plot(x)

plt.bar(x,)

plt.hist(x)





