
"""
In the name of GOD

Created on Sun Feb 25 14:32:18 2024

@author: ai.2024.pilehvar@gmail.com

L4
"""

'''
Review:
    
    1-Python--> zabanesho + safe chat
    
    zbaanesh --> python package
    safe chat --> IDE
    
    anaconda--> man joftesho barat ok mikonm
    
    anaconda--> creat env -->spyder
    
    
spyder--> safe chat (open, edit, save o ...)

3 ghesmta dare -->code ro minevisim (editor)
ghesmatge 2--> namayesh midahad ( moteghayer ha , plot ,)
ghesmate 3 --> console -->javab midahad


ya mtionim runne koli konim --> PLAY
ya chand khate morede nazar ro run konim --> I

**ta run nashe taghiri ijad nmishe

'''

'''
python--> az bala mikhone be paeen
az chapo be rast


moteghayer --> save konim ychizio
zarf --> name --> mohtaviat ro mirizm


type--> 1.1. int 1.2. float 1.3.complex
2.str
3.boolean
...



***2 nokte koli base
python : 
    1- keyword (banafsh , dastoorat)
 2-built in function (narenjie ye tabeast ye kari mikone)
 
baghie chiz haro sefid nmayesh mide


**structure barname:
    1-voroodi (assign , open, downlaod , input)
    2-badane (calculation : a+b hooshe masnooe)
    3-khoroji (nothing, save ,save to desktop , print)
 
'''
#zarf...... (variable)
#1-Numberr-->int,float,complex
a=2
type(a)

print( type(a))

b=2.2
type(b)


c=1j
type(c)

#amalgarhaye hesabi
#+ - * / ** = 

#moghayese
#== >  <  >=   <=

#2-boolean

a=True
b=False

type(a)


#3-string ( reshte )--> character, jomle , esm , ....

ali --> esme zarfe
'ali' --> khodesh reshtas

a=ali

a='ali'




a=123
b='123'


type(a) #Out[13]: int
type(b) #Out[15]: str


#built in function
a=open('c:// .....')
print('salam')
print('salam','khobi')
a=input('salam senet cheghadre:')
type(a)
len(b)
#hame ina --> narenji --> tabe dakheli

#assign
a='salam'
type(a)
len(a)

#access
b=a[2]
print(b)

#slicing
c=a[1:4]
print(c)


#tabe haye reshte : str function
#str, list , touple, set -->noe zzarf
#in function ha fght baraye yek noe khas az variable hastan

#rangi nmishan
#$nminevisi too parantez chizi bzari


#rooye variabelt bayad noghte bzni

a='salam'
upper(a) #nissssssxxxxxxxx
a.upper #inam nis --> function parantez
a.upper()
#farghe emal ejra ....

print(a)
#emal nashodee
#tamame tabe haye str --> emal nmishe --> b y zarf --> zakhire sazi


#---emal , bargardandant #apply , return
b=a.upper()
b='SALAM'

c=b.lower()


a.count('a')
print( a.count('a'))
b=a.count('a')


a.find('m') #Out[34]: 4
a.find('a')

a='salam khobi chetori'
b=a.split(' ')


a='salam,khobi,chetori'
b=a.split(',')

a='barman'
c=a.replace('r','t')

a=input('esmeto begoo?')

a.islower()

a=input('senet cheghadre?')

type(a)

a+2

#int() -->casting
a=input('senet cheghadre?')
type(a)
a.isdigit()



#==========
#review: 1-number 2-str

#bnayad zarf eshghal krd?
a=20
b=30
c=45
d=34
e=3293428

a=2
a=int(2)

b=2.2
b=float(2.2)

c='salam'
c=str('salam')

#---> list --> multiple variable

#assign
a=[13,20,31,43,57]
a=list((13,20,31,43,57))
type(a)
#aya fght adad miad dakhelesh?
a=['ali','vahid','hamid','reza']
type(a)


a=[13,'ali',True,13.32,1j]
type(a)
len(a)


#access
a=['ali','vahid','hamid','reza']

b=a[2]
#frgh ba str
a='salam'
b=['salam','khoobi','chetori']

a[2]
b[2]

#slicing
a=['ali','vahid','hamid','reza']
a[1:4]


#change-->
a[1]='zahra'
print(a)



#-------list ha mesle str ha --> tabe daran

#list functions
a=['ali','vahid','hamid','reza']

#insert
a.insert(2,'zahra')


#a='salam'
#a.upper()

#do no tabe drim
#return ya apply
#returni --> ghablie taghir nmikone--> pas mide --> zaref mikhaym k savce konim
#apply--> zarfi nmikha--> ghablie taghir mikone
a.append('zahra')

a=['ali','vahid','hamid','reza']
b=['mohammad','amir']


c=a+b

#b ejaye inke c tarif koni --> listo mipeyvande
a.extend(b)



#midonm chio pak konm
a=['ali','vahid','hamid','reza']
a.remove('vahid')


#indexo drm bar asase ijndex
a=['ali','vahid','hamid','reza']
a.pop(1)


a.clear()
#clearr**********
a=[]
b=[]
#*****


del a
del b

del c

#del a --> a.clear() az clear

a=['ali','vahid','hamid','reza']
b=['mohammad','amir']


a.extend(b)

c=a.extend(b)
#*****c=NOne
#tabe hate str--> bar migrdonan 
#tabe haye list emal mikona



