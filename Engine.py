import pygame
import importlib
import threading as t
from testGame.scenes import TestScene1
from Importer import importer

class Engine:
    screen = None
    running = True
    sceneDict = {}
    currentScene = None
    loadedPhysicsObjects = []
    loadedStaticObjects = []

    def init(self, subdir, x,y, scene):
        pygame.init()
        self.screen = pygame.display.set_mode([x,y])
        #screen.fill(255,255,255)
        #add all scenes to sceneDict
        sceneName = ""
        for sceneName in importer(subdir +"/scenes"):
            module = importlib.import_module("scenes." + sceneName,subdir)
            sceneObj = getattr(module,sceneName)
            self.sceneDict.update({sceneName:sceneObj(subdir)})
        #load default scene
        self.currentScene = self.sceneDict[scene]
        #begin game proccessing
        self._process()

    def _process(self):
        while self.running:

            #quit program
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #check for changed scene
            if self.currentScene.setScene != False:
                currentScene = self.sceneDict[self.currentScene.setScene]

            #get any new objects in scene
            physicsObjects = self.currentScene.getPhysicsObjects()
            staticObjects = self.currentScene.getStaticObjects()

            #proccessing object movements
            self.currentScene.process()

            #display all objects
        pygame.quit()
