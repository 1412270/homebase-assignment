# Homebase Assignment
This take-home assignment is designed to assess skills in backend development, with a focus on technologies such as Node.js, Python, Express, and Django. This repository contains three folders, each corresponding to a different project. The first project is a REST API server written in Node.js and Express. The second project is a web server written in Django. The third project is a Python proxy server.

## Getting Started
To get started with this project, follow these steps:

Clone this repository.  

### simple-rest-api      
Install the required dependencies:    
 - npm install express  sequelize sqlite3

Run this command to start server:   
 - node app.js  

### webserver      
Install the required dependencies:   
 - pip install -r requirements.txt     

Data migration by commnand:    
 - python manage.py migrate     

Run this command to start server:    
 - python manage.py runserver 8080     

### apiproxy    
Install the required dependencies:  
 - pip install -r requirements.txt  

Run this command to start server:  
 - python proxy.py

## Prerequisites
To run this project, you’ll need:

Node.js   
Python

## Usage
### simple-rest-api     
After started web api server, you can test CRUD operations: localhost:3000/users  
Sample User JSON data:  
{ "username": "Henri", "email": "henri@example.com", "password": "12345" }      

### webserver   
Create a supper user by command:  
 - python manage.py createsuperuser

Test CRUD operations via Django's admin interface:  
 - localhost:8080/admin/simpleapp/product/    

Fetch "User" data from the Express API via the Python proxy:   
 - localhost:8080/simpleapp/users    

## Built With
Express - A fast, unopinionated, minimalist web framework for Node.js.  
Django - A high-level Python web framework that enables rapid development of secure and maintainable websites.   
SQLite - A lightweight disk-based database that doesn’t require a separate server process.   
## Authors
Luu Tran Anh Kiet - [My LinkedIn](https://www.linkedin.com/in/kiet-luu-99a289199/)
## License
This project is licensed under the MIT License.  
