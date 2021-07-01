import uuid
import random 
from methods import Creature, Gender, MoveX, MoveY, AnimalKillByHunter, AnimalKillByLion, AnimalKillByWolf, AnimalDuplication

AllCreature = []
for i in range(15):

    Data = {"Id": uuid.uuid1(),
            "Creature": Creature.Sheep.value,
            "Gender": Gender.Female.value,
            "Xaxis": random.randint(0,500),
            "Yaxis": random.randint(0,500),
            "Move" : 2}
        
    AllCreature.append(Data)

for i in range(15):

    Data = {"Id": uuid.uuid1(),
            "Creature": Creature.Sheep.value,
            "Gender": Gender.Male.value,
            "Xaxis": random.randint(0,500),
            "Yaxis": random.randint(0,500),
            "Move" : 2}

    AllCreature.append(Data)

for i in range(5):

    Data = {"Id": uuid.uuid1(),
            "Creature": Creature.Cow.value,
            "Gender": Gender.Female.value,
            "Xaxis": random.randint(0,500),
            "Yaxis": random.randint(0,500),
            "Move" : 2}

    AllCreature.append(Data)

for i in range(5):

    Data = {"Id": uuid.uuid1(),
            "Creature": Creature.Cow.value,
            "Gender": Gender.Male.value,
            "Xaxis": random.randint(0,500),
            "Yaxis": random.randint(0,500),
            "Move" : 2}

    AllCreature.append(Data) 

for i in range(10):

    Data = {"Id": uuid.uuid1(),
            "Creature": Creature.Chicken.value,
            "Gender": Gender.Female.value,
            "Xaxis": random.randint(0,500),
            "Yaxis": random.randint(0,500),
            "Move" : 1}

    AllCreature.append(Data)

for i in range(10):

    Data = {"Id": uuid.uuid1(),
            "Creature": Creature.Rooster.value,
            "Gender": Gender.Male.value,
            "Xaxis": random.randint(0,500),
            "Yaxis": random.randint(0,500),
            "Move" : 1}

    AllCreature.append(Data)    

for i in range(5):

    Data = {"Id": uuid.uuid1(),
            "Creature": Creature.Wolf.value,
            "Gender": Gender.Female.value,
            "Xaxis": random.randint(0,500),
            "Yaxis": random.randint(0,500),
            "Move" : 3}

    AllCreature.append(Data)  

for i in range(5):

    Data = {"Id": uuid.uuid1(),
            "Creature": Creature.Wolf.value,
            "Gender": Gender.Male.value,
            "Xaxis": random.randint(0,500),
            "Yaxis": random.randint(0,500),
            "Move" : 3}

    AllCreature.append(Data) 

for i in range(4):

    Data = {"Id": uuid.uuid1(),
            "Creature": Creature.Lion.value,
            "Gender": Gender.Female.value,
            "Xaxis": random.randint(0,500),
            "Yaxis": random.randint(0,500),
            "Move" : 4}

    AllCreature.append(Data)  

for i in range(4):

    Data = {"Id": uuid.uuid1(),
            "Creature": Creature.Lion.value,
            "Gender": Gender.Male.value,
            "Xaxis": random.randint(0,500),
            "Yaxis": random.randint(0,500),
            "Move" : 4}

    AllCreature.append(Data)     

Data = {"Id": uuid.uuid1(),
        "Creature": Creature.Hunter.value,
        "Gender": Gender.Male.value,
        "Xaxis": random.randint(0,500),
        "Yaxis": random.randint(0,500) ,
        "Move" : 1}

AllCreature.append(Data)

AllCreatureCopy = AllCreature.copy() 

"""random şekilde X yönünde ya da Y yönünde hareket ettir"""
AllMove = 0

while AllMove <= 1000:
    for i in range(len(AllCreature)):
        rdMove = random.randint(0,100)
        if AllMove>1000:
            """1000 birim hareket sonunda işlem biter"""
            break
        # x,y = AllCreature[i]["Xaxis"], AllCreature[i]["Yaxis"] # oluşturulan koordinatlar
        if rdMove % 2 == 0:
            """ random sayı çift ise x yönünde"""
            NewXaxis = MoveX(AllCreature[i]["Xaxis"],AllCreature[i]["Move"])
            AllCreature[i]["Xaxis"] = NewXaxis

        elif rdMove % 2 == 1:
            """ random sayı tek ise y yönünde"""
            NewYaxis = MoveY(AllCreature[i]["Yaxis"],AllCreature[i]["Move"])
            AllCreature[i]["Yaxis"] = NewYaxis
               
        AllMove = AllMove + AllCreature[i]["Move"]
        # print("Eski Koordinat={}:{}, Yeni Koordinat={}:{},----{}".format(x,y,AllCreature[i]["Xaxis"],AllCreature[i]["Yaxis"],i))        
    
    AnimalKillByHunter(AllCreature) 
    AnimalKillByLion(AllCreature)
    AnimalKillByWolf(AllCreature)
    AllCreature = AnimalDuplication(AllCreature)        

for i in range(len(AllCreature)):
    print("Id:{}, Canlı:{}, Cinyiyet:{}, Konum:{}-{}".format(AllCreature[i]["Id"],AllCreature[i]["Creature"],
                                                              AllCreature[i]["Gender"],AllCreature[i]["Xaxis"],
                                                              AllCreature[i]["Yaxis"]))
    