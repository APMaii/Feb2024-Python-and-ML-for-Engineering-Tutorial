YEK computer yek mashin hesabe sade hast k az koli 'bit' tashkil shode ke
mohasebat ro ba in bit ha anjam mide yani miad mige har khone (yek khaneye 
jamed) age bargh vasl bashe 1 hast age bargh vasl nabashe 0 hast.
ba in technique e 0 o 1 i (binary) tonestim be yek jesme jamed 0 o 1 yad
bedim vad ba tabdile donyae paye ye 10 be paye ye 2 tonestim hame adad haro
barash besazim.

khob in computer na fahm dare na mitone yad begir na ..
faghat yek mashin hesabe pishraftas hamin.

omadan goftan ma niaz darim kari konim ke machine (computer) betone 
1-yad begire 2-fekr kone 3-tebhe oonn tasmim begire(amal kone)
khob in 3 ta paye ye hooshe masnoee shod

dota nasl hooshe masnooe darim:
    1-nasle aval miomadan migoftan bia ba if-else koli shorot bezarim
    va ba in shart ha betonim yek barname ye control shode besazim
    ba in kar system haye khebre (ke javabe soalaro midad) 
    chat bot haye avalie ke masalan age (if) benevisi salam mige salam
    va hata robot haee k sensorash age masalan felan signalo bede onam
    felan signalo mide va tabdil be harekate mechanici mishe
    
    2-nasle dovom: in nasl ba omadane machine learning oomad yani gfotan 
    bia ye kari konim computer ha betonan yad begiran va khob ba inkar
    soale aval--> az chi yad begiran ? khob az data (badan migim datachie?)
    khob fek kon machine ha betonan az data yad begiran(1*) va badesh tavasote
    yad gerefte hash ba manteghi ke bedast ovorde (2*) betonan pishbini
    konan ya daste bandi konan (tasmim begiran)
    ba in kar system haye khebre kareshono dadan b ChatGPT ba machine learning
    robotic ha ba inakr dg yad grftn yani b morore zaman hata behtar mishan
    
    
khob pas midonim k 70-80% e hooshe masnoee az machine learning omade
in machine learning yani chi ? goftim hoshe masnoe yani
1-yad bgire 2-mantegh kasb kone 3-tasmim bgire
chijori inkaro mikone?

machine elarning yani data driven ( mobtani bar dade)
khob yani data migire --> data ha chian?
data ha daghighan yek data frame hastan ya yek array hastan va ina
chanta radif dare ( tedade nemoone)
hameye in nemone ha chanta soton daran

dar beyne in sotonha , yekserihash vorodi hast yani (x) yani oni ke
ma mitonim taghireh bedim
va yek soton (k mamolan akharin soton) hamon khorojimon (y) hast yani hmaon
parametere mohemi k baramon moheme va oon parametere mohemo mikhaym
besanjim ya .....
khob pas midonim k in x o y beham bastegi daran yani y fght marbote b x
ba taghire x , yek rabete ee beyne x o y hast k y ham taghir mikone nesbat
be hamoon rabete.
mesal: y=2x+1 yani age x=0 bashe, y mishe 1/ hala x o taghir bdi
ba hamin formol y ham taghir mikone pas beyne y va x yek rabete hast
va in rabete hamin formoool hast.

