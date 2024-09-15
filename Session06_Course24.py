
"""
In The name of GOD
Created on Sun Mar  3 14:37:21 2024

@author: ai.2024.pilehvar@gmail.com

L6


off----> tamame jalasato --> my code , code 
review ---az basic az 0 ta function ha (porozhe A1)

subject= A1_AMIR_Ghasemi_Project


l7-->yekshanbeye 10march --> 20

NOKTE:
l7,l8,l9 --> ketabkhoone haye numpy,pandas, matplotlib

l10---> l14,l15 --->hooshe masnooe 



gheyre ejbari:
quiz akahre jalase (L)
quiz in telegram

ejbari:
project (A1,B2,C3)
20 % 30% 50%




#===============review
yek derakht darim---> dota shakhe 1-kalamati rerserv hastan 2- nistan

vaghty inja chizi minevsiim --> age reserv bashe rangi mishe age nabashe esme zarf midonatesh


reserve ha --> 1.1.python built in function(narenji) 1.2.keyword ha

#negah kon b khate 57


#-------------shakheye chap
#ag reserv nashode bashe be onvane zarf mishansatesh 
#khode zarf chan noo hastan
#1. number (1.1.int 1.2. float 1.3.complex)  2.str 3.bool 
#4.iterable[daste ee ke joz dare] ( 4.1.list (shabihesh) 4.2.set 4.3.touple 4.4.dictionary)
#chiasho yad grftim? assign(megdhar dehi) l,l, index [] (access) , taghir , hazf konim , ezafe konim
#yek tabe haye dakhelie khodeshono dahstn , for instance .upper() .find('a') | .append('ali')



#-----------shakhe ye rast (reserv)

narenji --> function --> () --> built in functionn
maroof tarinash

print() ---> chap mikone (**khoroji na fght namayesh)
input() ---> az user migire va zkhire (**khoroji dare) | features : 1.hamaro str zakhire mikone
type() --> typ dakhele zarf chie
open() --> dakhelesh address mizanim va b soorate khoroji data ro b ma mide
len() --> size e dakhele zarfo

#https://docs.python.org/3/library/functions.html

bool()
int()
float()
str()
#ina baraye casting estefade mishan
#man mikham ye adad ro az sahih bokojnam ashari


range() ---> for bekar miomd


"""

a=-2

b=abs(a)
print(b)



a=4.4
b=int(a)
print(b) #4


a=[14,15,16]
b=max(a)

print(b) #16

c=min(a)
print(c) #14

d=sum(a)
print(d) #45

a=[20,13,15,18]

e=sorted(a)
print(e)

a=['c','a','m']
e=sorted(a)
print(e) #['a', 'c', 'm']


a=['mohsen','ali','abas']
e=sorted(a)
print(e) #['abas', 'ali', 'mohsen']


a=['A','a','B','b']
e=sorted(a)
print(e) #['A', 'B', 'a', 'b']


a=['A','a','B','b',3,54]
e=sorted(a)
print(e)
#TypeError: '<' not supported between instances of 'int' and 'str'
a=345
e=sorted(a)
#TypeError: 'int' object is not iterable

a='ali'
e=sorted(a)
#str ---> iterable 
#'ali' --> ['a','l','i']


#----keyword
#dastoooraye ma ---> keyword
#banafsh msihan
#tabe nistan XXXX --> yek kari mikonan
if #shart
else #alternative sharte
elif #else if
for #loop
while

and #comparison  ham sharte 1 ham sharte 2
or #comparison yeki az in 2 shart

def
class #yek chizi hast k chanta def dare
return

del



#------yekam bishtar rajebe for harf bznim
#if ---> jaee shart bezarim (velesh kon ag nashod)
#if else --> jaee ke shart mziarim (alternative)
#if elif --> shart bad az sharte avali

#for , while--> loop --> tekrar iter ,

#for --> baze amon msohakahse , while zamoni k moshakahs nist
#for hamoon whiule hast k kh kootah neveshte mishe


