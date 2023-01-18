# powerplant-coding-challenge

*author: Jeremy Lipszyc*

*created the 18/01/2023*

## Overview

This project is part of the recrutment process of Engie. The project as to be done in 4 hours. The author use a little bit more of time, like 5 hours, to do it.

**The API is created with:**
- Django as backend framework
- Django-rest-framework as library for the API
- drf-spectacular for the swagger
- Pandas for computation

## Installation

Go to the target folder and clone the repo with:
`git clone https://github.com/jeroux/powerplant-coding-challenge.git`

the project is on the branch "master".

[Create virtual environment and active it.](https://docs.python.org/3/library/venv.html)


go in the folder
`cd powerplant-coding-challenge`

install the requirements
`pip install -r requirements.txt`

go in the engie folder
`cd engie`

create the db
`python manage.py migrate`

run the server on port 8888
`python manage.py runserver 8888`


## Usage
The documentation of the api is in the swagger.

With you browser go to the swagger at
[http://127.0.0.1:8888/swagger-ui/](http://127.0.0.1:8888/swagger-ui/)

You can use it to test the api.

If you want to use another mean, you can sent a POST request with the adequate format at
[http://127.0.0.1:8888/productionplan/](http://127.0.0.1:8888/productionplan/)