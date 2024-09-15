
"""
In the name of GOD

L5

Created on Wed Feb 28 14:19:47 2024

@author: ai.2024.pilehvar@gmail.com
"""

"""
**nokteye aval
Subject: L5_mohsen_famili_**
L5-
l5
ll


**nokteye dovom: AI be hich onvan estefade nashavad dar halle quiz
    nokteye sevom: #inja az if be khatere shart gozari


#------------
#review------
# kole kalamti k too python minevisim be do shakhe taghsim mishavad :
    
    1-reserv shdoan-->L rangi mishan (1.1. python built in tabe haye dkaheli
                                      1.2. keywrod --> dastoorat --> banafsh)
    2-reserv nashodan--> sefidan --> esme zarf dar nzr
    
    
zarf--> esm gozari --> type haye motefaveti 1.1int 1.2.float 1.3.complex + - / * **
2.str ( function .upper()  ) 3.list (function .append()  )


.....

python function---> narenji --> baraye hame no hame typi estefade mishe
esme tabe ro minevisi y eparantez dare toosh 

print()
input()
len()
type()
open()



keyword--> and or , dastoorat mantegh hay eman

sharti --> if , if else , else if (elif)
halghe ---> for , while , def


"""

#vaghty ma bekhaym shart bzarim az if estefade mikonim

'''
if shart:
    body (dastoor)

**nokat if ba shart fasele dare , do noghte yadet nre
**notkeye badi --> toye shart az amalgar haye moghayese estefade konj:
    == > < >= <= =!
**body---> mitone ye dastoor bashe ya chantaa --> ta zamni k ye tab fasele dre


'''

#review

a='salam'
c=a+2

b=40
d=b+2
print(d)



a=20
if a>2:
    c=a+2

    
if a>2:
    c=a+2
    b=c*2
    d=45
    e=d**c
    print(e)


#age shart true bshe oon body (dastoor) ejra mishe , age nashe chi --> nemishe
#dar har soorat ch shart doros bashe ch nabashe --> python mire khat haye badiu ro mesle ghabl ejra mione

if a>2:
    print('ok your numb is more than 2')

print('salam')


#agar a kochiktar az 2 --> salam
#ag a bozorghtar az do bashe

#az bala b paeen az chap be rast

b=a+2 #safe chatre khaliii**


# and or
#gahi ma dota shart darim

a=20
b=30

#'ham' a bozorg tyar az 10 bashe ham b bozorgtar az 10
#bayad har dota shart true bshe
#and



a=20
b=0

if a>10 and b>10:
    print('ok')


a=20
b=15

if a>10 and b>10:
    print('ok')



#gahi vagta mikham begam 'ya' --> yeki az in dota
#or

a=20
b=0
if a>10 or b>10:
    print('ok')





#gahi mikhyam begim age shartemon true nashod yekar dg ro kon


'''
if shart:
    body1 (1 ta chanta code)
else:
    body2(1 ta chanta code)

ag shart sahih shod body 1 ro ejra kon ag nashod body 2
'''

if a>20:
    print('your numb is more than 20')
else:
    print('your numb is unvalid')
    
    
if a>20:
    b=a+2
    c=b*2
    print('your numb is more than 20',c)
else:
    print('your numb is unvalid')


if a>20:
    b=a+2
    c=b*2
    print('your numb is more than 20',c)
else:
    b=a+2
    c=b*2
    print('your numb is unvalid')
    
    
    
#elif
#gahi vaghta mikhayjm chant asharte to dar too bzari

a=int(input('senet cheghadre: '))
#agar balaye 21 bood benevis shoma ghanoni ee too usa
#
if a>21:
    print('shoma to usa ghanoni ee')

#paro bal
if a>21:
    print('shoma to usa ghanoni ee')
else:
    print('to nisti')



#****age nabood mikham y sharete dg bzaram
a=30

a=19

a=16

if a>21:
    print('shoma to usa ghanoni ee')
elif a>18:
    print('shoma too iran ghano ee')
else:
    print('shoma ghanoni nisti')



#elif

#if else
#if
# if else
# if else[ if else]
#else if --> elif



#---shartttt booood----