#while
#1- i tarif she
#2-sharte payam
#3- i ro hey afzayesh mdiadi
i=0
while i<10:
    print('in body hast mitone chantga bashe')
    i=i+1

#for miad ba ye tabeye range hame inkararo mikone

for i in range(0,10):
    print('in body hast mitone chantga bashe')

#besooratye default 1 done ziad mikone
i=0
while i<10:
    print('in body hast mitone chantga bashe')
    i=i+2  
    
for i in range(0,10,2):
    print('in body hast mitone chantga bashe')


#for haro too ham mishe estefade krd---> nested for
#for o if --> mixed structure

#for --> 1-tekrar 2-iteration ()

a='Hamidreza'


b=[2,3,54,243,76,12]


#berii dakhelesh va doone doone varesh dari hala ya taghir bdi
#ya ye sharti bbini ya harchiiiziii

#mohem--> beri dakhel-->done done -->Varesii -->iteration

#boro tooo a done donaasho bekesh biron ....
for i in a:
    #baraye har doone in karo kon
    print(i)

c=0
for i in a:
    if i=='a':
        c=c+1
    
print(c) #2

#tooye range
for i in range(0,10):
    print(i)

a='hamidreza'
for i in a:
    print(i)


#range(0,len(a)) --> range(0,9)
for i in range(0,len(a)):
    print(i)


#yeseri kara hast too iteration anjam midan dar ayande

#elzamii nis
#tarfande

#counter 
#y zarfe khali k mishmore

#soal --> dar name chanta a darim?
#bnayad beri done done begardiu-->iteration-->for
name='hamidreza'

#y zarfe khali doros mikonan
counter=0
for i in name:
    if i=='a':
        counter=counter+1
#counter dare chikar mikone?--> mishmore

#aya hamishe esmesh bayad in bashe

d=0
for i in name:
    if i=='a':
        d=d+1
    

f=0 #hatman bnvbisi       
for i in name:
    if i=='a':
        f=f+1

#NameError: name 'f' is not defined



#append estefade mikonanj
#bazi vaghta nemikham beshmoram
#Mikham bekeshamesh biron

name_list=[34,56,13,545,243,12,54,23,30]

for i in name_list:
    if i<40:
        newlist.append(i)
#NameError: name 'newlist' is not defined
name_list=[34,56,13,545,243,12,54,23,30]
newlist=[]
for i in name_list:
    if i<40:
        newlist.append(i)


#dota tarfand yadet dadam dar for ha
#1- beshmori 2-bekeshish biron

#taki estefade mishe?

name_list=[34,56,13,545,243,12,54,23,30]
newlist=[]
counter=0
for i in name_list:
    if i<40:
        newlist.append(i)
        counter=counter+1

print(newlist)

print(counter)




#vaghty mikhay bekeshi biron yadet bashe
#tabe haye str khoroji mide emal nmishe
#tabe haye list emal mishe
name_list=['A','B','C','d','e']

for i in name_list:
    if i.isupper() == False:
        i.upper()

print(name_list)
        


for i in range(0,len(name_list)):
    if name_list[i].isdigit()==False:
        name_list[i]=name_list[i].upper()
print(name_list)

        

pass
break
continue


#age khasti terkar bshe fore khali
for i in range(0,11):
    print(i)
    
    
#age yek jaee az tekrar khasti ye kare dg bshe if else    
for i in range(0,11):
    
    if i==4:
        print('salam')
    else:
        print(i)
        
        
#
for i in range(0,11):
    if i==4:
        continue
    
    print(i)

#bn continue residi edame ro ejra nakon boro loope badi
#aasz halghe biron nemiad mrie adade badi




#yeja mikhay bgi az halghe bia biron
for i in range(0,11):
    if i==4:
        break
    print(i)



for i in range(0,11):
    if i==4:
        pass
    print(i)
#nothing -->pass

#emal shodan ya khorooji dadan ro dobare tozih midid?
# mesal ha ro motevaheh misham vali tooye mani in do
# moshkel daram

a='salam'

