# -*- coding: utf-8 -*-
import random 
from enum import Enum
import uuid



class Creature(Enum):
    Sheep, Cow, Chicken, Rooster, Wolf, Lion, Hunter = range(7)
    
    @classmethod
    def get_creature(cls):
        return random.choice([Creature.Chicken.value, Creature.Rooster.value])
     
class Gender(Enum):
    Female = 0
    Male = 1

    @classmethod
    def get_gender(cls):
        return random.choice([Gender.Female.value, Gender.Male.value])

def MoveX(ValueX, Move):
    """çift ise ileri, tek ise geri gidecek"""
    rdValue = random.randint(0, 100)    
    """ 1) rdValue çift ise ve X koordinat değeri + Hareket edebileceği birim toplamı 500'e eşit veya düşükse canlı +x ekseninde ilerlemektedir."""
    """ 2) rdValue çift ise ve X koordinat değeri + Hareket edebileceği birim toplamı 500'den büyükse canlı -x ekseninde ilerlemektedir."""
    """ 3) rdValue tek ise ve X koordinat değeri - Hareket edebileceği birim farkı 0'a eşit veya büyükse canlı -x ekseninde ilerlemektedir."""
    """ 4) rdValue tek ise ve X koordinat değeri - Hareket edebileceği birim farkı 0'dan küçükse canlı +x ekseninde ilerlemektedir."""    
    
    if ((rdValue % 2 ==0) & (ValueX+Move<=500)) :
        ValueX = ValueX + Move
        """print("1. adım ileri gider")"""
    elif ((rdValue % 2 == 0) & (ValueX + Move > 500)):
        ValueX =  ValueX - Move
        """print("2. adım geri gider")"""
    elif ((rdValue % 2 == 1) & (ValueX - Move >= 0)):
        ValueX = ValueX- Move
        """print("3. adım geri gider")"""
    elif ((rdValue % 2 == 1) & (ValueX - Move < 0)):
        ValueX = ValueX + Move
        """print("4. adım ileri gider")  """      
    return(ValueX)

def MoveY(ValueY, Move):
    """çift ise ileri, tek ise geri gidecek"""
    rdValue = random.randint(0, 100)    
    """ 1) rdValue çift ise ve Y koordinat değeri + Hareket edebileceği birim toplamı 500'e eşit veya düşükse canlı +y ekseninde ilerlemektedir."""
    """ 2) rdValue çift ise ve Y koordinat değeri + Hareket edebileceği birim toplamı 500'den büyükse canlı -y ekseninde ilerlemektedir."""
    """ 3) rdValue tek ise ve Y koordinat değeri - Hareket edebileceği birim farkı 0'a eşit veya büyükse canlı -y ekseninde ilerlemektedir."""
    """ 4) rdValue tek ise ve Y koordinat değeri - Hareket edebileceği birim farkı 0'dan küçükse canlı +y ekseninde ilerlemektedir."""
    if ((rdValue % 2 ==0) & (ValueY+Move<=500)) :
        ValueY = ValueY + Move
        """print("1. adım ileri gider")"""
    elif ((rdValue % 2 == 0) & (ValueY + Move > 500)):
        ValueY =  ValueY - Move
        """print("2. adım geri gider")"""
    elif ((rdValue % 2 == 1) & (ValueY - Move >= 0)):
        ValueY = ValueY- Move
        """print("3. adım geri gider")"""
    elif ((rdValue % 2 == 1) & (ValueY - Move < 0)):
        ValueY = ValueY + Move
        """print("4. adım ileri gider")   """     
    return(ValueY)

