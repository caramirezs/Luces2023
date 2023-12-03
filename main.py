import sys
import os
import git

main_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(main_path)

from TestPlanos import run_testplanos
csvFile = sys.argv[1]
if len(sys.argv) > 2:
    sleep_time = sys.argv[1] # en segundos
else:
    sleep_time = 0.017 # approx 60fps = 0.017
# Fetch & Pull

def git_pull():
    PATH_OF_GIT_REPO = f'{main_path}/.git'
    try:
        repo = git.Repo(PATH_OF_GIT_REPO)
        origin = repo.remote(name='origin')
        for remote in repo.remotes:
            remote.fetch()
        origin.pull()
    except:
        print('Some error occured while fetch/pull the code')

    return None


git_pull()
####

run_testplanos(csvFile, sleep_time)


