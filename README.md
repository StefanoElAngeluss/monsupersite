# monsupersite

## requirements.txt
* asgiref==3.6.0
* Django==4.1.7
* Pillow==9.4.0
* sqlparse==0.4.3
* tzdata==2023.2
* django-ckeditor==6.5.1
* django-extensions==3.2.1
* django-js-asset==2.0.0

#### Créer un fichier requirements.txt s'il n'existe pas pour ajouter les extensions ou api à ajouter dans le projet.
* pip freeze -r requirements.txt
#### si le fichier requirements.txt existe entrer la commande suivant dans votre terminal.
* pip install -r requirements.txt

#### Commande Terminal
* py -m ensurepip --upgrade
* python.exe -m pip install --upgrade pip
* source env/Scripts/activate

## Utiles
#### Néttoyer la migrations.
* rm -rf blog/migrations/*
#### Supprimer les .pyc
* find . -path "*/migrations/*.pyc"  -delete
#### Supprimer toutes les migrations.
* find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

#### Vous pouvez supprimer votre base de données.
* python manage.py makemigrations
* python manage.py migrate
* python manage.py migrate --run-syncdb

#### Si vous avez supprimé tous les fichiers et tables de migration.
* python manage.py makemigrations nom de l'application
* python manage.py migrate nom-de-l'application

### Supprimer des lignes de cette application de django_migrations table
* python manage.py migrate nom-de-l'application --fake-initial