def AnimalKillByHunter(dataList):
    KillAnimalList = []  # ölen canlıların Id'lerinin listesi    
    # KillHunterList = [] 
    for i in range(len(dataList)):
        """ Avcının koordinatlarını 2 değişkende saklıyoruz"""
        if dataList[i]["Creature"] == Creature.Hunter.value:
            HunterXaxis = dataList[i]["Xaxis"] 
            HunterYaxis = dataList[i]["Yaxis"] 
            
    for i in range(len(dataList)): 
          
        """avcı kendini avlayamacağı için eğer koordinat değerlerinden biri 0 olursa döngüden çıkılır."""
        if (abs(dataList[i]["Xaxis"] - HunterXaxis) == 0) or (abs(dataList[i]["Yaxis"] - HunterYaxis) == 0):
            break
        """Canlı listesindeki canlılar ile avcı arasında mesafe x veya y yönünden herhangi birine 8 birim veya daha yakınsa o canlı ölen canlı listesine aktarılmaktadır."""
        if (abs(dataList[i]["Xaxis"] - HunterXaxis)<=8) or (abs(dataList[i]["Yaxis"] - HunterYaxis)<=8) :
            KillAnimalList.append(dataList[i])
            
    """Öldürülen canlılar listesindeki canlılar tek tek ana listeden silinmektedir."""
    for i in range(len(KillAnimalList)):
               
        for k in range(len(dataList)):
            
            if (KillAnimalList[i]["Id"] == dataList[k]["Id"]):
                # print("Id:{}, index:{}".format(dataList[k]["Id"],k))
                del dataList[k]
                break

    return dataList #, KillHunterList     
    

def AnimalKillByLion(dataList):
    
    SheepCowList = [] # koyun ve ineklerden oluşan liste
    KillSheepCowList = [] # Ölen canlıların listesi
    LionList = [] # Aslanların listesi    
    
    for i in range(len(dataList)):
        
        """ inekler ve koyunlar bir listede, aslanlar bir listede toplatıldı"""        
        if (dataList[i]["Creature"] == Creature.Sheep.value) | (dataList[i]["Creature"] == Creature.Cow.value):            
            SheepCowList.append(dataList[i])
            
            """aslanların ve koyun-inek listeleri oluşturuldu"""
        elif ((dataList[i]["Creature"]) == Creature.Lion.value):            
            LionList.append(dataList[i])    
    
    """Ölecek canlıların listesindeki hayvanlar tek tek Aslanlar ile x ve y koordinatları hesaplanır. Eğer uzaklıklardan birisi 5 birim veya yakın ise 
    o canlı aslan tarafından yenmekte. Ölen canlı ölü canlılar listesinde aktarılır. """  
    
    for k in range(len(SheepCowList)):         
        for i in range(len(LionList)):   
            
            """aslanların öldürdüğü liste oluşturulur"""
            
            if abs(SheepCowList[k]["Xaxis"] - LionList[i]["Xaxis"]) <= 5 or abs(SheepCowList[k]["Yaxis"] - LionList[i]["Yaxis"]) <= 5:
                # print("öldüren aslan {}, öldürülen hayvan:{} ".format(i,k))          
                
                """ ölen canlı tekrar öldürülüp ölü canlılar listesine aktarıldığı için bu şekilde bir kontrol kodu uygulandı.
                Eğer ölü canlılar listesindeki canlının Id'si Ölecek olan canlılar listesindeki Id ile aynı ise bu canlı ölü canlılar listesinden silinmektedir."""                  
                for j in range(len(KillSheepCowList)):                    
                    if KillSheepCowList[j]["Id"] == SheepCowList[k]["Id"]:                        
                        del KillSheepCowList[j]
                        break
                """ölü koyun ve ineklerin listesi"""                    
                KillSheepCowList.append(SheepCowList[k])
                
    """ ölen canlı, bütün canlıların bulunduğu listeden silme işlemi uygulanmaktadır."""
                     
    for i in range(len(KillSheepCowList)):    
        for k in range(len(dataList)):
            
            if KillSheepCowList[i]["Id"] == dataList[k]["Id"]:
                del dataList[k]
                break
 
    return dataList #, SheepCowList, LionList,  KillSheepCowList
            
