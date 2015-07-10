import os
import sys

filename = sys.argv[1]
mode = sys.argv[2]
print filename
print mode
# Text file containing all repos urls is to be fed: input as 1st arg
# There are two modes it can run:
#   - mutli thread parallel clone: input 2nd arg as 1
#   - single thread sequential clone: input 2nd arg 2 
#
# Running: python gitReposCloner.py <input_url_list_file> <mode_number>
f = open(filename, 'r')

lines = f.readlines()

totalRepoLen = len(lines)

repoList = []

for line in lines:
    repoUrl = line.split(' ')[5]
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
if mode == '1':
    threads = []
    for i in range(totalRepoLen):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
else:
    for i in range(totalRepoLen):
        git("clone", repoList[i])