import sys
sys.path.insert(0, '..')
from Engine import Engine
from Importer import importer

run = Engine()

run.init('testGame',200,500,'TestScene1')