def AnimalKillByWolf (dataList):
    
    AnimalList = [] # ölecek canlıların listesi
    DeadAnimalList = [] # Ölen canlıların listesi
    WolfList = [] # kurtların listesi
    
    """ölebilecek hayvanların ve kurtların listesi oluşturuldu"""
    for i in range(len(dataList)):
        
        """ölecek hayvanlar listesinde koyun, tavuk ve horozdan oluşuyor"""
        if (dataList[i]["Creature"] == Creature.Sheep.value or dataList[i]["Creature"] == Creature.Chicken.value or dataList[i]["Creature"] == Creature.Rooster.value ):
            AnimalList.append(dataList[i])
            
            """sadece kurtların olduğu bir liste oluşturulur"""    
        elif dataList[i]["Creature"] == Creature.Wolf.value :
            WolfList.append(dataList[i])
    
    for i in range(len(AnimalList)):        
        for k in range(len(WolfList)):
            """ölebilecek canlı listesindeki canlılar tek tek kurtlara x ve y eksenindeki uzaklıkları hesaplanır. 
            Uzaklık 4 birim veya daha yakın ise o canlı ölü canlı listesine aktarılmaktadır."""
                        
            if abs(AnimalList[i]["Xaxis"] - WolfList[k]["Xaxis"]) <= 4 or abs(AnimalList[i]["Yaxis"] - WolfList[k]["Yaxis"]) <=4 :
                
                """ ölen canlı tekrar öldürülüp ölü canlılar listesine aktarıldığı için bu şekilde bir kontrol kodu uygulandı.
                Eğer ölü canlılar listesindeki canlının Id'si Ölecek olan canlılar listesindeki Id ile aynı ise bu canlı ölü canlılar listesinden silinmektedir."""
                for j in range(len(DeadAnimalList)):                    
                    if DeadAnimalList[j]["Id"] == AnimalList[i]["Id"]:                          
                        del DeadAnimalList[j]
                        break
                    
                DeadAnimalList.append(AnimalList[i])
                # print("öldüren kurt {}, öldürülen hayvan:{} ".format(k,i)) 
    """ölen hayvanları listeden silme işlemi"""
    for i in range(len(DeadAnimalList)):        
        for k in range(len(dataList)):
            
            if DeadAnimalList[i]["Id"] == dataList[k]["Id"]:
                del dataList[k]
                break           
    
    return dataList , AnimalList #AnimalList, WolfList , DeadAnimalList,       