a.upper()

print(a) #salam
#rooye a emal nmikone balke return mide.
#emal nashodd--> khoroji--->zarf
b=a.upper()



a=['ali','hamid','vahid']
a.append('reza')

print(a)

#emal shode--> khoroji nis balke mostaghim emal mikone--> niazi b zarf nadarim

#tabe haye type (str, list)--> ya emal mishan ( zarf nmiukhaym ) ya khoroji midan emal nmisha



'''
tabe --> box

vorodi --> process --> khoroji

vorodi , body, khoorji

styructure:
    
def esmetabe(vorodi1,vorodi2,...):
    body ( chanta bashe)
    
    return c 

**nokat
#esme tabe ro bayad daghigh hamoon ghanonaee ro rayat koni
#ke vase esme zarf mikrdi

#mitone vorodi dashte bashe mitone nadashte bashe ()
#chanta dashte bashe , , , , , 

#tabe ha --> 1-khoroji dare (return)  2-nadare


'''

#1-bedoone vorodi bedoone khoroji

def welcome():
    print('salam arz shod khosh amadid')

#hichi ejra nmishe --> zakhire msihe sakhtar

#sedash konam







#-----clc
'''
tabe ha :
    
    1- tariifesh konim (besazimesh)
    2-baraye estefade --> call (sedash konim)

'''
#1-tabe ee k na vorodi dare na khorji
def welcome():
    print('salam arz shod khosh amadid')



welcome()
#1- vorodi ndre --> choon vgorodi nadadam behesh
#fght print kard chizi bema pas nadade--> khoroji ndre

b=welcome()


#2-vorodi dashte bashe khorjji nadashte bashe
def jam(a,b):
    c=a+b
    print(c)
    
jam(30,40) #print-->70

b=jam(30,40)

#3-ham vorodi ham khoroji
def jam(a,b):
    c=a+b
    return c
#return yanichi ? yani ini k joloyue mane ro bzar jaye oon chizi k sedam zade

jam(30,40)

#Out[66]: 70
#out--> print nista --> in khorojie tabe he
b=jam(30,40)


#tabe bedone vorodi ba khoroji

def p():
    return 3.14

d=p()





'''
1-voroodi
2-calculation(body)
3-khorojii





'''

#*****************
#khasti tabe ro bkhoni bebin python che shekli mikhone
#1- tabe ro misazi bad call mikoni

tafrigh() #NameError: name 'tafrigh' is not defined

def jam(a,b):
    c=a+b
    return c


jam(30,40)

#aval mikhone mibine ke reserv nashode rangi nis
#sefide--> reserv nashode --> hatman esme zarfe
#parantez dare--> atbe hast
#bar migrde bala mibine tabe he tarif shod eya na ag nashod ebood error mide

#negah mikone chanta vorodi mikhad
#voroodi haro migire 
#a=30 , b=40  * movaghat va local
#body ro ejra mikone
#harja return resid bar migrde hamonjaee k call shpode

jadid=jam(30,40)
print(jadid)

#tamame zarf ha o esm haee k dar vorodi, badane , khoroi atrif msihe local (movaghat**)

print(a)
#NameError: name 'a' is not defined
print(b)
#NameError: name 'b' is not defined

print(c)
#NameError: name 'c' is not defined

#locsl

#man shayad yechizi bekham k save beshe
def jam(a,b):
    c=a+b
    d=c*10
    return c

jadid=jam(30,40)

print(d)
#NameError: name 'd' is not defined


def jam(a,b):
    c=a+b
    global d
    d=c*10
    return c

jadid=jam(30,40)
print(d)


#yek zarfe hamishegi sakht--> global
#*** local--> fght dakhele tabe shenas hastan  biron nistan
#gloval--> yani hamej ashenasan


#------------
#mashin hesab-------------
#num1 num2
def mashin_hesab(adade_aval,adade_dovom,amalgar):
    
    if amalgar=='jam':
        final=adade_aval+adade_dvom


