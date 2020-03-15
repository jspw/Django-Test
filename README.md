# Django 

## Creating a virtual setup for Django
- [install conda (miniconda or anaconda)](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html)
- `conda create --name env_name django`
- `conda activate env_name`

### Create new project 
- `django-admin startproject project_name`

- `cd project_name`

#### Create application (you can create as many applications under a project)
  
- `python manage.py startapp app_name`

 **start project** : `python manage.py runserver`