#------FUNCTIONE LIST --------

'''
append()	Adds an element at the end of the list

clear()	Removes all the elements from the list

copy()	Returns a copy of the list

count()	Returns the number of elements with the specified value

extend()	Add the elements of a list (or any iterable), to the end of the current list

index()	Returns the index of the first element with the specified value

insert()	Adds an element at the specified position

pop()	Removes the element at the specified position

remove()	Removes the first item with the specified value

reverse()	Reverses the order of the list

sort()	Sorts the list




'''



#=================
#Variable , function haye variable haro
#Python built in function --> narenji

#banafsha --> dasstooorat 

#IF
if #SyntaxError: invalid syntax

#structure

'''
***********MOHEM***********

if shart:
    dastooor [yek khat ya sad khat]

'''

print('OK')








a=15

#too shart --> amalgarhaye moghayese == > < => <=
if a>10:
    print('yes')
    
#age shart true bashe --> dastoor ra ejra mikonad

#agar nabashe chi?+
a=6
if a>10:
    print('yes')


4>3
3>4
#ag true bashe ejra mikone
#ag false bashe ejra nemikone

#****eshtebahate rayej
IF #eshtebahe aval
ifa>10 # beham bechasbonan
if a>10 #eshtebah

if a>10:
print(10)
    



#mesal
a=int(input('senet cheghadre?'))

if a>18:
    print('shoma senet ghabele ghabole')
    
    
    
#man mikham agar shartam false --> yekare dg anjam bde

'''
if shart:
    dastoore1
else:
    dastoore2




ag shart true shod --> dastore 1
agar nashod --> dastore 2

ag bala 18 bashi inakro kone ag nabashi yekare dgaro (**vel nakone)

'''
    
    
    
a=int(input('senet cheghadre?'))
if a>18:
    print('shoma senet ghanoonie')
else:
    print('shoma senet ghanoni nist')
    
    
#do no darim --> shart

#1- IF--->ag shart true bood inkaro kon ag nabod hichkari nakon
#2- IF else --> ag shart true bood inkaro kon ag nabood oonkaro kon


#else if --> elif
    
#**Nested IF else --> if els haye too dar too __>

#1-if
#1-if else


a=int(input('adade avaleto vared kon'))
    
b=int(input('adade dovometo vared kon'))

c=input('che mohasebati mikhahi?')
    
if c=='jam':
    d=a+b
    print(d)
    
    



a=int(input('senet cheghadre?'))

if a==20:
    print('congrat')

#*******
'''
***ghalat
if a=20:
    print('congrat')

a=b--> b ro briz too a
a==b --> a aya ba b barabar hast?
'''


#2ta nokteye dg

#sadta if estefade koni

a=int(input('senet cheghadre?'))

if a==20:
    print('congrat')
    
if a==30:
    print('ahsant')
    
if a<18:
    print('na')




#nokteye akhar --> dastoore shoma mitone bishtar az ye khat bashe

a=int(input('senet cheghadre?'))

if a>18:
    b=a+10
    d=b*10
    c=d+18
    print(c)
    

a=20
if a>18:
    print('salam')
    
    
print('khobi')
    







a=16
if a>18:
    print('salam')
    
    
print('khobi')



#================
#-----FOR--------
#yek kario chandbar anjam bdimmmm
#halghe--> tekrarrrr--> chandbar anjam bshe

print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')



#for.....
'''
**sade tarin halat

for i in range(0,100):
    dastooor



'''

for i in range(0,5):
    print('salam')

#----> shomarandee --> i
#b range negah mikone
#i ro yebar mzirm 0 dastore paeen ro anjam midam
#mizaram 1 ---> dobare anjam midm
#mizrem 2 anjam midm
#Mizrm 3 anjam midm
#mizrm 4 anjam midm va miram edame kod


#tekrar
for i in range(0,5):
    print('salam')
    
   
    
   
    
for i in range(0,5):
    print(i)


for i in range(0,5):
    print('salam')
    
    


#bia adade 0 ta 10 ro chap kon

for i in range(0,11):
    print(i)



for i in range(0,11):
    print(2*i)



for i in range(0,5):
    print(2*i)
#0
#2
#4
#6
#8


#if
#for




#=========================
#==========================
#=========================
#----quiz1

#list--> a==['user1','user2','user3']
#esme jadid az karbar begirim
#b tahe list ezafe kone





#-----quiz2
#ye mashin hesab besazim 
#az karbar ye adad begire , ye adade dige
#che kari konam ? agar nevesht jam ---> a+b print
#menhaaa --> a-b
#machine hesab besazim





#-----quiz3
#az karbar password begire * bezane
#ba halgheye for inkaro anjam bdan


#-----FUN------(veryyy optional)
'''
yek barname e benevisid ke betone tashkhis bede adad zoje ya fard
'''




'''
yek barname benevisid ke email address begire az karbar
va tebghe passwordrule haye maroof bebine ke aya email
vgaghe eie ya alaki ( validation)
'''

#check kone --> bozorg, kochik , character bashe


'''
yek barname benevisid ke email address begire az karbar
va tebghe email rule haye maroof bebine ke aya email
vgaghe eie ya alaki ( validation)
'''
#@ , gmail yahooo 



#Pishrafteee........

'''
adad begire factorielesho hesab kone


'''




















    




