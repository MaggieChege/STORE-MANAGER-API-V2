
[![Build Status](https://travis-ci.org/MaggieChege/STORE-MANAGER-API-V2.svg?branch=develop)](https://travis-ci.org/MaggieChege/STORE-MANAGER-API-V2)

[![Coverage Status](https://coveralls.io/repos/github/MaggieChege/STORE-MANAGER-API-V2/badge.svg?branch=develop)](https://coveralls.io/github/MaggieChege/STORE-MANAGER-API-V2?branch=develop)


# STORE-MANAGER-API-V2
This is Version 2 of Store Manager application. This web application stores enables the admin or attendant to make a sale and to add products that they would like to sell in their store.



# Getting Started

Setup your project  with the following steps

# Installing

Git clone this repository
``` https://github.com/MaggieChege/STORE-MANAGER-API-V2.git ```

Setup a Virtual environment at the root folder of the project
``` Virtualenv env ```

Create a .nv file and add the following variables 
``` source env/bin/activate ``` 
``` export FLASK_APP="run.py" ```

``` export FLASK_ENV="development" ```

``` export SECRET="your_secret_key" ```

``` export APP_SETTINGS="development" ```


# Install all dependencies

``` pip install -r requirements.txt ```

run the application ``` flask run ```


# Check the online Postman Documentation
https://documenter.getpostman.com/view/5420872/RzZ4p1Zi

# PIVOTAL TRACKER STORIES
https://www.pivotaltracker.com/n/projects/2209137

The follwing endoints should work

``` 1. POST /api/v2/auth/user ```


``` 2. POST /api/v2/users/login ```


``` 3. GET /api/v2/products ```


``` 4.GET /api/v2/sales ```


``` 5. GET /api/v2/<Product_id> ```


``` 6.GET /sales/<saleId> ```



``` 7.POST /products ```



``` 8.POST /sales ```


# RUN TESTS

Run unittests; ``` pytest -v ```
