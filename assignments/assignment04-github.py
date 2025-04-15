import os
from git import Repo 

REPO_URL = "https://github.com/vinnycascone/Vincenzo-assignment4" #github link to the repository
LOCAL_DIR = "/Users/vincenzocascone/Desktop/Vincenzo-assignment4" #cloning the repository on the computer
TARGET_FILE = "textfile.txt" #path where the file to change is located
YOUR_NAME = "Vincenzo"
# Cloning the repo if not already cloned
if not os.path.exists(LOCAL_DIR):
    Repo.clone_from(REPO_URL, LOCAL_DIR)
# Opening the repo
repo = Repo(LOCAL_DIR)
file_path = os.path.join(LOCAL_DIR, TARGET_FILE)
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
content = content.replace("Andrew", YOUR_NAME)
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(content)
# Staging the file, committing the change, and pushing
repo.git.add(TARGET_FILE)
repo.index.commit(f"Replace 'Andrew' with '{YOUR_NAME}'")
origin = repo.remote(name='origin')
origin.push()