#'tekrarr konim'''
#FOR , While

'''
baze

for chiz in baze:
    body(dastooor)

chiz--> shomarande --> i

'''
#tabeye dakheli

#range()  adad avalie , adad akahri 

range(0,10)
#0 1 2 3 4 5 6 7 8 9


range(2,10)
#2 3 4 5 6 7 8 9


#for i in range(0,10):
    

#**daghighan--> biay i ro bzari 0 dastore paeen ejra koni
#mese halghe --> i o bzari 2 dastore paeen ejra she
#i ro bzari 3 .......


#i ro mziari 9 dastooor ro ejra mikoni --> az halghe kahrej mishi

for i in range(0,10):
    print(i)

#az halgeh kahrej shodan--> adi az bala b paeen mese ghabl code mikhone
#agha hatman bayad print dashte bashim?
#hatman bayad i bashe?

for i in range(0,10):
    print('salam')

#aksaran baraye tekrar --> 

#dota kar anjam msihe mamoolan
#1- yek kario tekrar mikhaym konim --> rabti b i nadare , rangemon
    
for i in range(0,10):
    print('salam')
    
#yeja shomarande moheme baramon
for i in range(0,10):
    print(i)
    
    

#*** hamishe rangemon malooomee --> midonam 10 bar midonam felan bar




#pas ag range maloom  nabod chi? --> yek masale dashtim rnage ro nadashtim

#while --> ye shart mizarim migim ta inja anjam bde

'''
**bayad bbini for che mikone while ro arzyabi koni


while se ghesmat dare

--------------------
i=0 #i ro adad gozarei kon
while shart:
    body
    
    
**ta zamani k shart true hast , man body(dastoor) ejra mikonam


'''
i=20
while i<10:
    print(i)
#without start



i=0
while i<10:
    #print('salam')

#run ---> endless loop --> halgheye bi payan
#yek payani barash bzarim
     

    

#bayad too body y dastoor bzarim k i ro ziad kone


i=0
while i<10:
    print('salam')
    i=i+1

#10 bar salam ro type krd

#section 1-i ro tarif mikone 2-sharte payan 3-shoamrande ro afzayesh mide dar dastoor va dastoresham k has

for i in range(0,10):
    print('salam')


#in dota kod yeksanan

#jofteshoon -->  loop ( hlaghe)--> tekrar

#fargheshon --> for --> ye bbaze ee darim bazwye moayan baraye tekrar drim
#while --> ma nemidoonim va bayad ba yek shart jolosho begirim



#nokteye akahr--> range --> 1- adade ebtedaye i 2-adade entehaye i 3-ziad shodane i ro



#noketye digar
#adade 0,2,4,6,8 chap kone


i=0
while i<5:
    print(2*i)
    i=i+1

#ye rahe dg
    
i=0
while i<10:
    print(i)
    i=i+2
   
#haminro ba for ham msihe najam dad
for i in range(0,10,2):
    print(i)



#........
#for haye too dar tooo
for i in range(0,10):
    for j in range(0,5):
        print(i , j)
        


#--------

'''
baze

for chiz in baze:
    body(dastooor)

chiz--> shomarande --> i

'''
#chiz mitonbe a bashe?

for a in range(0,5):
    print(a)

for a in [0,1,2,3,4]:
    print(a)
    
    
b_list=[0,1,2,3,4]
for a in b_list:
    print(a)

for a in b_list:
    print(a+1)

#bejaye list-->reshte

b='salam'
for i in b:
    print(i)
    

a=input('passwordet chie?:')

for i in a:
    print('*')
    
print('*',end='')




        
a=input('passwordet chie?:')

for i in a:
    print('*',end='')
    

for i in range(0,len(a)):
    print('*',end='')
    
    
#----------------
'''
structure e ye barname

1- voroodi dari
2-body (calculation)
3-khorojii

hameye inaro too ye safe code 451 khat 10 khat bnvisam


yejaee yekario ye codio 20 khate 10 khate tari fkonm

boxxx 
faghat sedash bznm ye vorodi bgire ye khoroji bde

--> tabe (function)



'''
    
'''
TABE ---> 1- parantez 2-box

structure

def esme_tabe( arg):
    body




'''