mesale pazhoheshi:
    dar har reshte ee ma dastgahi darim ke yek setting dare ke ma mitonim
    taghiresh bedim va in yechizi khoroji mide k hala khorojish yek adade
    moheme ya oon khoorji ma yek moalefe ee azash ro baraye sanjidane 
    quality (keifiatesh) ya behaviour(raftaresh) dar nazar migirm
    
    masalan dastgahe 3d printing yek chizi dre yek setting ke mitoni
    taghiresh bdi. yek adade beyne 300 ta 400 mitoni taghir bdi
    'taghir'= pas yani in parameter vorodimone (x)
    
    khob ma ba in dastgah masalan ostokhone masnoe, ya organ haye
    masnooe misazim. khob in jesme masnoee ke ma misazim ehtemalan
    mitonim moshakhasate moshakhasi ro biaym azash dar nazar 
    begirim ( characterization) ta betonim befahmim keifiatesh chijorie
    (quality).
    khob in yani khorojimone (y), masalan estehkamesho mikhaym bbinim
    mishe y
    
    khob pas ma yek setting drim taghiresh midim (x emon) k az 300 ta
    400 mtionim taghiresh bedim va module e estehkamesh ham ma mikhaym
    bbinim har dafe ke setting avaz mishe (x) dar asl ostokhoni k sakhte mishe
    estehkamesh baz frgh dre (y)
    
    khob ma miaym hododan 10 ta setting dr nazar migirm hey azmayesh mikonim
    hey khorojiro k estehkamesh has ro misanjim
    yani masalan setting ro 10 ta adad mizarim , 300,310,320,330,340
    350,360,370,380,390
    khob har dafe k setting avaz mishe ehtemalan estehkam avaz mishe
    masalan settinge dastgah ro mizrim 310, estehkam mishe 10000
    bad mikonim 330 masan mishe 20000
    pas datamon chi mishe ? DATA chie?
    yek Data Frame hast k 10 ta radif dare ( tasavoresh konid)
    chera 10 radif? choon 10  ta nemone drim dg yani 10 bar azmayesh ro 
    anjam dadam
    khob in dah radif dota soton dare 
    yek soton settingemone (300-400) hamon x hamon vorodimon
    yek soton estehkmemone yani hamonn y hamn khoroji
    
    data=pd.DataFrame([[300,2000],[310,2300],[320,2600],[330,2800],
                       [340,2900],[350,3200],[360,3400],[370,3600],
                       [380,3800],[390,4000]],
                      columns=['Setting(x)','Estehkam(y)'])
    ino run bznid mishe data framemon dgahighan
    
    khob pas data yani x darim o y [** x ha mitone masalan 3,4 ta soton bashe
                                    yani masalan 3,4 ta setting drim]
    
    hooshe masnooe miad in rabete ye beyne x o y ro yad migire.(chijori?->migim alan)
    khob vaghty in rabete ro yad migire mitone pishbini kone va tasmim bgire
    pas 1-yad grft (az data ha) 2-moadel sakht(mantegh yad grft)3-bar hasbe manteghesh
    mitone pishbni kone (tasmim bgire o amal kone)


    khob khorojimon do no hast 1- mesle mesale bala adade peyvaste yani 
    1230,323032,21231,313,311 ya hata 14,14.22,14.7,14.9
    be in khoroji ha be mosheklemon migim regression

    hala bazi jaya x hamon hamone ama y emon khorojimon adadi nist
    balke masalan mikhaym begim in ostokhon ha gorohe 'a' bazia gorohe
    'b' yani oon 10 ta ostokhon ya gorohe a hastan ya gorohe b

    ya masalan aya mishakann ya na ag beshkanan (yes) ag nashkanan (no)
    ya a o b o yes o no k frgh dnre msn begim 0 ya 1 bashan
    yani in 10 ta data ya gorohe 1 hastan ( gorohi k msihkanan) ya
    gorohe 2 hastan ( gorohi ke ghavian nemishkanan)

    mesal:
        data=pd.DataFrame([[300,'yes'],[310,'no'],[320,'no'],[330,'yes'],
                           [340,'no'],[350,'no'],[360,'yes'],[370,'yes'],
                           [380,'yes'],[390,'no']],
                          columns=['Setting(x)','mishkane?(y)'])
    khob age khoroji gosaste bashe yani maasalann chantae chantae
    khob be in problem ha migan classification (daste bandi)
    

Kholase (summary):
    machine learning yani machine biad az data(?) yad begire(?)va
    
    data chie? yekseri x dare yani vorodi yani chizi k taghiresh 
    mitonim bedim . yekseri y dare yani khoroji yani chize nahaee k moheme
    baramon. va midonim x o y baham yek rabete ee daran yani ag
    x ro taghir bdim y taghir mikone
    
    khob khorojimon ag peyvaste bood --> regression
    age khorojimon gosaste bood---> classification
    


