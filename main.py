import git
import os
currentDir = os.getcwd()
repo = git.Repo(currentDir+'/.git')


def getAllFiles(path):
    files = os.listdir(path)
    for f in files:
        repo.index.add([path+'/'+f])
        repo.index.commit(f'update {f} Solution to alogexpert problem')


getAllFiles(currentDir)
