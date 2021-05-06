import os
from github import Github 
g = Github("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")

repo = g.get_repo("sharmadivyam102/demo-")
list(repo.get_branches())

for i in list(repo.get_branches()):
    print(i)
os.system('git branch')