khob berim bebinim regression chie?
***in regressione sadast rabti b hooshe masnooe ndre
#oon bala regression va classification yani regression va classifcione e
hoshe masnooeee/

ama alan mikhaym rajebe regressione sade harf bezanim bebinim chie



Farz konid yek microbubble darim, yani chi yani yek hobabe kheyli kochik
darim ke in hobab ro mikhaym bahash karaee konim. in hobab az esmesh malome
hobabe, yani zood mitereke. yek azmayeshi darim k feshar behesh emal mikonim
yani mizarimesh zire press va miterekonimsh, ye adad mide in dastgah be name
omega. omega yani cheghad tahamol dare in microbubble, hrchi balatar bashe in
omega yani hobabe ghavi tare, yani tahamole bishtari dare yani paydarie
fesharesh bala hast.
ama avalin test ke migirm rooye yek hobab behemon 200 midde omega ke in adad
kheyli kame.
ma nemitonim ba in moghavemato paydari az hobab ha estefade konim dr donyaey vaghe ei
application o karbordesh chie? masalan mikhan toye hobab daroo bezaran bere too
badan. ya azash estefade konan toosh nano mavad ro besazan ya masalan toosh
baraye haffario CO2 captur o ina estefade beshe.
motasefane dar tamame in application ha bayad paydar bashe va khode hobab
age bezarim too kar yeho mitereke.
vase hamin ma miaym tooye in hobab ha yechizi bename 3D graphene mizarim
yani yek made ee fek konid chanta noghte o mavade kochik hast
tazrigh mikonim dakhele micro hobab ha ta paydarish bere bala.

midonim ke khode microbubbl khob dakhelesh graphene nist az aval yani dar asl
0% graphene toshe. khob ma chan drsad graphene toosh vared konim?
aya 10 %? aya 80%? chii?
nemishe goft.
choon shayad masalan age 10 darsad berizim moghavemat ziad she
ama age masalan 40 darsasd berizim. momkene sangini ijad kone toye hobab
va hobab ro beterkone pas yani moosalaman ba afzayeshe graphene hatman
paydari afzayesh nemiabad.
pas yek rabete ee beyne darsade geraphene va paydarie fesharie bubble ha hast.

ma mitonim darsade geraphene ro 'tagghir bdim'--> yani settingesho taghir
bdim->yani in vorodimone --> yani in X emone.
vasamon paydarie feshari ke hamon omega hast moheme--> keifiate nahaee ro
moshakhas mikone--> pas in khorojimone --> yani Y hast

pas ye x o y darim k harmoghe x ro taghir bdim y ham taghir mikone va nemidonim
ke rabete beyne x o y chie daghighan khob ma donbale yek machine hastim ke
betoone in 'rabete' beyne  x o y ro 'yad begire'.

khob khorojimon choon omega hast va peyvaste hast yani 3000,34324,1231 yani
moshekelmon chie ? machine learning regression.

ghabl az inke varessh beshim mikhaym bedonim khode regression che mani ee mide
badesh berim soraghe machine learning regression chon in dota frgh daran.


dar regression, in miad mige khob ma panja dade darim

x=np.array([0,4,8,16,32])
y=np.array([200,310,420,560,630])
ya hata mitone besorate excelo dataframe bashe :
    data=pd.DataFrame([[0,200],[4,310],[8,420],[16,560],[32,630]],columns=['darsad','paydari'])
    #injori x o yemon mishe har kodom az sotonash --> access
    x=data['darsad']
    y=data['paydari']
    
    
baraye rasmesh do rah drim:
    1-plt.scatter(x,y)
    ya
    2-plt.plot(x,y,'o')



