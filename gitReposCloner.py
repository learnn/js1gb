import os

# Text file containing all repos urls is to be fed
f = open('2.txt', 'r')

lines = f.readlines()

totalRepoLen = len(lines)

repoList = []

for line in lines:
    repoUrl = line.split(' ')[1]
    repoList.append(repoUrl)
    
import threading
import subprocess

def git(*args):
    return subprocess.check_call(['git'] + list(args))

def worker(num):
    """thread worker function"""
    print 'Cloning repository: %s' % repoList[num]
    git("clone", repoList[num])
    return

# spawn worker thread for each repo clone
threads = []
for i in range(totalRepoLen):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()