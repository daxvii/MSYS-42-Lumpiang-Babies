Important codes for Django and Git

Navigation in Command Prompt:
cd <name of directory> to go to that directory
cd .. to go back once

Install Django:
py -m django --version (check if django is installed)
pip install django (install django)'
# Make sure to install django in your virtual environment as well

Create new virtual environment:
py -m venv <name of virtual environment>
#use venv in this case for uniformity

Activate virtual environment:
<name of virtual environment>\scripts\activate

Set up new Django project:
django-admin startproject <name of project>

Set up new Django app:
py manage.py startapp <name of app>
# Make sure you are in the directory with the manage.py file

Run server:
py manage.py runserver
# Make sure you are in the directory with the manage.py file

Migration for Django Models:
py manage.py makemigrations <app name>
py manage.py migrate
# Make sure you are in the directory with the manage.py file

Make sure to install git first and run git init in the desired directory

Clone Git project into directory:
git clone <link of Git repository>

Push to Git:
git add .
git commit -m "<message>"
git push
# Pls put a message so others know what was added or changed
# Be careful which branch you push to as reverting changes is difficult

Branch in Git:
git checkout -b <name of branch> (to create a new git branch)
git branch (to view available branches and which one you are in)
git checkout <name of branch you want to visit>
# It is common practice to never work on the main or master branch and only push to it when everything is finalized

Pull from Git:
git pull (to get any new files from git branch)

Merge from Git:
git merge <name of branch>
# Not sure if I understand it properly but I think you need to git pull both branches you want to merge then execute this command for them to properly merge, also don't delete the previous branch