rasmehs konido bebinidesh. khob ma midonim ke vaghty x emon yeki az 0 ,
4,8,16,32 bashe khob midonim chie y emon ama khob age bekhaym bbinim x emon 10 bashe
chi?? --> daronyabi behesh migan

age bekhaym bbinid masalan 40 darsad geraphene , paydari chghd mishe ?
behehs migan boron yabi.

khob sade tarin kar ine k biam noghat ro beham dg vasl konim:
    plt.plot(x,y)
khob moshkel ine ke fk konid khodeoton mikhayd har noghte ro b enoghte dg vasl konid
mesle shekle bala
khob vase noghte 40,50 ya balatar mikhayn noghte 32 ro b chi vasl konid?
pas yani boron yabi nmitoni ba inkar konid


#***********************
regressione sade miad mige:

mige bebinid man bekham yek khat bekesham. formole yek khat mishe in
Y=aX+b

mitonid rasm konid bbini

masalan:
    
    x=np.arange(5)
    a=1
    b=1
    y=a*x+b #y=x+1
    plt.plot(x,y)
    
    --------
    x=np.arange(5)
    a=1
    b=0
    y=a*x+b #y=x
    plt.plot(x,y)
    
    --------
    x=np.arange(5)
    a=2
    b=0
    y=a*x+b #y=2x
    plt.plot(x,y)
    
    --------
    x=np.arange(5)
    a=3
    b=4
    y=a*x+b #y=3x+4
    plt.plot(x,y)
    
    
    -----------------------------
    
khob ma faghat ba taghire a va b mitonim hezaran khat bekeshim.
regression mige man miad 1000 ta khat rasm mikonam ba taghire a o b.
chijori? miad aval yek hads mizne yani miad hsansi yek a o b entekhab mikone
masalan a=4 , b=2 masalan formol mishe y=4*x+2 va in khat ro rasm mikone
va haminjori be tartib a o b ro hey rasm mikone.
(soal?= khob chera inhame kaht rasm mkone? ke chi?)

mige man miad inkaro mikonam bad har khat ke rasm krdm . miad faseleye
har noghte ro ta in khat migiramesh R.
badesh vase inke kole fasele haro bebinam
zigma= R1**2 + R2**2 +......
pas in tabeye zigma omade faselehame noghat ro ta in khat hesab krde
be in tabe migan --> cost function

bad inghd hey a o b ro taghir mdie inghd mizare hesab mikone
va paeeen tarin zigma yani chi? paeen tarin zigmna yani
oon khati k paeen tarin zimgma ro dre yani b hame noghat nazdikk tre az beyne
hame khat ha

pas b in kar migan --> optimization ( behine sazi)

pas ba in kar mitone yek khat bedast biare ke a o b sh ro peyda krde
(chijori? hzarta a o b avaz krde hey zigma ro hesab krde
 az beyne oonhame khat oon khati ke kamtarin zigma ro dre omde
 dide ke a o b ish chie va gofte hala in khat
 masalan y=ax+b khate awlie mane)

dg bejaye oon panja noghte ma in khato drim y=ax+b
masaan fk kon a=1 , b=2 in kamtarin fasele ro dashtan ba noghat

miad mige azin bebad har noghte ee
har noghte ( yani beyne range daroon bashe masalan 10 k beyne 8 o 16 e)
ya biron az baze ( yani masalan 40)

mitoni b onvane x bzari too in formol va bdast biari y ro.


ba inkar oomad dar asl yek khat drovord
in khat chie???
nazdiktrin khat be noghat.
khat yani chi?--> yani formol yani hamon y=ax+b
pas dar asl chikar krde??-->omade 'rabete ' beyne x o y ro ' yad gerefte'
in kar kare hosh masnoe nis?



pas hala fahmidim chetro ba riazio amar yek model mitone rabete beyne x o y
ro yad bgire.


hala in regressione sade hast.

regresione machine learning chie???

jalase bad sohbat mishe



Alipilehvar1999@gmail.com
ai.course22.alipilehvar@gmail.com


GOOD LUCK!!!!!!
