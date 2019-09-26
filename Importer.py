from re import sub
import os
from fnmatch import fnmatch

def importer(root):


    importFiles = []
    rootPath = os.path.dirname(os.path.realpath(__file__)) + "/" + root
    for path, subdirs, files in os.walk(rootPath):
        for name in files:
            if fnmatch(name, "*.py"):
                if not "__" in name and not root in name:
                    importFiles.append(sub(r'.*/', '/', os.path.join(path, name))[:-3][1:])
    return importFiles