def AnimalDuplication(dataList):
    """Hayvan üretme fonksiyonu"""
    FemaleList = [] # Dişi cinsiyetin listesi
    MaleList = [] # Erkek cinsiyetin listesi
    NewLifeList = [] # Yeni doğan hayvanın listesi

    """ Cinsiyete göre listelere ayrıldı"""
    for i  in range(len(dataList)):
        
        if dataList[i]["Creature"] == Creature.Hunter.value:
            break   
        """ avcı üreyemediği için listeden avcıyı çıkarttık"""
        
        """ Dişi hayvanları bir listede topladık"""        
        if dataList[i]["Gender"] == Gender.Female.value:            
            FemaleList.append(dataList[i])
            
            """ Erkek Hayvanları bir listede topladık"""
        elif dataList[i]["Gender"] == Gender.Male.value:
            MaleList.append(dataList[i])
            
    for i in range(len(FemaleList)):
        
        for k in range(len(MaleList)):
            """ uygulanan yöntem Dişi ve Erkek listedeki hayvanlar içerisinden aynı türdeki hayvanların üzerinden işlem yapılmaktadır.
            Eğer dişi bir canlıya erkek 3 birim veya daha yakın olursa aynı türde yeni bir canlı meydana gelmektedir. Bu canlının cinsiyeti
            random olarak belirlenmektedir."""
            
            if FemaleList[i]["Creature"] == Creature.Sheep.value and MaleList[k]["Creature"] == Creature.Sheep.value:             
                
                if abs(FemaleList[i]["Xaxis"] - MaleList[k]["Xaxis"]) <=3 or abs(FemaleList[i]["Yaxis"] - MaleList[k]["Yaxis"]) <= 3:                
                    
                    Data = {"Id": uuid.uuid1(),
                            "Creature": Creature.Sheep.value,
                            "Gender": Gender.get_gender(),
                            "Xaxis": random.randint(0,500),
                            "Yaxis": random.randint(0,500),
                            "Move" : 2}
                        
                    NewLifeList.append(Data)

            elif FemaleList[i]["Creature"] == Creature.Cow.value and MaleList[k]["Creature"] == Creature.Cow.value:               
                
                if abs(FemaleList[i]["Xaxis"] - MaleList[k]["Xaxis"]) <=3 or abs(FemaleList[i]["Yaxis"] - MaleList[k]["Yaxis"]) <= 3:
 
                    Data = {"Id": uuid.uuid1(),
                            "Creature": Creature.Cow.value,
                            "Gender": Gender.get_gender(),
                            "Xaxis": random.randint(0,500),
                            "Yaxis": random.randint(0,500),
                            "Move" : 2}
                        
                    NewLifeList.append(Data)

            elif FemaleList[i]["Creature"] == Creature.Wolf.value and MaleList[k]["Creature"] == Creature.Wolf.value:               
                
                if abs(FemaleList[i]["Xaxis"] - MaleList[k]["Xaxis"]) <=3 or abs(FemaleList[i]["Yaxis"] - MaleList[k]["Yaxis"]) <= 3:
 
                    Data = {"Id": uuid.uuid1(),
                            "Creature": Creature.Wolf.value,
                            "Gender": Gender.get_gender(),
                            "Xaxis": random.randint(0,500),
                            "Yaxis": random.randint(0,500),
                            "Move" : 3}
                    NewLifeList.append(Data)
                    
            elif FemaleList[i]["Creature"] == Creature.Lion.value and MaleList[k]["Creature"] == Creature.Lion.value:               
                
                if abs(FemaleList[i]["Xaxis"] - MaleList[k]["Xaxis"]) <=3 or abs(FemaleList[i]["Yaxis"] - MaleList[k]["Yaxis"]) <= 3:
 
                    Data = {"Id": uuid.uuid1(),
                            "Creature": Creature.Lion.value,
                            "Gender": Gender.get_gender(),
                            "Xaxis": random.randint(0,500),
                            "Yaxis": random.randint(0,500),
                            "Move" : 4}                    
                        
                    NewLifeList.append(Data)
                """ Tavuk ve  Horoz çiftleşmesinden random şekilde tanımlanmadıktadır. Yaratılan tavuk ise cinsiyet dişi; horoz ise erkek olarak oluşturulmaktadır"""    
            elif FemaleList[i]["Creature"] == Creature.Chicken.value and MaleList[k]["Creature"] == Creature.Rooster.value:               
                
                if abs(FemaleList[i]["Xaxis"] - MaleList[k]["Xaxis"]) <=3 or abs(FemaleList[i]["Yaxis"] - MaleList[k]["Yaxis"]) <= 3:
                    
                    Animal = Creature.get_creature()
                                        
                    if Animal == Creature.Chicken.value :                        
                        GenderBird = Gender.Female.value
                    elif Animal == Creature.Rooster.value :
                        GenderBird = Gender.Male.value  
                        
                    Data = {"Id": uuid.uuid1(),
                            "Creature": Animal,
                            "Gender": GenderBird,
                            "Xaxis": random.randint(0,500),
                            "Yaxis": random.randint(0,500),
                            "Move" : 1}
                    
                    NewLifeList.append(Data)
                    
    """ oluşturulan canlıların listesi ana listeye aktarılmaktadır."""                 
    for i in range(len(NewLifeList)):
        dataList.append(NewLifeList[i])

    return dataList #FemaleList, MaleList, NewLifeList
            
    

    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            