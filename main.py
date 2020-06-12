import os

## Number of days you want to make commits
for i in range(1,365*2 + 1):
    d = str(i) + ' day ago'
    ## Open a text file and modify it
    os.system('copy /b text'+i+'.txt +,,')
    ## Add bot.txt to staging area
    os.system('git add text'+i+'.txt')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')

## push the commit to github
os.system('git push -u origin master')