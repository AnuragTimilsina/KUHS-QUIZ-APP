# KUHS Quiz App
 QUIZ application made for KUHS. 

## Features

- Authentication
- Choose quiz category
- Shows quiz time taken

## Installation

Clone the repository
Create a virtual environment and install the necessary packages in environment.yml file. 
cd to the path where manage.py exists and run the following commands.

```sh
python manage.py makemigrations
python manage.py migrate

#creating superuser
python manage.py createsuperuser

#Run development server
python manage.py runserver
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```



  
