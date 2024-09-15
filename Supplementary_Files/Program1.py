#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:12:59 2024

@author: apm
L4 B bad
"""

#======================================================
#python Booleans

#mesle adad ha mesle reshte ha
#adad ha ma dashtim
#string ha k dashtim
#yechizi darim بولی
True
False
#** harfge adad bozorg
a=True
type(a) #bool
len(a)

#koja bekar mire ?
#javabe com[parison operator ha hast]

a=b #frgh dre ba
a==b

a=b #assign yani migi a ro khali kon b ro briz toosh
a==b # yani dri miporsi a barabar ast ba b?
#pas montazere chi e ? javab
#javab chie? booly

a=2
b=2
print(a==b) #True

a=2
b='2'
print(a==b)#False
#ma fahmidim bejoz int,float comples, str clas ha va type ha
#class=type
#haye dg ee ham darim mesle boolean
#mohmtrinashon int,float,str,boolean
#ychiz dg darim sequence ( radif ya donbale) ke shamel shode az chanta

#--------LIST---------
firstlist=[7,8,4,2,9]
#esme zarf, mosavi , mohtaviate zarf dakhele yek beraket
#va tavasote comma joda shavad
#oon bala rast negah konid -->
#name=esmeshe type=list , size=5 , value=.....
#ye rAH DG HAS
type(firstlist) # type
len(firstlist) #size
#kafie bnvisimesh bnaraye value
print(firstlist) #value

#yek rahe dg baraye assign

firstlist=list(1,2,3,4)
#TypeError: list expected at most 1 argument, got 4
#parantez
firstlist=list((1,2,3,4)) #dovomin rahe assign

#set dictionary,touple hamashon yekian masalan frghaye jozi
#m,asalan yeseri ghabele taghir nistan
#yeksderia index bandi nashodn va beham rikhtan

#che type haee migire ? hamechi?
#fght adad ? nma begop hamechi

second=['ali','mehrzad','amir','amirali','mohammad']


#bayad yeki bashe , gharo ghati asan
third=['ali',3,'mehrzad',20,True]



#-----------------
#access---- yani dastresi
#daghighan mese str hast fght
#har value ro mese character mibine

a='ali'
a[1]
#migoft kolan 3 ta char( character) dre , bia az 0 na 1 yni dovomio brdar

#ama list nmige char mige oon element ro
a=['ali','mehrzad']
a[1]

#----------slcie drim

listt=[46,32342,747,124325,253734,     24626532,252625,2652]
listt[1:3]#[32342, 747]
#hata mitonid begid chanta chanta boro jolo
listt[1:5:2] #[32342, 124325]

listt[:4] # az 0 ta 3
listt[4:] # ta akahr
#-------------------
#change----------------
listt=['user0','user1','user2','user3','user4','user5']

#taghir bdim
#kodomo taguhir bdim? felan
#aval access bad change(modify)
listt[3]='AMIRHOSSEIN'


#taghir yafft
print(listt)
#['user0', 'user1', 'user2', 'AMIRHOSSEIN', 'user4', 'user5']

#MITONIM CHANTARO TAGHIR BDIM
listt[3:5]=['ali','amir']
print(listt)
#['user0', 'user1', 'user2', 'ali', 'amir', 'user5']

#ma hame karaye assign. accesss, slice , change ro yd grftim
#masalan set o ... baziashon taghir nmikone
#bayad tabdilesh krd b list ba list() taghir dad dobre tabdil krd
#bazia tekrari nmigire
#bazia index ndre

#---tebghe mamool ma yekseri method drim
#che no methodie ?
#str , int , ... chi bodan ? type
#behesh class ham gofte mishod
#har clas yekseri chizi dre bename methods
#list ham yek type ya yek class has va accordi9ngly 
#chi dre?
#methods

#-**methodha ziadan ama mohemasho nesbatan hefz shin ama niazi b hefz niss

#mesle har methodi aval value ro esmesho minvisim
#noghte miznim
#esme method
#dakhele parantez ehyanan setting
listt=['user0','user1','user2','user3','user4','user5']


new_list=listt.insert()
#yani aval kodom index , va chi tosh bzrm?
listt.insert(6,'ali')
#ezafe krd
#nmiaz b zakhrie nist
#choon rooye current ( liste hal) taghirat emal mishe ( apply)

#agar khali bod ke hichi ezafe mikone
#agar por bood miad yedone mizare baghie ro be roo bala hol mide
listt.insert(3,'ali')


#mohemtrin
#in tabe haa miad taghirat ro rooye value emal mikone

#append yekioaz mohmtrin hast
listt.append('jadid')
#be akahresh miad ezafe mikone

pass_list=[1234,0000,234245,143432,3132423]
new_password=int(input('please insert your pass:'))
#miaym az append estefade mikonim
pass_list.append(new_password)


new_password=int(input('please insert your pass:'))
pass_list.append(new_password)
#farghesh ba insert ine ke insert niaz b index dare ke tarif konim ama
#in mizare tah karfi b index ndre

#---------------------------------
#dr ghabli ha fght ewlement ezafe mishod
#agar bekhahim yek sequence( mese list)
#kolesho ezafe konim chi?

#extend
#miad ye element fght 
list1=['a','b']
list2=['c','d']

new_list=list1+list2 #yek rah

list1.append(list2)
#dakhele list yek omde
#kole list ro rikhte na done done
#ma mikhastim c ro joda brize d ro joda brize ama kolesho be onvane ye lis


list1=['a','b']
list2=['c','d']
list1.extend(list2)

#remove chan ravesh dre
#AZ TARIGFHE ESME ELEMENT
list1.remove('a')
#az tarigfhe index
list1.pop(0)

#kodom ;list 1?? bbinid list 1 hezarta dshtim ama
#choon python az bala b paeen mikhone
#akharin taghiri k dadio yadesh mimone

#akhario ytadeshe python
#alan list1=[d]
#pas dobare asign bdid
list1=['a','b'] # va run
#az keyword python
del list1 #kolesh pak mishe
del list1[0] #oon element pak mishe
#kamel pak mishe moteghayer zarfo jasho tohsao hameja
list1.clear()
#list 1 yek zarfe ke liste ama toosh khalie

#del miznim kole list1 mipre
#cleasr tosho khali mikone


#========================
list1=['d','b','a','c']
list1.sort()
#yani miad tabeye sort ya hamon methode sort ro rooye listr 1 apply emal mikone
#va ahal tebghe adad ya alphabet miad moratab mikone

#reversde ham drim miad reverse mikone

#Mitonimk begim chijori moratab kon?
#bale ba tarife key

list.sort(key=str.lower)
#hamaro aval kochik kon bad inkaro anjsam bde
#ya  hata badan mitonim yek tabe bsazim va be onvane key bdim

#yek buil in function ham drim
sorted() #in vase hame bekar mire
#ini k ma migim bvaraye list




#---------------

#==========================================
#--------IF------------------------


#yani chi yani migim
#do no drim yeki if / yeki if-else
#dar har dosoorat 
#bebini python miad az bala be paeen mikhoone
#vaghty mirese be if dg bahs avaz mishe miad ye algorithmio donbal mikone

#algorithme if injorie ke
#mirese be if yek sharti dare age shart true bashe (yani doros bashe)
#yekio ejra mikone
#age na rad mikone
#khodemoooni: mige age injori bod inkaro kon age nabod ham velesh kon

#if else hala chie?
#mige age injori bod inkaro kon age nabood yekare dg ro kon


#sakhtaresh shabihe zire
#** do no drim yeki if / yeki if else

'''
if (shart ):
    gozare ro (dastoor) dar soorate true bodane shart ejra shavad
    
'''
#miad mige age shart bargharar bod kare paeeni ro kon
#age nabood rad kon


'''
if (shart):
    age true bood ino ejra kon
else:
    age false bod shart ghablie ino ejra kon
'''
#if else yechize ezafi dre:
#in frghesh ine ke mige ag shart bargharar bod inkaro kon , age nabood
#mese ghablie ve nakon balke yekare dg ro kon


#dar shart az com[parison] operators estefade mikonim
#== mosavi ast ya na?  =! mosavi nist ?  > bzoorgtar < kochiktr
#<= >= ...

#aval yek adad mizrim
a=4

if a==4:
    a=a+2

print(a)
    #
    #
    #
    #
    #
    #
#6 , choon didi a are 4 hast = shartemon true shod
#statement ro ejra krd ( dakhele fasele (tab))
    
#----------
a=5

if a==4:
    a=a+2

#birone halghe
print(a) #5 yni ejra nshode



#--------------

num=int(input('please insert your number:'))
if num>2:
    print('this number is more than 2')


#dar ife khali ag true nabod ( false) mipare
#kari ndre
#ama dar if else yek statement mizrim baraye false





num=int(input('please insert your number:'))

if num>10:
    print('this number is more than 10')
else:
    print('no sorry')
    
    
    
#if va if-else

#yechize dg darim be esme ELIF

if num>10:
    print('this number is more than 10')
else:
    print('no')
    

#------ age doros bood inkaro kon
#ag doros nabod dobare ye sharte dige ro besanj


if num>10:
    print('this number is more than 10')
elif num>5:
    print('more than5')
else:
    print('less than 5')
    

#--------------IF------------------------
if swhart:
    dastoor
    #aval if, bad shart bad donoghte
    #bad enter--> fasle bayad rayat shr
    #dastooremon ro mizrim
    #az dastor khstim biaym biron enter barmigrdim
#too shart az comparison operator estefade mikonim

a=50
if a==50:
print('ok')
#IndentationError: expected an indented block
a=50

if a==50:
    print('ok')
    #ta kojua??
    #tav vaghty dar in faslee gir oftade
    print('next')
    print(4)
    
       
print('hello') #asan kari b if ndre
#vaghty fasele hazf mishe dg if o ina dr kar nis
#mishe mamoli
a=50
if a==50:
    print('ok')
#out=ok

a=40
if a==50:
    print('ok')
#out= hichiiiiii

#choon dakhele shart true nshode
#yani jzovge shart nis
#hala ag bkhaym bgim onaee k too shrrt nistan felan kro konan
#else
a=40
if a==50:
    print('yes')
else:
    print('no')
    


#***else maid zire if va donoghte migire
#dastooresh miad yek fasele
a=40
if a==50:
    print('yes')
elif a==40:
    print('no')

#imagination: joloye if vaysadid vba migid
#koln dorahi dorost mikonid mese derakht
#while ya for
#halghe chie?
#yek shomarande dre k bas bgim chande ? masan 0 masan1
#starte shomarande
#miad yek end mizrim brash yani ta koja bshmor masan 10
#miad az 0 ta 10 : 0,1,2,3,4,5,6,7,8,9,10
#hey i=0 , i=1 bd i=2
#va dastoore paeen ro ejra mikone

for i in range(0,10):
    print('salam')
    
    
#for ke dastoore
#i yek shomarandas
#in ham yani dar in range
#range ham maid az start ta yeki monde be end misaze masalan 0,1,2,3,4,5,6,7,8,9 shod dah ta
#subject= i b ch drdi mikhor?
for i in range(0,10):
    print(i)
#0
#1
#2
#3
#4
#5
#6
#7
#8
#9

#javabe quiz

password=input('passeton chie:')
len_pass=len(password)
for i in range(0,len_pass):
    print('*')
#*
#*
#*
print(1)
print(2)
#1
#2
#chra 1 2
#choon ye settingi has bename /n
print(1,end='')
print(2,end='')
#12

for i in range(0,len_pass):
    print('*',end='')
    
#***

for i in range(0,len(input('passet chie:'))):
    print('*',end='')
    
for i in password:
    print('*',end='')
    #tooye password
#passwodrdemon chie? 356 
#khob mige fk kon yek reshtas
#baraye har I ee k dar password hasd
#yani 356 mitonimk bgim masalan 3 ta harfe
# yani 3 ta i 
#miad az 0,1,2

#or i in password=for i in range(0,len(password)):

#i chie???
name='ali'
#yek str hast
name[0] #a
name[1]#l
name[2]#i

for i in name:
    
#yani name cheghadre andazash? mige 3 ta element ali a l i
#i ro miad az 0 ta 3 0,1,2 
#i in name= i in range(0,len(name))

#b ezaye se ta chikar konm?
name[i] #NameError: name 'i' is not defined
i=0
name[i] #=name[0]=a

for i in name:
    name[i]
#mige baraye harchi element dar name hast i bzar rangesho
#darf name ali drim seta elemente a l i
#miad i ro az a,l,i mizre hey tekraer mikone ynichi
#yni mige i=a khate paeren ejra mishe
#bad mige i=l khate paeen ejra mishe
#i=i khate paeen ejra mishye
#maid biron

for i in name:
    print(i)
    
#aval mikhone mige yani baraye i haee k dar name hast
#name 3 ta hast yani i az 0,1,2 ejra konm
#i=0 mizre mige name[0]=a print mikone
#i=1 mizr emige name[1]=l
#i 
#ali

#----for------------
for i in name:
     print(i)  
     #str

     

#-------farghe in dota
for i in name:
    print(i)
 
for i in range(0,len(name)):
    print(i)
    
for i in range(0,len(name)):
    print(name[i])
    
#noketey payani
#i mitone ba estefade az len ya range adadi bshe in shomarande
#yni az yek adad ta yek adad dg hey i ro bzaare

#ya ag bgim i in name
#biad i ro hey bzare horof ha ya element haye daroone oon namer



#jalaseye bad========
#1- def ro yad midim va mirim soraghe
#madule ha
#numpy
#matplotlib

  
    
#----------farghe emal(apply) ya ejra (run)
a='ali'
a.upper()
#Out[15]: 'ALI'
#mige ejra krdm
print(a) #ali
#yanhi ma apply nmikone bishtare methodhaye str
#ejra mikone
#shoma baraye apply ye step dgh niaz drid
#asign
new_pass=a.upper()
oldlist=[1,2,3,4]
oldlist.append(5) #vaghty ejra krdm
#chizi be onvane Out[felan] nadad---> yani
#emal shode na ejra(tahvil)
newlist=oldlist.append(7)
#newlist=Nonetype

    
#--------------------------
#felan if o if-else ro bdoonid




#ghab;li baraye ejraye exeption
#ma mikhaym yek filter bzarim
#begim yeseri chiza anjam bde nade

#====================
#halgeh hast ya 
#mikhaym ye kario tekrar konim
#do no halghe --> yeki while
#for

while
for
#minevisim banafsh mishe yani dastoore


#while aal mige ye adad bzar baraye shomarandamon
#yechi bname shomarande drim k aksaran i mizrn
i=1
#shomarande yani mishmore
#az chan shoro kone az 1
#bad benevis while va jolosh sharte edameye halghe

while i<6:
    #statement (hey dor mizne)

    #while yani ta zamni ke
    #ta zamani ke chi???
    #in shart sahih bashad
    
#t zamani k i kochiktar az 6 hast
#man oon statmente ke fasele dre oon zir ro
#ejra mikonm mese ye halghe

#hey brmigarde aval check mikone
#hey mibine true e okey

#khob inja
#run nakonid !!!!!!!!!!!!!!!!!!!!!!!!!!
'''
i=1
while i<6:
    print('salam')
    
'''
#i ro yek mizre
#hey check mikone
#check mikone mige zire 6e ? are
#pas ejra mikone
#hey dobare
#dobare
#dobare
#va khob be in migan
#endless loop yek halghe bipayan
#tamom nmoishe

#rahi ndre ke az halghe kharej she

#mian migan yek chize jadi bzar k biad kharej she

i=1
while i<6:
    print('salam')
    i=i+1

#avalin bar= i yek has
#sharte i<6 true hast pas mire too  halghe
#print mikone salam ro
#bad miad i ro +1 mikone
#i emon shod chan ? 2
#dobare check mikone
#i<6 bale
#print mikone salam ro
#i ro ezafe mikone +1 = i emon shod3
#.....
#i=5
#i<6 bale
#print mikone salam ro
#i ro mikone +1 = i=6
#hala miad mige i<6? hast? naaaa
#pas ejra nmikone va az halghe miad birooon

i=1
while i<6:
    print('salam')
    i=i+1



#khoroji:
    #salam
    #salam
    #salam
    #salam
    #salam
    

#sakhtare kolie while ?

#aval yek shomarande mizarim
#minevisim while
#badesh shart mzirim behehs migan  sharte khoroj az halghe
#yani ta vaghty true has edame bde
#dakhelesh uyek statement has k ejra mishe
#yek  i+.. ya har calculationi mizrim ke
#ezafe kone be I ta betonim az halghe brim biron
#behesh migan khoroj az halghe





#------------------FOR-------------
#for miad mige sade tar mikon m kareto
#hamino sade bnvis

#benevis baraye felan ta felan yani
#start ta end ye kario man hey tekrar konm
'''
for (shart):
    statement ( dakehle halghe loop)
    '''
    
    #frgh ine ke dakhele shart shoma miayn
    #start o endi k too while mziashtino mizrim

#aksaran mian az tabeye dakhelie range estefade mikonim


a=range(0,5)

range(0,5)
#in adad nis motyeghayer nis yek range e
#beyne 0 ta 5

for i in range(0,5):
    print('salam')
    
    #mige ma yek range drim az 0 ta 5 (khode panj hesab ni)
    #0,1,2,3,4,5
    
    #mige done done bia i ro yebnar 0 bzar yebar 1 yebar 2....
    #va hey ejra kon
    
    
#be kalame sade
#az 0 ta 5 = 0,1,2,3,4 (5 BAR) in kare paeeno bokon


for i in range(0,5):
    print('salam')
    



for i in range(0,10):
    print('ali')
    
    
    
    
    
    
    
#=========================================================
#=========================================================
#=========================================================
#=========================================================
#=========================================================
#=========================================================
#==================L6=====================================
#=========================================================
#=========================================================
#=========================================================
#=========================================================
#=========================================================

Hatman aydemon nare break pass , ....

#===========DEF============Function==============
for i in range(0,10):
    print(i)



for i in range(0,10):
    if i==4:
        break
    print(i)


for i in range(0,10):
    if i==4:
        pass
    print(i)



for i in range(0,10):
    if i==4:
        continue
    print(i)


a=int(input('senetoon cheghadre?'))
if a>99:
    raise TypeError("NO your age is not ok")
else:
    b=a+10
    c=2000+b
    print(f'you money can get back in the year of {c}')
    
    
raise SyntaxError('dont forget to use something else')





#yek tabe vorodi dre calculation khooroji(optional)
    
    
#avalin ghesmta: tarife tabe

#aval def bad esme tabe bad parantez toye parantez vorodi ha
#esme vorodi
#donoghte
#yek tab o fasele

def first(input1):

#chanta vorodi

def first(input1,input2):
   
    #har esmi
    
def first(a,b):
    a+b
    if
    for
    a.append()
    
#age khoroji ndshte bashe ?


def jam(a,b):
    c=a+b
    
#tabe ro run mikonim fght save mishe ejra nmishe
#ta vaghty sedash nznim hich etefaghi nmiofte

#seda zadan= fasrakhanie tabe


jam# esme tabe

#chie? tabe --> ()

jam() #vaghty vorodi ndre

#chon mesale ma vorodi dre, vorodi haro bayad tooye parantez bznim
#seda zadan bad az tarife tabe bashed


jam(4,5)

#khoroji dad ? na
#chika rkrd?
#a ro gozasht 4 , b ro gozasht 5 
#c ro hesab krd
#haminnn

#too variable ha ham chizi b onvane C vojod ndre

#avalin 

global
local
#har chizi dakhele tabe shoma tarif mikopnid birone tabe
#vojopde khareji ndre

#magar inke poshtesh bnvisid global

#khoroji chikar konim?
#2 noe
#yeki print vase tamasha
#yeki return baragrdone

def jam(a,b):
    c=a+b
    print(c)


jam(4,5) #9
#c ro save nkrd chon harchi dakhele tabe local has na global
#ag bekhaym brgrdone yani khorji dshte bashe chi?


def jam(a,b):
    c=a+b
    return c

#avalin nokte: tabe vaghty b return brese baghiaro dg nmikhone

#2- return yani jayee k farakhani ya sedash zadim miad mide bma


jam(4,5)
#9


#tabe ro fhmidim
#ychizi class
#vali bdonid class tashkil shode az yekseri tabe + yekseri adade sabet

#===================


#==========class=========================
def bank(name,balance):
    print('hi',name,' your balance is',balance)
    
    
bank('ali',2000)



def bank(name,balance,deposit):
    total=balance+deposit
    print('your balance is',total)
    
bank('ali',2000,40)
    







def x(a):
    return a*2
x(2)

x = lambda a: a*2
x(2)



class bank:
    x=5
    
a1=bank()
a1.x


    


class bank:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def welcome(self):
        print('khosh amadid',self.name)

a1=bank() #TypeError: bank.__init__() missing 2 required positional arguments: 'name' and 'age'

a1=bank('ali',24)
        
a1.name
a1.age

a1.welcome()


class bank:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def welcome(abc):
        print('khosh amadid',abc.name)
        
a=bank('ali',24)  
a.name
a.age
a.welcome()




class bank:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        
        
    def information(self):
        print('Hi this is ATM setting and you can have name, balance')
        print('also you have vam , date and you can use some functions')
        print('like balancee() and deposit() and getting_cash(), or vam()')
        
    def balancee(self):
        print('Your balance is: ',self.balance)
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        print('Your money are deposited')
        print('Your current balance is:',self.balance)

    def getting_cash(self,getting):
        self.balance=self.balance-getting
        print('your money getting you in cash ')
        print('Your current balance is:',self.balance)
        
        
    def vam(self,vam,vam_date):
        self.balance=self.balance + vam
        self.date=vam_date
        self.vam=vam
        print('the bahre is 5% each month')
        
    def bedehi(self,now):
        dif=now-self.date
        bedehi=(dif*1.05)*self.vam
        print('you must pay',bedehi,' as soon as possible')

    def pardakht(self,bedehi):
        self.balance=self.balance-bedehi
        self.vam=self.vam-bedehi
        
#hala if o else o inaro biar vasaat


a=bank('ali pilehvar meibody',50)

a.name       
a.balance       

a.balancee()
a.deposit(40)


a.balancee()


a.getting_cash(40)

a.balancee()

a.vam(500,2)

a.balancee()


a.bedehi(10)

a.balancee()

a.information()



class shobe(bank):
  pass

class shobe(bank):
  def __init__(self, name, initial_balance):
    shobe.__init__(self, name, initial_balance)



class shome(bank):
    def __init__(self,name, initial_balance):
        super().__init__(name, initial_balance)
    
    

class shome(bank):
    def __init__(self,name, initial_balance):
        super().__init__(name, initial_balance)
        self.graduationyear = 2019
        

class shome(bank):
    def __init__(self,name, initial_balance):
        super().__init__(name, initial_balance)
        self.graduationyear = 2019
        
        
class shome(bank):
    def __init__(self,name, initial_balance,vam):
        super().__init__(name, initial_balance)
        self.vam = vam
        
        
class shome(bank):
    def __init__(self,name, initial_balance,vam):
        super().__init__(name, initial_balance)
        self.vam = vam
        
        
    def welcome(self):
        print("Welcome", self.name,'with', self.initial_balance, "to the class of vam with ", self.vam)
        
        
        






***
****
*****


#madule, ketabkhone chie, 
#@ketabkhone : yani yek file i has ke koli tabe dre 100 ta tabe dre
#shayad 100 ta adade sabet dre masalan pi 
#va shmoma kafie sedash konid varedesh konid (import)

#bejaye neveshtane 100 khat kod fght az tabe hash estefade konid

#file new

#yek madule neveshtim


#no madule named 'numoy''


#berid internet ino search konid

#pip numpy

#pip esme madule


#searech konid va brid site e pipy
#oon paeene esmesh
#copy konid

#ke aksaRAN INJORIE 
#pip install numpy




#copy

#koja paste koniM?

#anaconda omd chanta mohit sakht vae ma
#avalish base(root) bood
#brid environmente jadid bsazid

#az styart brid roosh

#hgar mohit mitone vase khodesh package bgire

#ba chi ? powershell


#dar strart search konim powershell ( esme mohit)

#baz mishe

#toosh copy paste ro anjam midim va enter




#====================================

'''
vorodi: 
    az tabeye input()
    open yek file open()
    variable haro  bzrim assign
    def(vorodi)

body(calculation):
    mohasebate amalgarha + - * 
    traine hoshe masnooe
    preprocessign amade sazi data
    predict kardan
    if, if else, for , while
    
khoroji:
    print--> fgh chap mikone bma khoroji nmide estefade konim fght nshon mide
    returne def --> khoroji bde bebarim use konim
    savesh konim --> too folderamon
    plot ( rasm she)


#pas harmoghe khastim code bznim bayad in structuremon bashe

#tooo har marhale che konim?
#------vorodi input----
#too vorodi python buil in haro daryabid input() open()
#variable ha --> type ha mohem str,int ....
#badesh bayad rooye vorodi taghirati bdim shayad
#casting --> type()  int(input('adad bde:'))

#badesh miad vasate kar , hala ghrare rooye vorodimon
#raw nist ( kham nis roosh rpeprocess krdim amade krdimesh)
#ag mikhaym brim toosh ( iter bznim , peymayesh (bazresi))--> for
#agar bekhaym screening konim, gharbalgari yani biaym
#jolo dataharo bgirim shart bzrim mesle yek gharbalgar
#biad yeseri vorodi haro joda kone---> if , if_else
#if fght b onae k true bodn dastor mdiad
#if else miomd b onae ham ke sharteshon false bod ham dastoor midad

#age khastim yekchizio tekrar konim 'tekrar'__repeat-->loop
#for, while
#while vase zamanie k shartemon tahesho ndonim 
#az inja(start) ta vaghty ke shartemon true bashe yekkar ro hey tekrar kon
#for--> az start ta end inkaro anjam bde

#operator hamon + - / * **
#(parantez) > **> * > / > + > -
#a*b+2--> miad aval a*b mikone bad +2
#chikiar konimolaviat beshkonim--> parantez
#a*(b+2)
#tooye while ya if--> baraye shartemon az comparison-->
#== , =! , > , < , <= >=,

#khorojimone----
#baz mitronim yekseri taghirat bdim
#casting
#1-hichi fght biad print she-->fght in samte rast consule namayesh mishe
#vase chekari kolan bekar mire? baraye check krdn
#return--> yani biad meghdaro be ma bde baraye useeee ( estefade)





#--------chan no neveshtane in structure ro drim (vorodi,calculation,khoroji)


#pseducode(shebhe code) ta alan harkari kmikrdid

a=input()
c=a+b
if
for....
print(c)


#formal nis fght vae tamrino yad girie

#chikar konim?
#biaymaz class ya def estefade konim


#def-------
yek kaerkhone ro dar nazar bgirid ye esm dre
daghighan mese bala vorodi migire calculation mikone too body
va khoroji mide


def name(input):
    body (calculation)
    return output

#-------------------
*******nasihate doostane:
    ta alan shoma 50% e python ro yad grftid ama baghiash
    depend on your practice
    
    
'''

#structure def(function)
#1-tarif
#2-farakhani

#----------------tarif krdne tabe
#L7
#yek vorodi
def esmetabe( vorodiha):
    dastoorat
    
#do vorodi chi?
def jam(a,b):
    dastooor
    
#har esmi msihe gozasht? bale

#khoroji chi mide?


def jam(a,b):
    c=a+b
    
def calculator(num1,num2,amalgar):
    
    if amalgar=='+':
        result=num1+num2
    if amalgar=='-':
        result=num1-num2
    if amalgar=='*':
        result=num1*num2
    if amalgar=='/':
        result=num1/num2
    #ta inja result hesab mishe bar hasbe amalgari k dadim

    return result




import firstmadule as f

#yani mokhafafesh konim
f.pi
f.zarb(3,4)




#pas fhmidim madule chie

#ketabkhone chie??
#yek foldere mese yek ketabkhoone
#por az maduleeeeeee koli madule dre
#-- har madule kioly function, class o .. dre


#sade trin madule

import math
#ag import shod ok ok ag na harfaye akhare jalase ro fgosdh bdid
#masalan radikal bgirm
#** ....

math.sqrt(4) #Out[48]: 2.0
#dar halate adi
#bayad yek functionbsazim
def sin(a):
    #dfonbale ye ssin ro bsazim
    #p hro bznim
    #n bgirim
    #radiano tbdilk konim
    #bargardonim
    s=43*a
    return s

#bjaye sakhte in hame def
#rahat yeki bode 
#math ro skhte
#yek tabe bename sin sakhte
#kafie aval esme ketabkhone bad oon tabe ro seda bznim

math.sin(30)



math.pow(2,4) #Out[50]: 16.0
#constant adade sabet

#k dfg niazi b parantez



math.e

math.pi



#in shdo math
#cmath ham drim k ykm pishrafte tare

import cmath
#arc cosin hyperbolic o ina ham dre


math.floor(4.15)


#----------------------------

#ketabkhone haye default k dre aksaran
#math
#cmath
#random
#statistic
#date


import #esmeshon



#hala ketabkhone haye maroof k ghrare kar konim
import numpy #bartaye moahsebat
import matplotlib #baraye rasm
import pandas #baraye kar ba dade preprocess
import sklearn #baraye hooshe masnoee

#inaro ndre default bayad brim brizim


#yadetone yekseri environment dashtim???
#rooot --> khey7lia hanoz roo root drn run mikonan

#anacvonda

#******
#-----------
#search name pip


#avalin sait ba esme pypi
#copy konid
#paste dar powershell


#har mohit dota chiz dre
#1-spyder
#2-powershel

#vaghty mikham vared shyam naizi b abaz krdne anaconda nis
#hamin chasp paeen start 
#havasam bashe ke ()


#baraye jalase dg
import math
import cmath
import random
import statistics



import numpy


#** ehtemalkan 4 taye balaro drid niazi b pip o install nis
#ama baraye numpy bayad search bznid

#=====================================================================
#=====================================================================
#=====================================================================
#=====================================================================
#-----------------baraye jalasate bad-----------------------

#1- import haro check konid:
    math,cmath,random,statistics inaro ehtemalan drid

#2-brid numpy ro import konid ag nadarid ya harkodom az balaharo ndrid 
#search konid pip esme library, bad avalin sait
#oon tike ke neveshte pip install numpy ro copy konid


#oon mohiti ke hamishe run mikonid spyder(esme mohit)
#search konid anaconda powershell , hatman too parantezesh esme
#mohiti bashe ke hamishe spyder ro run mikonid
#bznid yek safe siah miare
#vaysid load she va bad paste konid pip install ro 
#enter ro bznid
#vaysid download she va install bshe
#badesh biad import numpy bznid va bbinid ovord ya na


#import bekhaym konim

import #esme ketabkhone


import firstmadule.py

#ehtemalan mige peydash nkrdm
chikar konim?
#bayad to path bashe


import firstmadule

#.py niaz nis

#yek no  raveshe import hast

#harja kari ba tabe haye dakhele in ketabkhone drim madule drim
#esmesho seda bznim
firstmadule.pi #Out[4]: 3.14
#pi yek adade , tabe nis pas niazi bn parantez ndre

firstmadule.jam(4,5) #Out[5]: 9

#yek raveshe import bod
#raveshe dovom mokhafafe

import firstmadule as f
#yaNI ESME MADULE ro bnvis as bzar jolosh mokhafaf
#har mokhafafi

#hey nanevuisiam firstmadule

f.pi
#pas mitonm dstresi dashte basham ba dad

f.jam(23,50) #Out[9]: 73


f.taghsim(4,8) #Out[11]: 0.5
f.taghsim(5,0) #change the second


#porozhe





#=========================================================
#=========================================================
#=========================================================
#=========================================================
#=========================================================
#=========================================================
#==================L7=====================================
#=========================================================
#=========================================================
#=========================================================
#=========================================================
#=========================================================


#chjanta madule maroof drim

math
cmath
random
request


#hyarkodom yek kari

import math
import math as m
#age erro ndad yani daratesh
#age error dad baayd brim install konim

import cmath

import random
import request


#yeseri ketabkhone harfo defau;lf dare python ama age nadasht chi?





#mirim esmesho search miznim


#numpy
#matplotlib
#pandas

import numpy

import math
#delta=b2-4ac aval hesab mikonim
#bad migim age ---(esme age omd yani if mikhad)
def root(a,b,c):
    #step hae k ye ensan anjam mide
    delta=b**2-4*a*c #aval delta hesab mikonim
    
    #age delta mosbat bood
    #age delta manfi bood
    #ag delta sef bod
    
    if delta>0:
        r1=(-b+math.sqrt(delta))/(2*a)
        r2=(-b-math.sqrt(delta))/(2*a)
        
        return r1,r2

    if delta==0:
        r=-b/(2*a)
        return r
    
    if delta<0:
        
        print('there is no answer')
        #return None
    #ye karee dg
    
    
    
    
#======

#===========================================
#ina ketabkhone haye sade bodn randomo , 
#math , .....


import statistics
#baraye amar hast

#mean() miangin
#median()  #adade vasat

#median_high() #adade vasato begir beyne ono bishtrrin adade vasate

#median_low()

#mode()  #

#variance()
#pvariance()

#pstdev()
#stdev() enheraf az meyar


statistics.mean()

#iterable migire --> yani list migire 
#iterable--> harchi ke lemeent toosh dasht

a=[1, 3, 5, 7, 9, 11, 13]

print(statistics.mean(a)) #7


#biaym besazim bbinim chijori sakhtan

def gamlab_mean(mylist):

    numbers=len(mylist)
    summ=0
    for i in mylist:
        summ=summ+i
    mean=summ/numbers
    return int(mean)

print(gamlab_mean(a)) #7
print(statistics.mean(a)) #7




a=[1, 3, 5, 7, 9, 11, 13]
print(statistics.median(a)) #7


a=[1, 3, 5, 7,8, 9, 11, 13]
print(statistics.median(a)) #7.5


a=[1, 3, 5, 7, 9, 11, 13]

print(statistics.median_high(a)) #7




a=[1,1,2,4,5,7,7,7,8,9,11]
print(statistics.mode(a)) #7


a=[1,1,1,1,1,1,1,2,4,5,7,7,8,9,11]
print(statistics.mode(a)) #1


#harchi in adad bzoorgtr yani distribution pahn tar tare yani dade ha door tar az mianginan

statistics.stdev(a) #Out[54]: 3.5456210417116734
statistics.variance(a) #Out[55]: 12.571428571428571
math.sqrt(12.571428571428571)

#yani  variance = stdev**2

#khob in dota vase ine bbinim cheghad dade ha paeralkandan

#chra variance estefade mishe ?

#parakandegio bishtr nshon mide


#==================
#keteabkhoneye numpy-----------

#--------------NUMPY------------
#bargshtim b list
#list chi bod?
#kolan variabl ha chanta kar bas bahash konim injori taghsiemsh konid

#1-assign ( megdhardehi) 2-access element (index) 3-iter (peymayesh) 4-method

#list chi bod?
#asign
#2 rah dre
#rahe avalo []
a=[4,5,6,7,7]
b=['user','ali','new']
c=[4,'user',True]
#rahe dovom estefade aaz built in fucntion
a=list((1,2,3)) #2 ta parantez

#acces chi bod ? yani mikham b yek elemenet ( onsoi , joz) az in list dastam brse
#yani bekeshamesh biron ya taghiresh bdm ya hazfehs konim
#esme on listo seda bzn [ ] indexesh **havaset basahe index az 0 shroo mishe na az 1111111
a=[4,5,6,7,7]

#masalna dovomin elemente liste a
#dovomin yani indexe 1
a[1]

#yani python maid jaye kole a[1] oon joz ro mizare
#khob mitonim savehs konim 
b=a[1]


#loop--ityer----peymayesh
a=[4,5,6,7,7]
for i in a:
    print(i+1)


#mikhaym yek list bnsazim done done elemente a ro +1 kone brize
#rtoo liste jadid
  
a=[4,5,6,7,7]
for i in a:
    b.append(i+1)

#in error mide
#AttributeError: 'NoneType' object has no attribute 'append'

a=[4,5,6,7,7]
for i in a:
    k.append(i+1)
#NameError: name 'k' is not defined
#ras mige miad b k ezafe mikone yekchizio , k chie ?


k=[] #yewwk liste khali
a=[4,5,6,7,7]
for i in a:
    k.append(i+1)
print(k) #[5, 6, 7, 8, 8]

#pomadan goftan list sariii nist , biaym yek chzii bsazim kheyli sari bashe
#50 nbarabar sariiiii tarrrr
#numpyyyyyy
#hamchenin list fght yek bodie yani matriso ch bdonm matris haye chan bodi nmisyhe sakht

a=list((1,2,3,4))


#------------------------------------
#vahkleye importe numpy
import numpy

#agar zad numpy mdule is not fined --> bayad bri too environmenti ke
#spyder nasb hast , powershelesho bzni bnvsii install pip numpy 
#bbndi abrname ro dobare baz koni hala bzn

#ravesh haye dg ye import
#kolan se raveshe
import numpy


#vbase dastresi b yek tabe bayad dot mizdi m va chon tabe hast parantez dre


#aslan numpy baraye ine ke yechizi mesle list bsazi tahvil bde
#ba yek tabe ee benam array



numpy.array((1,2,3,4,5)) #ino k mizani maid kolesho vrmidre ye array mizare

#ma baayd savesh konim

#assign---------------------
new1=numpy.array((1,2,3,4,5))
new2=numpy.array([1,2,3,4,5])

#ag naszarim  parantz cvhi?

false_array=numpy.array(1,2,3,4,5)
#TypeError: array() takes from 1 to 2 positional arguments but 5 were given

#mige nahayatt yeki dota bgire chra panjta dadi?

#pas mesle tabe neveshtan ma taeen mikrdim chnta voprodi bgire
#ina ham too numpy taeen krdn chanta bgrie

#se raveshe assign---------
new1=numpy.array((1,2,3,4,5))
new2=numpy.array([1,2,3,4,5])
name_list=[1,2,3,4,5] #ya set, touple
new3=numpy.array(name_list)


#typesh chie ? masan ghadim int dshtim floast 

type(new1) #Out[31]: numpy.ndarray


#sakhte hey bnvisam numpy --> baraye hame skahjte
#pas avale barnamatonm mokhafaf import konid
import numpy as np

a=np.array((1,2,3,4))


#pas aasign ro yad grfim
#type ham yad grdim
#dimention chie ? mage nagtfoti matrisma msihe sakht va va va
#bahse dimention mishe

#chan no bod darim بعد

#0-D array (sefr bodi)--> hamoon adade khodemone---------------
#hamon numbere khodmone ama type e numpy
arr=np.array(58)
#frghesh ba adad ?
numb=58
#boro bala samte rast moghayese kon

print(type(numb),type(arr)) #<class 'int'> <class 'numpy.ndarray'>

#fght khastam bgm bdoni, ma estefade ye ziadi nmikonm azash


#mohmtrin ghesmat injas
#1-D array ( yek bodi)--> hamon liste
#bejaye ye adad mesle section ghabli bayad chanta bnvisi

arr=np.array(58,59,60) #--> bayad dota aprante basheeeeeeeee*****
arr=np.array((58,59,60)) #ya arr=np.array([58,59,60])



#in shod 
#ma list drim chra akhe ino misazim? chra hamon [58,59,60]
#yekish ine ke sarii tare 50 brabar sari tar hast 


#2-D (do bodi)--> matrissss
#yani mikham sotono radif dashte bashe fght yek soton nabashe

#yek parantez ke defaulte
#yek beraket bzanid
#har beraketi k tooye in beraket miznid yekkk radife

arr=np.array([[1,2,3],[4,5,6]])

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])

arr=np.array([[1,2,3,6],[4,5,6,8],[7,8,9,11]])

#arr=np.array([[1,2,3],[4,5,6,8],[7,8,9,11]]) bja adad list mzire

#dast negah dar

#dota method yadet bdm,

#esme oon araye ro bzar dot bzn 
arr.ndim #in dimention (bod) ro mide  1

#size======
#oon bala samte rast 
#bad az type nvshte size yani chi
arr=np.array([58,59,60])

#(3,)
#yani man y soton drm 3 ta khone tooshe


arr=np.array([[1,2],[4,5],[7,8]])

#(3,2) #yani aval dota adadde yani man do boid9iam
# avalie tedade radifame dovomie tedade soton

#yani se ta beraket hast k too hrkodom dota adad hast


#on bala rast type dare o size
print('our type is : ' ,type(arr))
print('our dimention is : ' ,arr.ndim)
print('our size(shape) is : ' ,arr.shape)

#3D----------------


#yek bodi doros emiznim roosh yek sotyon nshon mdie
#ama yadet bashe yek radifeeee

#vaghty too 2d chan ta mizrim kenare ham mishee radif ha roye ham

a1=np.array([1,2,3,4])

a2=np.array([[1,2,3,4],[5,6,7,8]])

#se bodi yanjhi bia in dobod ro

a1_1=np.array([1,2])
a1_2=np.array([3,4])


a2_1=np.array([[1,2],[3,4]])
a2_2=np.array([[5,6],[7,8]])


a3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])


#------------assign ro yad grfim
#ndim , type, shape ham yad grfim 

#access element----------------
arr=np.array([1,2,3,4])
#access yani ye  element ro az delesh bkshm bironn

#masalan dovomioo
#mesle list
#esmo bnvis ba ye beraket toye beraket index
#***** az 0 shoro mishe index haaaaaaa

print(arr[1]) #2

arr=np.array(['ali','vahid','hamid','reza'])
print(arr[1]) #vahid



#ino k balad bodim too list yademon dadi

#bia sakht tar vasat drm--> do bodi chi>

arr=np.array([[1,2],[3,4]])

#aval b zabone farsi bego chie bad mashinish kon

#masalan adade 4 elemente mikhaymesh chi migim farsi
#migim aval migim radife chandom abd soton


#chon haminjori bod dg dobodi miomd yek bodi haro besorate radif radif roo ham mizasht

#pas chi migim radife 1 soton1
arr[1,1] #Out[64]: 4


arr=np.array([[1,2,3],[4,5,6]])
#adade 5 ro mikhaym

#radife chand , sotone chand ???
#hamino bnvisi
#*** radif haro az 1 nshmor az 0 bshmor indexxxx

arr[1,1] #Out[67]: 5

#masalan 6
#radife 1 sotone 2
arr[1,2] #Out[68]: 6


#------
a3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

#age adade 7 ro bekhaym chibznim?

#aval bas begi kodom safe bad mese ghabli
#bad begi kodomr adif kodom soton



#overall: kodom safe, kodom radif , kodom sotooon

#@7 kojas
#too safeye 1 e , radife 1 e , sotone 0

#esmo minvisi jolosh
a3[1,1,0] #Out[70]: 7



#------slice
#too gahbli goftim ye element bekeshim biuron
#ag chanta bkhaym bkshim chi ? slicing

#sade tarin-->1 D

arr=np.array([1,2,3,4,5])
#mikham az 2,3,4 ro vrdare
#yani indexe 1,2,3 
#mishe az 1 ta 4 **5omio hesab nmikone
arr[1:4] #Out[74]: array([2, 3, 4])


arr[:4] #yani poshte do noghte chizi nzri yani az aval
arr[2:] # ag bad az donoghte chizi nzre yani az felan(2) ta akahgr
arr[1:5:2] #yani az indexe 1 ta 5 2 ta 2 ta 

arr[::2] #yani az aval ta akahgr dota dota vrdar







#2D-------
arr=np.array([[1,2,3],[4,5,6]])
#ye radif 1,2,3 bala dre ye radif 4,5,6 paeen
#mikham4 o 5 ro bde

arr[a,b]

#inja a o b dasht
#a shomare khone ye radifemon bod 0 yani radif bala 1 yani radif paeen
#b ham shomare khoneye sotoon
arr[1,0:2]

#masan 2,3 ro mikhaym

arr[0,1:]


#--
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])





#--------------------
#numpy assign , access , slice ro yad grftiimm
#brid + - konid bbinid mishe ?


#inaro emtehan konid
#aya in chizi pas mide yani mitonim savesh konim too ye variable e dg ?
#ya inke fght emal mishe rooye arr 

arr.copy()
arr.view()
np.concatenate()
np.stack()
np.vstack()
np.dstack()
np.array_split()
np.sort()
np.where()
np.searchsorted()
   
#********

import numpy as np

#bahash array miskahtim --> list
#assign
#0D
a=np.array((2))
#1D
a=np.array([1,2,3,4,5])

#2D
a=np.array([[1,2,3,4],[4,5,6,7]])


#chia dasht?
print(type(a)) #<class 'numpy.ndarray'>

print(a.ndim) #2 number of dimention

print(a.size) #tedade elementa yani chnta toshe 8

print(a.shape) #(2, 4)   #2 ta radif , 4 ta soton 

#hmishe vaal radife bad soton --> 2D 
#too 3d ==> avalk laye bad radif bad soton

#access -- []
#*** index az 0 shoro mishe az alan adsat kon bgo radife 0om

a=np.array([1,2,3,4,5])
a[0] #avali 1
a[4] #5




a=np.array([[1,2,3,4],[4,5,6,7]])
#kodom radif kodom soton [radif,soton]
#adade 4 kodome ? radifew 0 om , sotone 3 vom
a[0,3] #Out[10]: 4

#slicing -- [:] yanio chnta access
a=np.array([1,2,3,4,5])
a[0:2] #Out[13]: array([1, 2])
a[1:4] #Out[14]: array([2, 3, 4])


a=np.array([[1,2,3,4],[4,5,6,7]])
#[chanta radif,chanta sotonesh]
a[0:2,1:4]



#another way to assign 
#ag khastrim bgim az 1 ta 10 ro baramon bsaz chtor?



a=np.arange(10)
print(a) #[0 1 2 3 4 5 6 7 8 9] 
#vaghty y adad mziri mire az 0 ta yeki monde b on adado array mikone

#np.arange(start,end,step) az chant ta chant , chanta chanta brer(optional)

a=np.arange(0,6)
print(a) #[0 1 2 3 4 5]  end ro dr bar nmigire

a=np.arange(0,6,2)
print(a) #[0 2 4]

#ina k hamash 1 bodi bod ? chijori 2 bodish konim

#masaslan
a=np.arange(0,6)
print(a) #0,1,2,3,4,5
#mikham 0,1,2 bala bashe , 3,4,5 paeen
#aval bayad hesab koni --> 
#array jadid chanta radif dre chnta soton

#yani 2 ta radif dre va 3 ta soton ==> (2,3)

#esme oon araye ee k mikhgay reshape esh koni ro seda mzini

a.reshape(2,3)
#zadam roo a taghir nkrd ??
#dar asl in emal nmikone balke pas mide

b=a.reshape(2,3)

#ya ag bkhaym shabihe emal nbashe yani zarf kasif nakoni
a=a.reshape(2,3)

#EMAL CHI BOD YADAM RF
a=list((1,2,3,4))
a.append(5)
print(a) #[1, 2, 3, 4, 5]
#ma chizi zakhire nkrdim k too zrfi chra injori shod ?
#a taghir krd chra ?? chon in tabe emal mishe pas nmide

#ag zadi out dad ya too zrf rikh yani emal mishe
b=a.append(5)
#b=Nonetype ---> yani emal mishe chizi pas nmide


#change------
#kafie access konim va taghirewsh bdim
arr = np.array([1, 2, 3, 4, 5])
arr[0]=42 #(42,2,3,4,5)





#noktye ye dg copy view
#ama 
arr = np.array([1, 2, 3, 4, 5])
arr2=arr
arr[0]=42
print(arr) #[42  2  3  4  5]
print(arr2) #[42  2  3  4  5]
#vaghty mosavi mziri har taghiri emal bshe roo onytekiam mishe

arr = np.array([1, 2, 3, 4, 5])
arr2=arr.view()
arr[0]=42
print(arr) #[42  2  3  4  5]
print(arr2)


#agar nmikhaymmm taghgirat emal bshe
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0]=42
print(arr) #[42  2  3  4  5]
print(x) #[1 2 3 4 5]
#yani .copy() miad ye copy migirer va hgarkari ba aslie bokoni kari ndre

#yechi dg dare bename -1 reshape
a=np.array([1,2,3,4,5,6])
#mikham bgm boro 2 ta radif kon
#hosele ndrm beshmorm bbinm dota radif chnta soton mishe
#fghht mikham bgm do radifash kon
#rahakr= n-1
b=a.reshape(2,-1)
#ya barax
c=a.reshape(-1,2)



#iterating and loop i access in the ndrray
#agha mikham bbinm for chie --> bazrresi --> peymayesh

a=np.array([1,2,3,4,5])

for i in a:
    print(i)
#1
#2
#3
#4
#5
#yani mire tooye array done done ro mikeshe biron
#hala harkari dri anjam bdi ro too bopdy bnvis

#masan mikham bre chek kone hrkodom 4 hasto bokpone 8

a=np.array([1,2,3,4,5])


a=np.array([1,6,6,3,4])

for i in a:
    if i==4:
        print(i)
        
        
        
        
print(a) #[1 2 3 4 8]


#rahe hal printe
a=np.array([1,2,3,4,5])

for i in a:
    if i==4:
        i=8

a=np.array([1,2,3,4,5])

for i in a:
    if i==4:
        i=8
        
#2 ta rahkar
a=np.array([1,2,3,4,5])

for i in a:
    if i==4:
        a[i-1]=8
     
        
     
a=np.array([1,2,6,4,5])

#az rahe dovom





for i in range(0,len(a)):
    if a[i]==4:
        a[i]=8

print(a) #[1 2 6 8 5]

#shomarande ba element overlapp nakone



arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)
 
#baraye do bodi ha injori access mikonim

for x in arr:
  for y in x:
    print(y)


#hala ag bkhaym bgim random bsaz bramon chi?
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

#goftm 1 bodi dorose mizni rosh sotonie yama yek rradife
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2),axis=0)
print(arr)

#axis=0 hamon defaulte 


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2),axis=1)
print(arr)
#AxisError: axis 1 is out of bounds for array of dimension 1


#---baraye dobodi ha
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=0)

print(arr)
#concat k mizni dota ardif ro dar toole ham michasbone
#man mikham roye ham bndazatesh
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)

print(arr)


#ravesh haye dg
#axis== dar toole ham ya na

#baraye 1 bodiconcat nmitone kari kone ama alan mitone

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=0)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)





#---split

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

#miad yek array ro tabdil mikone be chand array

#hala bkhay6n dastresi peyda konid
#soal bporsid===> chandomin array ro mikham?
#masaalan set atagsim krd, kodomo mikham? avalio ? dovomip?

newarr[0] #Out[69]: array([1, 2])





#===========
#yadfetone man for zdm k yechizio masalan peytda konm?
#--where
arr = np.array([1344, 2434, 34, 34432, 534, 423, 41])

x = np.where(arr == 1344)

print(x) #(array([0], dtype=int64),)
#yani mige injdexe 0 adadi k mikhay


arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x) #(array([3, 5, 6], dtype=int64),)

#yek arrayi mide
#toosh index ro mige k kodom index ha
#oon chizi k madn made nazarame ro dre


#mitonid sharto avaz konid --> masalan kodom zoje
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x) #(array([1, 3, 5, 7], dtype=int64),)



#=============
#sort
#ke miad 
#az 0 - .... 
#az A - Z a - z
#moratab

arr = np.array([3, 2, 0, 1])
np.sort(arr)
#pas mdie yani bas zakhire konim sort ro


print(np.sort(arr))
#[0 1 2 3]




arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr)) #['apple' 'banana' 'cherry']



arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))


#filter
#yani bgim yseriaro bardar ysreia ro brndre

arr = np.array([41, 42, 43, 44])

#baayd ye x i bsazim
#xze toosh chie? True False 
#badan migim treu haro brdar falsarpo bdnaz dor

x = [True, False, True, False]

#structure:
newarr = arr[x]

print(newarr) #[41 43]


#yani ma bshinim done done bgim kodoma true ? na shart bzar
#masalan mikhay bgi zoj haro negah dar

arr = np.array([1, 2, 3, 4, 5, 6, 7])
#ag tolani bashe cdhi?

filter_arr=[]

for element in arr:
    if element%2==0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
        
print(filter_arr)  
#[False, True, False, True, False, True, False]
#structure:
    #new_array= hamon_array[liste filterr]
    
newarr = arr[filter_arr]
print(newarr)
#[2 4 6]




#arrange ro?
#ag kkhastim random bsazim chi?
#yanji yek array bsazim toosho az wadade random por konim
#flash back <----
import random
x=random.random()
print(x)
#yeki adady beyne 0 ta 1 reandom mide

#ag mikhasam baze bdm
x=random.randint(1,8)


#numpyu mige bia man hamino drm
#bja yek adad yek arraye ro por mikonmn barat az adade random


x=np.random.rand()
print(x)
#in hamoone


x=np.random.randint(100)
print(x)


#hala k frghi nkrd?
#size

#yani y array mikhay bsaZI BBIN CHANTA RADIF CHNTA SOTON
#(RADIF,SOTON)

x=np.random.randint(100,size=(2,3))

#fght int hastan
#float mikham
#rand beyne 0 1 mide
#randint range dre


x=np.random.rand(5) #in yek numpyy mide 5 sizeshe
x=np.random.rand(3,4)


#+ - *2
#=================quiz====================

#yek file e python b esme khodeton minvi9sid
#5 ta numpy array misazid ham 1 bodi ham 2 bodi ham 3 bodi bashe

#rooshon tamame tabe haee k emroz gofte shod ro tamrin bznid
#nahayat bshe 40,50 khat
#ta charshanbe........

#dar akahr rasmesh konim
#importesh konid ya brid pip instal konid
#matplotlib
#tooye powrshel ( hamon environment)

#pip install matplotlib

import matplotlib.pyplot as plt


x=[1,2,3,4,5,6,7,8,9,10]
y=[2,4,6,7,10,13,16,18,20,43]


plt.plot(x,y)


#hala x va y mitone array ham bashe
#array haee k 40,50 khat bahash tamrin zadido rasm konid





#=========================================================
#=========================================================
#=========================================================
#=========================================================
#=========================================================
#=========================================================
#==================L8=====================================
#=========================================================
#=========================================================
#=========================================================
#=========================================================
#=========================================================
#numpy , matplotlib + open


#3 ta ketabkhoneye mohem ghabl az hoshe masnooe
#numpy ----> pip install numpy ( dakhele powershel ( environmenti k spyder run mishe))
#matplotlib--> pip install matplotlib
#pandas---> pip install pandas
#enter miznim __> wait --> download + install > refersesh sypyder
#badesh soragehe import mirim

#3 no import darim
import numpy #sade tarin import
import numpy as np #import + esme mokhafaf
from numpy import random #tabe keshidan biron az ketabkhone

#ketabkhone ( mesle math , random , statistics , cmath)
#havie koli tabe va class va adade sabet bodan va ma 
#esme ketabkhone ro mizdim , dot mizdim mirf toosh va az dakhele
#ketabkhone ye tabe miovord va oon ag adade sabet bod k hichi
#ag def (tabe) bood parantez dasht k too parantez vorodi migrf
#hala oon tabe ya emal mishod ya bema khoroji mdiAD return, ke mitonesim savesh konim
#ya class, khode class az hezaran tabe sakhte shode
#dot miznim mire dkahele ketabkhone , classo miznim dot miznim mire too class yeki az tabe haye clas ro seda miznim va va va


#mohem trin haye numpy
#------documentation --> hatman 

#import
import numpy as np
#shoma brid dakhele khone done done run she
a=np.arange(6) #0---6 
a = np.array([1, 2, 3, 4, 5, 6]) #yek bod9 , paramntez yadet nre
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) #2D bodi has bod=dimention , chanta parantez too hham
#1d--> fght ye rafdif bod 
#2d--> radif hae k soton daran
#array ychi mese list bod k behesh migan araye
#chanta adad sabet mitonim az array e mon bedast biarim k propertie(moshakahsetesh)
a.nndim #number of dimention yani mgie chan bodi
a.shape #ag 1 bodi (n) n tedae soton #2bod (radif,soton) #3bodi ( laye, radif, soton)
a.size #tedade element
a.dtype #noe va type e elementaro mige

#---assign
a = np.array([1, 2, 3, 4, 5, 6])
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
#ya mitoni listo , df , .... mise np ish krd
b=list((1,2,3))
a=np.array(b)
#yadetonam bashe dakhele assign yechi drim bname dtype

c=list((1.0,2.0,3.0))
a=np.array(c,dtype='i')
#integer= i , boolean = b , complex= c, string = s , float=f


#chizaye dg mesle arrange
a=np.arange(6)# az 0 ta 6
#chizaye dg darim
a=np.zeros(10) #ba sefr por mikone vali 1 bodie
a=np.ones(10)
a=np.empty(10) #in miad ba adade random por mikone --> hamon 0 e , khali , soratesh az zero bishtre

#a=np.arange(start,end,step)
a=np.arange(1,60)
a=np.arange(1,60,2)

#ag bkhaym masalan beyne 0 ta 10 , taghsim bar 5 esh konim
a=np.linspace(0,10,num=5) #yani range e 0 ta 10 o taghsim bar 5 kon arrayesh kon
#*to hasmashon mitonid dtype bznid trype ro avaz koinid

#reshhape
#ag zeros khastam do bodi bashe chi #do radife 5 sotoni mikham

a=np.zeros(10)
b=a.reshape(2,5) #(chanta ardif,chanta soton)
#hata tabe ha mitonan poshte ham bashan

a=np.zeros(10).reshape(2,5)


#random mitonim bsazim
a=np.random.rand() #yek adad beyne 0 ta 1 mide
#chanta adad ?
a=np.random.rand(5)

a=np.random.randint(100,size=(2,3)) #0 ta 100 inetegr

#chra fght inetger ?
#do no distribution --> yani beyne 0 ta 100 computer ke mikhad vardare random
#har adad too range3 0 ta 100 ye shansi drn vase vardashtan
#ag mikhay shans hame ja yeksan bashe yani hame adad--uniform
#ag na mikhay dore yek adadi (seed) beyne y adadi ehtemale bishtri dashte bashe vrdare --> noraml gussian
#ye siz emidi ( chnata rasdif, chanta soton)
#boro tooosho , beyne felan range por kon
#computer mige khob beyne in adad man chghd ehtemal ebrdahstano hesab konm
x=np.random.uniform(size=(2,3))

x=np.random.normal(size=(2,3))
#frgh dre ba balaee
x = random.normal(loc=1, scale=2, size=(2, 3)) 
#loc == oon jaee k mikhay bishtr doresh vrdashte she
#possion, exponteional --> mitonid bbinid

#----access--> dastresi b elemeent
#shabihe llist
#havasemon bashe index az 0 shoro mishe

a=np.array([45,46,47,48,49,50])
#avali? --> index=0
a[0]
#slice -> chanta element
a[1:5]

#2d
a=np.array([[45,46,47,48,49,50],[4335,231,2255,25,34,35]])
a[1,1] #Out[19]: 231
a[1,3] #Out[20]: 25

#slice
a[0:1,2:4]

#copy view
x=a.copy() #hr tghir roye a roye x tghir nmikone
x=a.view() #barax

#sort
np.sort(a) #az 0 ta 9 , az a ta z moratab mikrd emal mikrd
b=np.where(a==4) #shart ro dakhele paranetz ba comparison operator == , > <

#too matrisa taranahade dahstim

a=np.array([[1,2,3],[4,5,6]])
b=a.T #t e bozorg


#---split k biad jhoda
a=np.zeros(40)
new=np.split(a,10) #mishkonatesh

#filter
a=np.array([[1,2,3],[4,5,6]])
b=a[a==4] #sharteto tooye parantez bzari
#shartaro ghashnagehs konid a%2==0

#operator gha--> amalgarha
#hrchizi k roo adad mishod rooye numpy ham mishe ama bayad size a yeki bashe
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
b=arr1+arr2
c=arr1-arr2
d=4*arr1
e=arr1/arr2
#ya az tabe estefade koni
newarr= np.add(arr1,arr2) #+
newarr = np.subtract(arr1, arr2) #-
newarr = np.multiply(arr1, arr2) #*
newarr = np.divide(arr1, arr2) #/
newarr = np.power(arr1, arr2) #**
newarr = np.absolute(arr1) #motlagh

#round
arr = np.floor([-3.1666, 3.6667])
arr = np.ceil([-3.1666, 3.6667])


a=np.array([1,2,3])
#mikhyam max ya min ya sum dr bairim

a.max() #3
a.min() #1
a.sum() #6

#baraye dobodi ha yechi drim bname axis
#axis=0 hamishe yadet bashe miad toole soton amoodi anjam mide
#axis=1 hamishe yadet bashe miad toole radif --> ofoghi
a=np.array([[1,2,3],[4,5,6]])
a.max() #6
#gahi vagghta mikham bgm too kdoom soton kodoma maxe

a.max(axis=0) #amoodi #Out[25]: array([4, 5, 6])

a.max(axis=1) #ofoghi #Out[26]: array([3, 6])
#sum va join ha
#axioos fght baraye do bodi has
#default axis=0 e yani amodi 
#1 bodi ham bbinid amodi nvshte shode dg

#join--dota array ro bchasbonim

arr = np.concatenate((arr1, arr2))
arr = np.stack((arr1, arr2), axis=1)
arr = np.hstack((arr1, arr2))
arr = np.vstack((arr1, arr2))
arr = np.dstack((arr1, arr2))
#mitoni dakhele parnatez axis bzzari

#tamnom shod ma hata mitonim savcesh kponim biron az spyder

#np.save ( 'esmi k mikhay save she' , kodom array)
np.save('filename', a)

#badna k khasti laodesh koni
#load
b = np.load('filename.npy')


#==========matplotlib
#protocol--> inmport, xy , plt draw

import matplotlib as mpl
import matplotlib.pyplot as plt

#kolan bahse x o y e
#x vorodimon 
#y khorojimon
#mitone adad bashe ? KHEYR
#yani fght yechi shyabihe list, array, dataframe
#beshe ye listi az x ha

#hm mitonji liost bashe
x=[1,2,3,4,5,6,7]
y=[45,43,32,2,23,23,43]

#mitone numpuy bashe
x=np.array([1,2,3,4,5,6,7])
y=np.array([45,43,32,2,23,23,43])

#bayad t5edade x ha va y ha brabar bashe--> bbin kolan bahse rasme noghats
#har noghte dar mokhtasat ye x ee dare y y ee dare


#start-----
x=np.array([0,6])
y=np.array([0,100])
#ch mani ee mide
#yani do noghte dreim 
#yeki mokhtasatesh hast (0,0)
#yeki hast (6,100)


#sade trin dastoor
#plt= seda zdm ketabkhone ro besorate mokhafaf
#dot yani boro dakhele ketabkhone
#tabeye plot ro
#tabe hast? --> pas parantez dre pas voirodi mnigire
#vorodi chie ?? kh chiza ama ejbari vfght y hast


#aval x badan y
plt.plot(x,y)

#kolan miad noghato bhm vasl mikone

x=np.array([0,3,6])
y=np.array([0,200,100])
#se noghte , (0,0) , (3,200) , (6,100)
plt.plot(x,y)

#fght y ro bdi
plt.plot(y) #miad x haro noghye aval 0 mdie , nogyteye badi 1 mide va va

#default miad noghato vasl mikone


#hey naizi nis x o y o bznim chon dg save shode too variablamon
plt.plot(x,y,'o') # se noghte khali dad
plt.plot(x,y,'*')

#g bkhaym ham khat bashe ham line
plt.plot(x,y,marker='o') #ham kjhat mikeshe ham noghato

#aval fhmidim linee e kahli, bad noghate khali , bad noghato khat baham
# o , * , . (,) x X + p s

#ms=marker size
#*** x o y fght ejbarie inaro mitoni tanzim koni

plt.plot(x,y,marker='o',ms=20)
#size e markero pointemon noghtmono taghir mide

plt.plot(x,y,marker='o',ms=20,mec='r') #dore point
# red= r, 

plt.plot(x,y,marker='o',ms=20,mfc='r') #tooye point


plt.plot(x,y,marker='o',ms=20,mfc='r',mec='r') #tooye point

#r , k , b , g , y ,w qutation bd esmo bnvisid
#noghat hyam o , * +

#ta inja settinge noghato dadi
#settinge line o chikarf
#y khat , andaze dre, rang dre , noghte noghte ee chijorie , size

#ls = line style
#: ,  - , -- , -. , ""
plt.plot(x,y)
plt.plot(x,y,ls=':')
plt.plot(x,y,ls='-')
plt.plot(x,y,ls='--')
plt.plot(x,y,ls='-.')


plt.plot(x,y,color='r')
#or
plt.plot(x,y,c='r')

#hame chiz joz x , y ekhtiarie
#masalan yek khate range siah , nogte chin
plt.plot(x,y,c='k',ls=':')


#linewidth

#in fght adad ro hm bayad dar qutation
plt.plot(x,y,linewidth='20')


#===================
#fght bayad x o y bdim? na mitoni tabe bdim

x=np.array([1,2,3,4,5,6])
#mitoni az random , arrange estefade koni

y=x+2
plt.plot(x,y)


#mikhay rangi bashe
x=np.array([0,100])
y=x**2 #0, 10000

#yni dastore paeen maid do noghte peyda mikone bvasl mikone

plt.plot(x,y)
#vase hmain ma az arrange estefadde mikonim


# 0 ta 100?
x=np.arange(0,100)
y=x**2

plt.plot(x,y)


#---------------
#dta khat?

x=np.array([1,2,3,4])

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(x,y1) #intoo taghirato bde
plt.plot(x,y2) #intoo taghirat ro bde

#---
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([2, 3, 4, 5])
y2 = np.array([6, 2, 7, 11])

plt.plot(x,y1) 
plt.plot(x,y2)


#ya hamshooo dakhele yek plot bnvis

plt.plot(x1, y1, x2, y2) #tanzimat rooye kol ejra mishe ha
plt.show()


import math
x=np.arange(0,100)


sin_list=[]

for element in x:
    y=math.sin(element)
    sin_list.append(y)

final_sin=np.array(sin_list)

plt.plot(x,final_sin)



#ya sade tar
'''

sin_list=[]
for i in range(0,100):
    y=math.sin(i)
    sin_list.append(y)

'''
    



#===============================
#ina ke aan chioe? x esh c hie y esh chie ?
#masalan xc emon tempreture damae, khob man az koja bdonm ?
#bahse lable
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title('POLYMER CONDUCTIVITY')
plt.xlabel('average MWN')
plt.ylabel('conductivity')
plt.show()


#fonto mitonid taghir bdid
#yek dictionary minvisan
#yechi mese liste
a={ 'nam1' :'ali'  ,'name2' :'vahid' , 'name3' :'hamid'     }

#mese list , bjaye index 0 1 2 , samte chape paranetzo mzire

#font
font1 = {'family':'serif','color':'blue','size':20}
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])


plt.title('POLYMER CONDUCTIVITY',fontdict=font1)
plt.xlabel('average MWN')
plt.ylabel('conductivity')
plt.show()
#fght title? na harchizi k bkhay






#--------
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.show()




#title yechi dre benam loc
plt.title("Sports Watch Data", loc='left')


#inaro bayad b kole structure codetone zaf konid

#age gridbkham 
plt.grid()

#meesal
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)
plt.title('POLYMER CONDUCTIVITY')
plt.xlabel('average MWN')
plt.ylabel('conductivity')
plt.grid()
plt.show()

#plt.grid(axis = 'x') #amodi mikeshe , y = ofoghi


#tanzimatesh ham msihe tagir dad
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)
plt.title('POLYMER CONDUCTIVITY')
plt.xlabel('average MWN')
plt.ylabel('conductivity')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()




#====================================================
#====================================================
#====================================================
#scatter-------------------
#bishtar baraye rasme noghat bekar mire
#masalan 13 ta noghte drim va rasmehs mikonim b hamin sadegi

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()


#------------------------------------------------------
#ag dota data dashte bashim yani 10 ta az yek type 10 ta az yek type e dg
#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()
#------------------------------------------------------
#mitoonid rang ro taghir bdid b sadegi
#baraye har data begid che rangi mikhayd

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'r')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = 'k')
plt.show()
#------
#gahi vaghta mikhahid ke yek shedatii bedid
#yani masalan yekseri noghte darim k harkodom yek x o y darand
#tozihat ro bekhonid

#aval 13 ta noghte misazim
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

#miaym migim k y emoon rangesh beyne maalan 70 ta 100 hast
#migim agha bia az 0 ta 100 done doone b 0 yek adad bde
#b 10 yek adad bde b ..
#yani mikhaym shedate Y ro bbinim
#pas yek numpy az colour misazim
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])


#bad migim bekesheshon
#tooo tanzimat joloye c , colour ro mizrim 
#cmap ham yani hala k shedate ranagro gofti
#mane matplotlib biam masalan az 0 ta 100
#chio taghir bdm ? abi b ghermez ? siah b sefid ?
#hame ina yek esmi dre va mitonid dar matplotlib bznid 
#scatter colour va bbinid
#https://matplotlib.org/stable/gallery/color/colormap_reference.html
plt.scatter(x, y, c=colors, cmap='viridis')


#inam nshon mide shedatesho samte raste tasvir
plt.colorbar()

plt.show()

#** mitonid title va .. ham mesle plot bznid

#-------------------------------------------------
#mitonid bgid az noghteye aval ta noghte ye akahr
#har noghte ch sizi dashte bashe
#yek array misazid baraye har noghte az dataton
#yek adad b onvane size midid 
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

#size ro inja avred konid
plt.scatter(x, y, s=sizes)

plt.show()


#ychiuzi dare bename alpha k mitonid bgid cheghad kamrang bashe beyne 0 ta 1 e
plt.scatter(x, y, s=sizes, alpha=0.5)



#====================================================
#====================================================
#====================================================
#bar--------------------
#dar asl baraye rasme dade haye sotoni hast
#mesal -->

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()


#0------mitonid ofoghi ham rasm konid hamino
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
#bejaye bar() az barh() estefade konid
plt.barh(x, y)
plt.show()


#**********************
#dakhle plt.bar() mitoonid tanzimat bdid
#color rang hast , width andaze zekhamat hast
#hrcvhizi joz x , y baghiash ekhtiarie va fght settinge
plt.bar(x, y, color = "r", width = 0.1)



#====================================================
#====================================================
#====================================================
#histogram-------------------------------------------
#in baraye distribution hast yani baraye توزیع
#vase inke bebinid tozih ha chijorian
#masalan fk konid hamchin chizi drid
#in cxhie? 
#ye x drim k omade mige
#250 ta adad sakhte dar yek array k hamashon 
#+ - 10 ta nazdike 170 adad vardashte random va tooye
#in array ro por krde
x = np.random.normal(170, 10, 250)



#hala age bekhyam bbinim har adad cheghad shans dashte k bardashte shode
#یعنی توزیع عدد هارو ببینیم کافیه پایین رو بزنیم

plt.hist(x)
plt.show() 
#hamantor k didid mige ke 170 bishtrin shanso dre
#badesh 160,180 bnishtr 
#va ....
#in ax chiuo neshon mide ? mige tooye in x 
#x chie ? ye data hast yek zarfe toosh 250 ta adad hast
#mige az beyne in 250 ta adad , masalan aksareshon nazdike 160 ta 180 hast valueshon




#====================================================
#====================================================
#====================================================
#pie chart-----------------------------------------
#baraye rasme nemoodar haye dayerre eee
#masalan ma mikhaym bgim yek dayere ro 
#be charghesmat taghsim kon
#35% , 25% , 25 % , 15%

#kafie injori bnvisim
y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show() 



#agar bbinid in rangaro khodesh tartibi gozshte 
#chizi tozih ndde
#khob age joloye har ghesmat bkhaym tozih bnvisim kafie
#be tartib benevisim
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.show() 



#mitonid dar kenare label ha , begid harkodom be tartib che rangi bashan
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 


#------mitonid yekodom ro bkshid biron
#kafie yek list  bzarid va harkodom k bayad sare jash abshe bezarid 0
#ooni k mikhayd bkshid bironm yuek adad az 0 ta 1 bdid , yani
#chan darsad biad biron
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0] #inja mighim avalie , yani oni ke 35 darsade yani oni ke apple hast 0.2 az hame bishtrr biad biron
#ama baghie 0 , yani sare jashon bashand

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()




#=================================
#ketabkhoneye seaborn --> doicumentation bekhonid
#bar rooyte matplotlib neveshte shode va ykm khoshgeltare
#https://seaborn.pydata.org/tutorial/introduction.html





#===============================
#file-------------------------
#ta alan vorodimono khodemon misakhtim ya assign mikrdim
#chijori vorodi vardarim"
#az desktopi jaee chzii
#data chie? 1-text .txt / 2.ax .jpg,.png, asp / 3-video
#4-excell .csv--> 90% e datahaee k analysize
#tooye azmayeshgah yek excelle
#yani soton dare va ....

#chijori open konim?

#[pas nakeshimesh]
#choon mikhyam openesh konim va yeja savehs konim bahash kar konim
#python yek puthon built in function , tabeye daskheli 
open #narenji shod
#built in function --> tabe hast
#chi mikhad parantez ---> vorodi mire dakhelesh
#structure

#bayad yek variable yani yek zarfg bsazid
#mosavi bsazid va open ro bznid va haerchi open krdid
#bre too zarf zakhire she

#dota vroodi migire
#f= open ( address , chikar mikhaym konim?)


#address= jaee k hast , ** too qutation baayd bashe , #\\ 
#.format bashe

f=open('data_c.txt')
#in addres kafi nis
#chanta rahe
#raftam onja click rast too filam
#properties
#location ro cpy krdm
#C:\Users\sunhouse\.spyder-py3\codha\2023COURSE
#ama niaz b tagiir drre
#har \ --> \\
#va format bzni tahesh

f=open('C:\\Users\\sunhouse\\.spyder-py3\\codha\\2023COURSE\\data_c.csv')

#1--> \ tbdim krmd b \\
#2--> tahesh esme filamo bznm
#3. format yadewt nre

#oomad y texti sakht
#hala y arg dg bas bhsh ezazfe koni

f_loc='C:\\Users\\sunhouse\\.spyder-py3\\codha\\2023COURSE\\data_c.csv'
f=open(f_loc,)

#ag mikhay bkhooni read --> 'r'
#mikhayt bnvisi --> 'w'
#ye file has mikhay chizi bhsh ezafe koni append --> 'a' 
#'x' ham shabihe 'a' hast ama ag oon file vojod ndshte bashe error mide


#--mikham bkhonm
f=open(f_loc,'r') #mire dakhe locationi k dadam behesh be gahsde khodnban bazesh mikone

f=open(f_loc,'w') # be ghasde neveshtan

f=open(f_loc,'a') #b gahsde ezafe krdne chizi

#C:\Users\sunhouse\Desktop
f=open('C:\\Users\\sunhouse\\Desktop\\ali.txt','r')

#mikhay bkhoni bkhon

print(f.read())

#mikhay panjta caracter bkhone
print(f.read(5))

#yek line bkhone
print(f.readline())


#ag se bar bnvisi
print(f.readline()) #in khate vaalo mikone
print(f.readline()) #mire khate badi ( dobare az aval nmikhone ha)





#*****mohmtrin chiiiiiz
f.close()
#ag nakonid na save mishe na hichii asan hang


#bastamesh haal mikham bnvism

f=open('C:\\Users\\sunhouse\\Desktop\\ali.txt','w')

f.write("Now the file has more content!")

f.close()
#hamaro pak krd va nevesht


f=open('C:\\Users\\sunhouse\\Desktop\\ali.txt','a')

f.write("aya ezafe shod ya na?")
f.close()



#remove
import os
os.remove('C:\\Users\\sunhouse\\Desktop\\ali.txt')

#inam azin








#----------------------
import pandas


#pip install pandas




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
#=========================================================
#=========================================================
#=========================================================
#=========================================================
#=========================================================
#=========================================================
#==================L9=====================================
#=========================================================
#=========================================================
#=========================================================
#=========================================================
#=========================================================



import numpy as np
import matplotlib.pyplot as plt



#yechizi dahstim bname list
a=list((1,2,3,4,5))
#numpy omad dota kar krd
#1-sorato bord bala gfo man 50 bareabar sari taram
#yani ychi drm bename array (araye) 50 barbara saritare 
#operating mohasebat .....

#dobodio se bodi


#se bodi--> vase yadgirie
#2D --> kh bekar miad
#chona ksare dathaaaa--> too azmayeshgah , too sanat , too business va va va
#2D--> yekseri radif dre (ina sample) #yekseri soton dre

a_list=list((30,40,50,60,70,80))
a_array=np.array([30,40,50,60,70,80])

#pandas gof khob 
#numpy > liste
#pandas omd gof man ychi bsazam bhtr az numpy bashe

#pandas > numpy > list
#gashtan donbale index baraye access skahyte

#[pasa chika rkonim? --> biaym label besazim
#ye oon sotone more nazar esm dashte bashe


#omad  moarefi krd
#Series
#list dashtim , Array dashtim , 
#hala drim bname Series


import pandas as pd
#aval k bayad improt krd va mokhafaf krd b pd
#sedash abyad zad pd
#noghte zad rft dakhel
#yek tabe bekeshim biron
#tamame tabe haye pandas horofe bozorg avaleshon dre **********
#yademon ham hast k python case sensetive has yani a ba A frgh dre

#Print #rngi nbmishe
print #rngi mishe

ali=4
Ali=6

#series=Series

#eshtebahhhhhhh************
#a_series=pd.series

a_series=pd.Series([30,40,50,60,70,80])



#moghayese in se ta----

a_list=list((30,40,50,60,70,80))
a_array=np.array([30,40,50,60,70,80])
a_series=pd.Series([30,40,50,60,70,80])


#structure
#Series(data,index)
a_series=pd.Series([30,40,50,60,70,80],index=['a','b','c','DD','oon','akhari'])

#b che dard mikhore?


#bbin listo numpu mikhasi acces koni
#dovomio mikhasi

a_list[2] #Out[38]: 50
a_array[2] #Out[39]: 50

#hala fk kon 10000 ta index has 

a_series['akhari'] #Out[40]: 80
a_series['c'] #Out[41]: 50


#avalin chizi k sakht --> sereies ---> numppy 1D hast k indexash ma mitonim nam gozari konim

#assign
pd.Series([20,30,40],index=['ali','vahid','reza'])

#ye raveshe dg dare bename dict dictionary

#dictionary
#list []
#dict {}
calories_list=['day1','day2','day3']
calories = {"day1": 420, "day2": 380, "day3": 390}
#esme zarf = 



new=pd.Series([20,30,40],index=['ali','vahid','reza'])

new_dict={'ali':20 , 'vahid':30, 'reza':40}

#dict ro tbdl b serie

convertshode=pd.Series(new_dict)




#===========================
#kholase ye asli
#yechi dahstim bname list


#numpy , array ovord k sari tr bodo do bodi mishod


#pandas omd ychi ovord benaME Series k mitonesim b jaye index ha khodemon y chizi bzarim hala esm bashe adad

#2d?

#omd gof 
#ychizi drm bename DataFrame --> Serie 2  bodi


#********************************
#new=pd.DataFrame(data)

#mitoni dasti vared koni
#mitoni numpy, dictionary ya ...


a=np.array([[11,10],[12,20],[13,30],[14,40]])
b=pd.DataFrame(a)
b=pd.DataFrame(a,index=['a','b','c','d'])
#b=pd.DataFrame(a,label=['takane','dama'])

#yekare dg--> dictionary
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

c=pd.DataFrame(data)

c=pd.DataFrame(data,index=['data1','data22','data3'],columns=['ali','vali'])


#access-->
#BE oon radi brsi daghigh mes elisto
#list a[2]
#kasfie bnvisei esmeshpo va esme index

c['data1']


#2d
a2_array=np.array([[30,40,50,60,70,80],[5,6,7,8,9,10]])

a=pd.DataFrame([[10,20,30],[5,4,3],[1,2,3]]) 


#DataFrame hamon Numpy arraye e 2 bodi has
#fght indexo columns balash mitoni adad ya horof bzari




#yeki az rahaye moheme assign
data2 = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

mydf=pd.DataFrame(data2)

mydf=pd.DataFrame(data2,index=['data1','data2','data3'])


#assign ro yd grftim
#baraye acces----

#mese list mese numpy
mydf[0] #KeyError: 0

mydf['data1'] #KeyError: 'data1'

#ina baraye numpy o list bood

mydf.loc['data1']
#calories    420
#duration     50
#Name: data1, dtype: int64


#agar indexat frgh nmikrd ham
mydf.loc[0]





#==================
#assigne value dastiiiiii
#ag yek file dahstim chi? masalan excell bashe ya ya ya


#ye formate kh kh mahboob --> csv
#aval openesh konid

#esme zarf mziri
mydf=pd.read
#inop k mizni harchi formate miare vbarat

mydf=pd.read_csv('C:\\Users\\sunhouse\\Desktop\\data.csv')

#C:\\Users\\sunhouse\\Desktop\\data.csv

#az open estefadekoni b formate csav miad inja

#ama in pd.read_csv -->o oon csv ro mikone yek dataframe

type(mydf) #Out[71]: pandas.core.frame.DataFrame


print(mydf) #vaghty print bzni
#hamon csv file ro miare
#5 ta readife aval 5 ta radife akhar
#paenesham mige chanta radif dar chanta sotoon

#mian esme oon zarfi k zakhire krdno mizanan
#va chnta kar bahash mikonan

#analyse avalie
#mydf file e mane
mydf.head() #5 ta radife avalo
mydf.head(10) #10 taeo miare
mydf.tail()
mydf.tail(10)
#mhemtrin
mydf.info()

#4 ta column (soton drim)
#jolosh nvshte harkodom chanta non-null
#ma ba inkar mibinim k chanta sotonemon null hast ya nan hast
#null o nan yani kahli ya harhcizi --> naghs

#assign
#khodemon dasti midim
#dictionary
#liste --> series
#np array 
#file hast

a=np.array([[1,2,3],[4,5,6]])
b=pd.DataFrame(a,columns=['a','b','c'])

#dastresi
#dota dastresi
#ya mikhay b indexi brsi loc
b.loc[0]
#a    1
#b    2
#c    3
#Name: 0, dtype: int32

#age column sotonio mikham
#esme moteghayed yni dataframemon ye [] dakhelesh esme sotonm
b['a']
#0    1
#1    4
#Name: a, dtype: int32


#preprocesign --> ghable farayanad

#analys mikonim dataro



#--------initial analysis ( analize avalie )----------------------

#azinja bbad analyse nahaee -- DATA CLEANING - PAKSAZIE DATA-----------
#---DATA CLEANING-------
#hamishe datahmon baraye hsohe masnooe ya film ( nadeer) , ax 
#dataa ( hamon adad) --> formatesh chie? word, excell , csv(hjmishe)

#formatesh pas na array hast na pd hast na hichiii

#ama mitonim ba read_format --> tbdilesh konim bn dataframe

#aval initial analysis miznim

#naghs dr datahmon
#1-empty cfell ( khali bashe)
#2-wrong format
#3-wrong data 
#4-duplicated (tekrari)


#pas dar datahmon 4 ta naghs drim



#harja khali bashe moshkel dar convert open bashe 
#NAN= not a number

#ag bjaye str zade adsad -- wrong fromat

#baste b application , 

#wrong data
#masalan y kari mikonim bayad damaha hame beyne 20 ta 60 bashe

#ag jaee zade shode bashe 700 --> ghalate
#in ghalat shayd bkhtre dastgahe , nemname , kasi k type krde , convert , 
#mohem nis ressource manabe khata mohyem nis

#mohem ine ke yek naghsi dr data hast
#hala yki az in charta 1-empty cell (nan) 2-wrong format (bjaye str int)
#3-duplicated (tekrari has) 4-wrong data ( rangesh frgh mikone y aya)



#dr in soorat avalin akremon in bod k ba info mididm k chnta mpty drim

#deoone donne mikhaym brim bbinim chjikaresh konm

#-----empty cell------------------
#aval info miznim mibinim khob dare dg
#marhale1-bfhmim null darim ya na---> info
#marhale 2- agha asan fhmidim hala chikarwesh konim?

#hazdfesh konim?--ag are ok haazf kon
#ya replace konim? --bachi??

#hazf
#kole oon datframeto bnvisi

mydf.dropna() #yani drop kon na number
#ino bzni bayad savesh koni dakhele ye variable e dg

#ama vase rahati
mydf.dropna(inplace=True)
#miad rooye khode mydf emal
mydf.info() #baraye chek krdne

#az 169 ta row , 164 
#hgaashonam shdoan non-null

#be sadegii


#agha nmitonim rotye felan soton inakro konim?
#baraye hazf na********


#replace --> jaygozin kon --> ba chi? chi jahs bzrm?

#jaye tamoome null ha bia

mydf.info()

mydf.fillna(120) #ba in mitoni fill koni 
#tamame noghate khalio ba 120

#ama in khdoesh yek datfrsame e jadid mide emal nmishe

mydf.fillna(120,inplace=True)

mydf.info()
#hamon 160  ta radif monde ama 
#calories , 164 non -null boid alan shode 169 ta yani poresh krdim ma


#masalan fght yek sotono biad empty cell hasho por kone
mydf['Calories'].fillna(120,inplace=True)
mydf['Pulse'].fillna(200,inpalce=True)
#aval ino mzini b kjole soton dastresi peyda mikone


#overview: ya roo kole columnha yani kole dataframe harchi empty cell dre por koni
#y bgi felan soton felan adad felan...

#karhaye ghashngtar
#mean() / median() / mode()


x=mydf['Calories'].mean()
print(x) #368.22248520710065

mydf['Calories'].fillna(x,inplace=True)

#--------------

mydf=pd.read_csv('C:\\Users\\sunhouse\\Desktop\\data.csv')


ffil_df=mydf.fillna(method='ffill')
bfill_df=mydf.fillna(method='bfill')

#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html
#method{‘backfill’, ‘bfill’, ‘ffill’, None}, default None
#Method to use for filling holes in reindexed Series:
#ffill: propagate last valid observation forward to next valid.
#backfill / bfill: use next valid observation to fill gap.


#-----------2wrong format
#str bashe bokonm int
#fek kon yek df drim 
#charta soton dre 1000 ta radif
#yeki az soton ha date hast
#bayad hame injori bnashan '2/6/8'
#ama bazia momkene 2/6/8 adad bashan na str

#minvisi
#avalk mirm toye sotonm
#pd.to yani ino hamashono in format kon
mydf['Date']=pd.to_datetim(mydf['Date'])

#ya hat miutoni az remove estefade koni
#in remove frgh dre

df.dropna(subset=['Date'], inplace = True)


#** tozih




#-----------
import sklearn




#-------QUIZ-----
#VOICE TROZIHESH

'''
bebinid bayad yek tabe besazid ke az taraf
file e csv bgire

yani aval biad ba dastoore zir oono tabdil kone be yek pd.DataFrame

name=pd.read_csv(input)


#badesh yekseri calculation anjam bde ( ya khodesh ya tahiresh bdid b numpy)


va sepas an ra nasb kone

hameye ina bayd dar yek tabe bashe 

mesal: azmayeshe tensile yek testi hast ke miad nemone ro mikeshe
va dar har stress , strain ro andaze giri mikone

nahayat yek file e csv mide ke

1000 ta radif hast k har radif do sotone yek soton strain , yek soton stress

tabeye zir file ro migire va monhanie stress-strain roi mikeshe

va yekser chizaro mananande modole young ham hesab mikone



'''

def Stress_Strain_Curve(input_file,which):
    '''
    This function is belonged to stress strain
    Parameters
    ----------
    input_file : .csv format
        the file must be inserted in csv.
    whcih : str
        please say which work we do ( plot or calculate?).

    '''
    #convert the file
    mydf=pd.read_csv(input_file)
    
    if which=='plot':
        #get the data on each columns
        stress=mydf['stress']
        strain=mydf['strain']
        
        #plotting data
        plt.plot(stress,strain)
        plt.title('stress-strain curve')
        plt.xlabel('stress')
        plt.ylabel('strain')
        plt.show()
    
    
    if which=='max stress':
        #calculat the stress_max
        stress_max=mydf['stress'].max()
        return stress_max

    if which=='young modul':
        #calculate young modul and .....
        return young_module
    
    
****L13
#review-----
#python built in function ha
#dastoorat ( if , if else , while , for )
#str,list + method
#random
#def
#numpy
#matplotlib
#pandas-----
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#frghe list numpy
a_list=list((30,40,50,60,70,80))
a_array=np.array([30,40,50,60,70,80])
a_series=pd.Series([3040,50,60,70,80])
a_series=pd.Series([30,40,50,60,70,80],index=['a','b','c','DD','oon','akhari'])
#assign--> dasti bnvbisi/ list bzar / numpy array bzari / data ro import koni / dictonary
#access
a_list[2] #Out[38]: 50
a_array[2] #Out[39]: 50

#pandas
#fght bjaye index esme on index
a_series['akhari'] #Out[40]: 80
new_dict={'ali':20 , 'vahid':30, 'reza':40}
new_dict={'ali':[20,30,40] , 'vahid':[30,40,50], 'reza':[40,50,60]}

#2d --> DataFrame too pandas / 1D--> Series
a=np.array([[11,10],[12,20],[13,30],[14,40]])

#ino tbdil konm b datframe chanta rah dre
#avalin rah--dasti
a=pd.DataFrame([[11,10],[12,20],[13,30],[14,40]])
#dovomin rah--> tabdile arraye b df
new_array=np.array([[11,10],[12,20],[13,30],[14,40]])
a=pd.DataFrame(new_array)
#sevomin rah--> tabdile dict be df
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
a=pd.DataFrame(data)
#4 omin rah--> open the file 
a=pd.read_csv('address')


#4 rtahe dataframe sakhtan ro ayd grftrim
#frghe df ba arr chie?
#mitonim [index radif row ]haro ya [label (column) soton]

#index
#yeki az ravesh haye bala assign kon value ro 
#badesh ....
df=pd.DataFrame([[11,10],[12,20],[13,30],[14,40]],index=['a','salam','taghire khoon','nemoneye4'])

#baraye column ha ya soton ha ya label
df=pd.DataFrame([[11,10],[12,20],[13,30],[14,40]],columns=['vizhegie 1','vizhegie 2'])


#hala cdhijori access konm?
#baraye np array ha-->
arr=np.array([[1,2],[3,4]])
#masalan acces b yek value mikhasim

#esm bad beraket arr[kodom radif, kodom soton]
arr[1,0]

#pd
#ya yek element bkshi biron , ya yek row , yek yek columns
#ag yek soton bekhaym
df['vizhegie 1']
#ag element khasi
df['vizhegie 1'][2]
df['vizhegie 1',2] #KeyError: ('vizhegie 1', 2) mnmitone

#radif mikhay
df.loc[0]

#element mnikham
df.loc[0]['vizhegie 1']
#or
df.loc[0,'vizhegie 1']


#mitonimmm hata az yechizi bname iloc estefade konim
#yani kari dg nadare chi esmesh chie dagghighan mese numpy amal mikoen
#esmefile.[kodom index][kodom soton] hamaro b adad bgo az 0 b badd

df.iloc[0][1]
#or
df.iloc[0,1]

#-------operator
#+
#-
df1=pd.DataFrame([[1,3],[2,4]])
df2=pd.DataFrame([[5,7],[6,8]])

#jam
zarfe_jadid=df1+df2
#df1-df2
#xarb dar yek adad df1*2
#be tavan df1**4

#na tanha kole dataframe ro operate mitoni koni balke mitoni har soton ro ya har radif ro

#dar hame ja baraye acces b 
#************
#tooye pandas ma
#4 ta chiz drim
#1-kole datframe--> df
#2-fght yek radif --> df.loc(9)
#3-fght yek sotonm --> df.['esm']
#4-yek element (yani yedon adad) df.iloc[0,1]

#operat ro rooye kol ya harkodom k bkhay anjham bdi
df1=pd.DataFrame([[1,3],[2,4]])

df3=df1+1



#biay bgi columne avalio inkaro konm baahsh
#**********aval access bad apply
zakhirer=df1[0] +1 
zakhire=df.loc[0]+1

df1=pd.DataFrame([[1,3],[2,4]],columns=['v1','v2'])
                 
#operator haye amari bzni

df1.max() #chonj dota soton drim vase harkodom maximume on sotrono mide

#access apply
df1['v1'].max()

df1.loc[0].max()


#dg harchi paeen miznm 
#shoam mitoni roye kole df , roye yek soiton , roye yek radif ya rooye yek element ejra koni

df1.max(axis=1) #inm baraye oona


df2=df1.T#resizew

#masalan fk kon yek dataframe drim bename air_quality
#chn nemoneye operation

#sakhte yek dsoton

df1['v3']=df1['v1']*2.45


air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
air_quality["ratio_paris_antwerp"] = (
    air_quality["station_paris"] / air_quality["station_antwerp"]
)


#sort--> tartib ddn --> soal mishe man bar ch asas tartib bdm , bar asase kjodom columns

df.sort_values(by="Age")
#yani bia df emon ro sort kon bar asase sotone  Age


#cjoinn , chasbond

df3=pd.concat([df1,df2],axis=0)
#**
#axise 0 yani dar toole ofoghi
#axise 1 dar toole amoodi
mydf=pd.read_csv('C:\\Users\\sunhouse\\Desktop\\data.csv')


#chikar mikone? kole sotone duration ro hazf mikone
mydf.drop(columns='Duration')

#tamame dSTOR HAYE pandas , emal nmishe balke ye df e jadid
#mide va bayad zakhirash koni
#vali hamashon yechi drn bename inplace ag True koni mishe emal
newdf=mydf.drop(columns='Duration')

#or
mydf.drop(columns='Duration',inplace=True)

#ina hazfe soton bod
#hazfe radif chtor?
mydf.drop(index=12)
#m,esle hamishe in dastor ye array pas mide bayad zakhire konim


mydf.drop(index=12,inplace=True)

#ag inplace False bashe true nabashe taghirat rooye df save nmishe




#====analyss================

#vared krdne data
mydf=pd.read_csv('C:\\Users\\sunhouse\\Desktop\\data.csv')
mydf=pd.read_csv('C:\\Users\\sunhouse\\Desktop\\data.csv',index_col=0)
#ag 0 bzni in vase vaghtye ke
#ya mitoni joloye index_col= esme dsotoni kmikhay bar hasbe oon index gzoari bshe

#initiual analasys --> analize avalie
mydf.head() #5 radife avalo
mydf.head(10) 
mydf.tail()#5 taye akhar
mydf.tail(15)
mydf.info() #Initial analysis
#caval mige chanta row drim , entries yani chnta radif drim chanta sample drim chnat nemonde drim
#har soton chantash non-nulle
#bayad non-null ha ba entries barabar basher

#null== dadeye naghes

#===========================bahse cleaning data

#isna
pd.isna(mydf) #vase kochika harja true bashe yani naghese

#----Null chn type drn
#1-nan --> empty cell --> khalie 
#2-formatesh bade
#3-eshtebahe (yani masan damaha nmitonan zire 0K) damamon has -10
#4-dupliocated tekrary repeated

#-------empty
#1-remove
#2-replace ( 1- yek adad dasti , 2-ya mean modian bgiri , 3-methdohaye forward backward)

#remove
mydf.dropna(inplace=True)

#ag replace koni yani fill
mydf.fillna(120)
newdf=mydf.fillna(120)


mydf.fillna(120,inplace=True)


#yadete goftm az chand aspect janbe bbin #in vase kole df ha has
#ag bnkhaym rooye yek column ya yek soton taghir ijad konm chi?
#acces apply

mydf['Calories'].fillna(120,inplace=True)
#yni in soton , harchi khalie ro ba 120 avaz kon


#fotmat frgh kone chi
#miam migim kole oon soton ro b felan format tabdil kon
x=mydf['Calories'].mean()
print(x) #368.22248520710065
mydf['Calories'].fillna(x,inplace=True)


ffil_df=mydf.fillna(method='ffill')
bfill_df=mydf.fillna(method='bfill')


#-----------------
#flash back
#taghire yek element

#103 bod mikham konm 106
mydf.loc[2,'Pulse']=106

#----vaghty yek element eshtebah bshe dakhele data mitoni injori aqvazesh koni

#soal=--> man yad grftm chijori dadeye ghalato wrong data 
#taghir bdm ama khob datam 1 millyard value dre chikar konm

#for o if o ina inja mian bkar

#ghablesh dota chizo yad bgir


mydf.index #listye indexaro mide
mydf.columns #listi az column hato


for x in mydf.index:
    if mydf.loc[x,'Pulse']>200:
        mydf.loc[x,'Pulse']=100
        

#masalan dama

for i in mydf.index:
    if mydf.loc[i,'Tempreture']<-273:
        mydf.loc[i,'Tempreture']=0
        
#repeated ya duplicated
print(mydf.duplicated()) 

mydf.drop_duplicates(inplace = True)




#-----------------------akharin marhale pas az analysis

#vaghty drop mishan index ha bham mikhore *****
mydf.drop(index=4,inplace=True)

#indexa bhm mirize
mydf.reset_index(drop=True,inplace=True) 




#==================
#yechizi drim bname corr
mydf.corr()


#age rabetey soyon haro bkhaym bbinim azin estefade mikonim
#pulse ba pulse / ya x ba x ch rabete ee dre
#x=x / pulse = pulse = pulse = (1)* pulse

#1- rabete mostaghim
#0 yani hcih rabete ee beyneshon nist



#===================
#plot

#mitoniaz matplotlib estefade koni 
#mitoni xnadi
y=mydf['Pulse']
x=np.arange(len(y))

plt.plot(x,y)
plt.show()


#ya mitoni az khode pandas estefade koni
mydf.plot()
plt.show()


#in ke fght plot e sadas ma scatter dahstim vba va

mydf.plot(kind = 'scatter', x = 'Calorie', y = 'Calories')


#=======================================================
#Machine learning beshavim-------------------


#farghe hoshe masnoee va automation

for i in range(0,5):
    print(i)


#do generation ( nasl) darim

#machine--> 0 , 1 mifhme va hichii nmifhme hich shooor hich dark maghz hichhh csimplke salculator

#hadaf goal--> machinemon mesle yek ensan yadbegire, va fekr kone va amal kone

#3 ta moalefd 1- yadgrftn 2-fekr krdn 3-tasmim grftn




#2 ta generation --->

#first generation---> hjoshe masnoe ha --> if else e khodemone
#mesal

telegram.input() #mire migire text ro az trf

newchat=telegram.input()
newchat='salam chetori'


newschat=input('salam man robotAM JAANam')
if newschat=='salam':
    print('salam janam?')
if newschat=='khobi':
    print('mersi to chtori')
if newschat=='gheymat chande':
    print('345')
    
#in shdo firsdt egeneration

#thrick mizdn

#momekne rtaraf salam o Salam #sAlam

newschat=input('salam man robotAM JAANam')
l=newschat.lower()
if l=='salam':
    print('salam janam?')
if l=='khobi':
    print('mersi to chtori')
if l=='gheymat chande':
    print('345')

#htmn trrf nminevise salam
#shayd bge salama agha
#ssalam fdelani



#----------
newschat=input('salam man robotAM JAANam')
text=newschat.lower()

if 'salam' in text:
    print('salam')
    


#=====================
#ROBOT /#10000000 khat ---> robot


#sisteme khebre ---> miomdn vase harsoale shimi , ya hrchi injori if o else misakhtahn




#hamin alanesh --> too insta
#5 ta soal bnvisi , bgi roo harkoidm click krd ch jagvabi bde


a=input('number:')
if a==1:
    print('تخفیف های ما .....')
    
    
    
    
#=================
#moshkele first generation chi bod?


#1- niaz b cod haye ziadd boood( programmed)
#2- birona az mahdode ro nmifhme (out of data) = prediction ndre pishbini ndre
#3- yad nemitone begire ( mohemtrinn eshkal)

#ghoveye yadgiri ndre--------
#banabrin fkr krdn bia yechi bsazim k yad bgie

#hooshe masnooe --> bozorgtrin shakahsho moarefi krd--> Machine learning ( yadgirie mashin)
#yek mashin betoone yad bgire


#hooshe masnooe chata shakhe dre
#1-sisteme khebre 
#2-robotic
#......

#machine learning o jozve shakhe ha nmidonan
#balke machine learning 80% e hoshe masnoe hast k dar tamame shakhe ha ifaye naghsh mikone



#NLP
#


#Macxhine learning---->
#Data-driven --> mobtani bar dade
#ye box hamishe drim


#box --> bhsh ye data midim ( film, ax ,e excell)
#az roosh yad migire ( relationship)
#hala tebghe oon tasmnim migire , fekr mikone amal mikone

#2 phase
#1-fazesh training
#2- amalklard



#-----YAD GEREFT ===> GHOVEYE YADGIRI DADIM B MASHIN 
#yadgiri ba rpayeye data bood***


#hamishe yqdet bashe

#ma data hamonn yek excelle yek dataframe yek arraye e
#hamvareeeeeeeeeeeeeeeeeeeeeeeeeee******

#radif dre o soton dre

#har dataeee dar jahan--> yek vorodi dre yek khoorji ( optional)

#vorodi --> yani ma mirtonim tanzimesh konimo taggiresh midim 
#khoroji--> partameteri ahs k bartaye ma moheme 

#in datmone yek vorodi yek khgoroji dre

data=pd.DataFrame([[0,30,200],[4,43,300],[8,56,453],[16,65,478],[32,71,589]],columns=['DARSADE GRAPHENE','Temprature','PAYDARIE FESHAR'])



data2=pd.DataFrame([[0,30,200],[4,43,300],[8,56,453],[16,65,478],[32,71,589]],
                   columns=['DARSADE GRAPHENE','Temprature','PAYDARIE FESHAR'])


#[pas yek vorodi ee drim yek khoroji



#khorojiiimon---> 3 ta halat dre
#1- ya peyvaste hast --> yani adade injori--->Regresssion
#2-ya gosastas--> 1,2 'a' 'b' -->classification



data=pd.DataFrame([[0,30,'y'],[4,43,'n'],[8,56,'n'],[16,65,'n'],[32,71,'n']],columns=['DARSADE GRAPHENE','Temprature','PAYDARIE FESHAR'])

#chantaeesh mikonim
#y o n
#bale o na
#0 o 1
# 1 o 2 3
#A B C
#tabaghe bandi--> daste bandi--> classificatiomn




#---------------------
#machine learning------------------------
#1-regression
#2-classification



data=pd.DataFrame([[0,30],[4,43],[8,56],[16,65],[32,71]],columns=['drsd','feshar'])

x=data['drsd']
y=data['feshar']

plt.scatter(x,y)\
    
    
    
    
    
#-----l8=========














