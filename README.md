# Django 3 !
**I am learing from there** : 
[Python and Django Full Stack Web Developer Bootcamp](https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/)

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


 ## Database :
### Models :
- `python manage.py migrate`
- `python manage.py makemigration app_name`
- `python manage.py migrate`

### create superuser :
- `python manage.py createsuperuser`


### Use bootstrap in django forms

- install crispy : `pip
 install django-crispy-forms`
- [Documentation](https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html) 

## Password Authentication 
- install Bcrypt : `pip install bcrypt`
- install Django Argon : `pip
 install argon2-cffi`


 ### Important Documentations :
- [Getting Started](https://docs.djangoproject.com/en/3.0/)
- [Form and field validation](https://docs.djangoproject.com/en/3.0/ref/forms/validation/?fbclid=IwAR31WkOA0nKRSUIJ9mCU3MnkF7d_jwIMZstbA6tEeo-j2A6ISz-Pk0NS_no)
- [Validators](https://docs.djangoproject.com/en/3.0/ref/validators/)
- [clean](https://kite.com/python/docs/django.db.models.Model.clean)
- [Model field reference](https://docs.djangoproject.com/en/3.0/ref/models/fields/)
- [Custom Template](https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/)
- [The Django template language](https://docs.djangoproject.com/en/3.0/ref/templates/language/)
- [Django’s Templates](https://djangobook.com/mdj2-django-templates/)
- [#27956 closed Bug (fixed)](https://code.djangoproject.com/ticket/27956)
- [Template Filter](https://docs.djangoproject.com/en/3.0/topics/templates/#filters)
- [Built-in filter reference](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#ref-templates-builtins-filters)
- [Writing custom template filters](https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/#howto-writing-custom-template-filters)
- [How to Use Bootstrap 4 Forms With Django](https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html)
- [form.as_p](https://teamtreehouse.com/community/what-is-advantage-of-formasp)
- [Password Authentication](https://docs.djangoproject.com/en/3.0/topics/auth/passwords/)