#short tar
def mashin_hesab(num1,num2,amal):
    
    if amal=='jam':
        cal=num1+num2
    if amal=='tafrigh':
        cal=num1-num2
    if amal=='taghsim':
        cal=num1/num2
    if amal=='zarb':
        cal=num1*num2
    if amal=='tavan':
        cal=num1**num2
        
    return cal
    

zarf=mashin_hesab(10, 20, 'jam')

print(zarf) #30




#tabe ee besazi k khoroji nade balke fght print kone

def mashin_hesab(num1,num2,amal):
    
    if amal=='jam':
        cal=num1+num2
        print(cal)
    if amal=='tafrigh':
        cal=num1-num2
        print(cal)
    if amal=='taghsim':
        cal=num1/num2
        print(cal)
    if amal=='zarb':
        cal=num1*num2
        print(cal)
    if amal=='tavan':
        cal=num1**num2
        print(cal)

mashin_hesab(10, 20,'jam')    

zarf=mashin_hesab(10, 20,'jam')
print(type(zarf))


def mashin_hesab(num1,num2,amal):
    
    if amal=='jam':
        cal=num1+num2
        print('adade mohasebe shode:')
        print(cal)
    if amal=='tafrigh':
        cal=num1-num2
        print('adade mohasebe shode:')
        print(cal)
    if amal=='taghsim':
        cal=num1/num2
        print('adade mohasebe shode:')
        print(cal)
    if amal=='zarb':
        cal=num1*num2
        print('adade mohasebe shode:')
        print(cal)
    if amal=='tavan':
        cal=num1**num2
        print('adade mohasebe shode:')
        print(cal)
        
    return cal



zarf=mashin_hesab(10,20,'jam')





#----farghe print , khorojiii


#*********
#ma chra az tabe estefade mikonim?

#k y codi dariim (body) , hamishe ye khoorji migirim
#yekseri chizasho taghir mitonim bdim


#koja mestefade msihe az atbe---> hamin script (safe chat)

#call (vorodi midi) --> khoroji migiri --> zarf

##input---> fun

a=int(input('adade aval ro vared konid'))
b=int(input('adade dovom ro vared konid'))
c=input('amalgare morede nazar')

def mashin_hesab(num1,num2,amal):
    
    if amal=='jam':
        cal=num1+num2
    if amal=='tafrigh':
        cal=num1-num2
    if amal=='taghsim':
        cal=num1/num2
    if amal=='zarb':
        cal=num1*num2
    if amal=='tavan':
        cal=num1**num2
        
    return cal
    

zarf=mashin_hesab(a,b,c)

print('\adade hesab shode : ' , zarf)

#in vase quiz--> fune

#user poshte console nasheste

#baraye tabe khodemon too kodemon estefade mikonim
#XXXXXX---> input fune

def mashin_hesab(num1,num2,amal):
    
    
    if amal=='jam':
        cal=num1+num2
    if amal=='tafrigh':
        cal=num1-num2
    if amal=='taghsim':
        cal=num1/num2
    if amal=='zarb':
        cal=num1*num2
    if amal=='tavan':
        cal=num1**num2
        
    return cal

mashin_hesab()


material='Al'
K_dif=95
k_dif2=120

final=mashin_hesab(K_dif,k_dif2,'jam')

def Newton_law(m,a):
    
    F=m*a

    return F


zarf=Newton_law(10,2)

zarf=Newton_law(10)
#TypeError: Newton_law() missing 1 required positional argument: 'a'




#a b soorate def

#hamishe a =10
#magar inke user taghir bde

def Newton_law(m,a=10):
    
    F=m*a

    return F

Newton_law(10,2)

Newton_law(10)


def Newton_law(m,a=10):
    '''
    M= mass
    A= shetabe 
    in tabe be shoma F midahad k niroo hast
    
    '''
    F=m*a

    return F


zarf=Newton_law()




#===========
#proje

#yekser adad k baste be reshteye khodeton
p=3.14


#miangin 5 ta adad bayad bsazid

#yek tabe besazim











