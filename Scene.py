
#Interne Dateien
from Texture import *
from Entity import *
from Array import *

class Scene:

    def __init__(self):

        self.contentEntities_OBJECT         = []
        self.contentEntities_ID             = []
        self.contentEntities_TEXTURE        = []
        self.contentENtities_ATTRIBUTES     = []


    def sceneCreate_RANDOM(self, RANDOM = False, RANDOMKEY = 10):

        for i in range(RANDOMKEY):
            self.contentEntities_OBJECT.append(Entity(x = 150 + 80 * i, y = 150 + 80 * i))


    def sceneLoad(self, sceneID):

        if sceneID == "INGAME::001::001":
            self.__LOAD_instance_INGAME_001()
    

    def __sceneOVERWRITE(self, contentEntities, contentID, contentTexture, contentATTRIBUTES):

        self.__contentClear_ALL()

        for element in contentEntities:
            self.contentEntities_OBJECT.append(element)

        for element in contentID:
            self.contentEntities_ID.append(element)

        for element in contentTexture:
            self.contentEntities_TEXTURE.append(element)

        for element in contentATTRIBUTES:
            self.contentENtities_ATTRIBUTES.append(element)


    def __contentClear_ALL(self):

        self.contentEntities_OBJECT.clear()
        self.contentEntities_ID.clear()
        self.contentEntities_TEXTURE.clear()
        self.contentENtities_ATTRIBUTES.clear()


    def __LOAD_instance_INGAME_001(self):

        instance_NEW = [

            Entity(),           "PLAYER",       "NONE",     "CONTROLLABLE",
            Entity(x = 300),    "ENEMY_01",     "NONE",     "AI",
            Entity(y = 300),    "ENEMY_02",     "NONE",     "AI"       

        ]
        
        instance_FINAL = arraySplit(instance_NEW, 4)
        print(instance_FINAL)
        self.__sceneOVERWRITE(      
            
            instance_FINAL[0],  #OBJECT Komponente
            instance_FINAL[1],  #ID Komponente
            instance_FINAL[2],  #TEXTURE Komponente 
            instance_FINAL[3]   #ATTRIBUTE Komponente        
            
             )