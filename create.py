# import os and sys library to perform command line inputs
import os
import sys

# import GitHub API; install if not found
try: 
    from github import Github
except:
    os.system('pip install PyGithub')
    from github import Github
    
# import JSON library
import json

#---------------------------------------------------------------------#

# get name of new project
args = sys.argv[1:]
name = ' '.join(args)
gitPath = '-'.join(args)

# load JSON file
with open('config.json', 'r') as f:
    config = json.load(f)
    
# create new project folder locally
path = config['folderPath']
try:
    os.chdir(path)
except:
    print('Invalid Folder path.')
    exit()
os.makedirs(name)
os.chdir(path + '\\' + name)

# login into Github
user = Github(config['username'], config['password']).get_user()

# get user's login name
loginName = user.login

# create new repository
repo = user.create_repo(name)
print("GitHub Repository Created Successfully.")

# go into directory and run git commands
os.system('echo # ' + name + ' >> README.md')
os.system('git init')
os.system('git add README.md')
os.system('git commit -m "first commit"')
os.system('git remote add origin https://github.com/' + loginName + '/' + gitPath + '.git')
os.system('git push -u origin master')
os.system('code .')