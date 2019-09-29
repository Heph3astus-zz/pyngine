import importlib

class Scene:

    setScene = False
    staticObjects = {}
    physicsObjects = {}
    staticObjList = []
    physicsObjList = []

    def __init__(self, dir):
        #defining all objects
        for objName in self.staticObjList:
            gameMod = importlib.import_module("gameObjects." + objName,dir)
            gameClass = getattr(gameMod,objName)
            gameObj = gameClass()
            self.staticObjects.update({objName: gameObj})
        for objName in self.physicsObjList:
            gameMod = importlib.import_module("gameObjects." + objName,dir)
            gameClass = getattr(gameMod,objName)
            gameObj = gameClass()
            self.physicsObjects.update({objName, gameObj})


    def getPhysicsObjects(self):
        return self.physicsObjects
    def getStaticObjects(self):
        return self.staticObjects

    def process(self, screen):
        for obj in self.physicsObjects:
            currentObj = self.physicsObjects[obj]
            currentObj.process()
            screen.blit(currentObj.spriteImg, (currentObj.posx,currentObj.posy))

        for obj in self.staticObjects:
            currentObj = self.staticObjects[obj]
            if currentObj.change == True:
                currentObj.process()
                currentObj.change == False
            screen.blit(currentObj.spriteImg, (currentObj.posx,currentObj.posy))