#vase zarf esm dashtim , vase tabe ham esm darim
def jam():
    print('salam')

'''
1-vorodi 2-body 3-khoroji

**2 body bayad dahste bashe
'''
def jam():
    print('salam')
#**vaghty run mikonmam hich etefaghi nmiofte


#call --> sedaaa

#age esme tabe ro seda bezanam mire body ro ejra mikone

jam() #parantez bzar python befahme dari function seda mizani

def welcome():
    print('salam')
    print('khobid shoma?')
    print('khosh omadid')


welcome()

#nokte --> print-->klhoroji nist --> calculation




#vorodiii
#age bedone vorodi
def jam():
#ag yedone voirodi
def jam(a):
#ag dota bashe
def jam(a,b):

#ag 5 ta bashe
def jam(a,b,c,d,e):

    

#**bjaye a o b mitoni harchizi delet mikhad bzari

def jam(a,b):
    c=a+b
    print('mohasebate shoma msihavad:')
    print(c)
    
    
#***ta vaghty seda nazani tabe ro , body ejra nmsihe
    

jam(20,30)



#bejaye inke in 3 khat kod ro bnvisam
c=a+b
print('mohasebate shoma msihavad:')
print(c)



#kh sade miam jam()

#in kare tabe hast

#body ----> fahmidim
#vorodi --> fahymidim

#khorojhiii??
#aya in tabe haye bala khoroji midad?

d=jam(20,30)
# d ma por nmishe--->khoroji ndarim



def tafrigh(adade_aval,adade_dovom):
    c=adade_aval-adade_dovom
    print('mohasebate shoma anjam shod:')
    print('javab: ')
    print(c)


tafrigh(20,30)




d=tafrigh(20,30)

#d=none type object
print(type(d))
#<class 'NoneType'>


#printt ---> khoroji nist --> namayeshe


def tafrigh(adade_aval,adade_dovom):
    c=adade_aval-adade_dovom
    return c


d=tafrigh(20,30)
print(d)

print(type(d)) #<class 'int'>




#1----
def setare(a):
    for i in a:
        print('*',end='')

password=input('passwordet chande?')

setare(password)


#2-


def setareh():
    password=input('passwordet chande?')
    for i in password:
        print('*',end='')


setareh()



#--------------------------

#-------------------------------------------------------------------
#quiz 1
'''
-------------BMI CALCULATOR-----------------------
yek barname besazid ke vazn va ghad ro begirad az karbar
vazn ro taghsim bar ghad be tavane 2 kone ( yani aval vazn ro be tavane 2 kone
                                           badesh ghad ro taghsm bar oon adad kone)
agar oon adad kochiktar az 18.5 bood bege under weight, ag beyne18.5 ta 25 bood bege normal
age beyne 25 ta 30 bashe bege over weight agar beyne 30 ta 35 bood bege obese agar
balaye 35 bood bege very obese




یک برنامه بنویسید که وزن و قد رو از کاربر بگیرد و قد رو به توان دو کند و وزن رو تقسیم بر آن کند
اگر زیر 18.5 بود بگه کم وزن اگر بین 18.5 تا 25 بود بگه نرمال اگر بین 25 تا 30 بود بگه اضافه وزن
اگر بین 30 تا 35 بگه چاقی و اگه بزرگتر از 35 باشد بگه چاقی مفرط

'''


#-------------------------------------------------------------------
# Quiz 2: Prime Number Checker
# Write a Python function to check if a given number is a prime number.
# The function should return True if the number is prime and False otherwise.


#-------------------------------------------------------------------
#Quiz 3:
#ye tabe n ro begire
#fibonachi ro baraye ma print kone
# Quiz 3: Fibonacci Sequence Generator
# Write a Python function to generate the Fibonacci sequence up to a specified term.
# The function should take the number of terms as input and return the Fibonacci sequence as a list.



#-------------------------------------------------------------------
#quiz4
#mashin hesab ro be soorate tabe ee benevisid ke khoroji  nadashte bashe va faghat print bede



##-------------------------------------------------------------------
#quiz5
#mashin hesab ro be soorati tabe ee benevisid ke khoroji fght dashte bashe



