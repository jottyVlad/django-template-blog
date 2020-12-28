# Simple template of django blog.
```sh
$ git clone https://github.com/jottyVlad/django-template-blog.git
$ cd django-template-blog
```

Let's create virtualenv and download packages from requirements.txt:
```sh
$ virtualenv env
$ source env/bin/activate
(env)$ pip install -r requirements.txt 
```

And let's run our server!
```sh
(env)$ cd django_template_blog
(env)$ python manage.py runserver
```

In the site there is an existing superuser. Login:pass is admin:admin.
To make migrations make some changes and write in console:

```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```

Good luck!
