**Ayomi**

A login register and profile management app built with django and bootsrap 

**stack**
 django
 bootsrap
 docker(dockerfile docker compose)

**How to**
 
***to build the image***

  go to the root folder and ``docker compose build ``

***to start the service***

run  ``docker compose up``

***to migrate***

run these commands:
``docker-compose run  python manage.py migrate``

  ``docker-compose run  Python manage.py makemigrations``


***to create a superuser***


run  ````docker-compose run Python manage.py createsuperuser````

***to run the server***

 
run ````docker-compose run Python manage.py runserver````


***Login and registration***


once the server is launched you can  login or register 

but first register if you have no account

***profile edit***

after login, you can see your profile 
click on edit button to edit your bio or email

