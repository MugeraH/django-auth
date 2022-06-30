# Django Auth Lesson

# Description

A simple application demonstarting one of the ways django handles
authentication and access control for users

# Preview
https://user-images.githubusercontent.com/73559321/151102012-5a572faa-7904-4685-8a57-f541e833e556.mp4

## Author

[Mugera Hughes](https://github.com/mugerah/)

## Behaviour Driven Development (BDD)

1. Sign Up

| Behaviour              |                Input                 |                               Output |
| ---------------------- | :----------------------------------: | -----------------------------------: |
| Allow user to register | user details email,username,password | User account and profile are created |





2. Login

| Behaviour                                |         Input         |                                                                                                                         Output |
| ---------------------------------------- | :-------------------: | -----------------------------------------------------------------------------------------------------------------------------: |
| Allow user to login into the application | Username and password | If user is registered and has correct credentials he/she is redirected to the home page based on their user Access credentials |

## TESTING APPLICATION
### SAMPLE CREDENTIALS
username: super
password: Pass2020

username: Admin
password: Pass2020

username: User
password: Pass2020

## Setup/Installation Requirements

### Getting the code

1. clone repository
   https://github.com/MugeraH/django-auth.git
2. Move to the folder and install requirements
   cd django-auth
   pip install -r requirements.txt

### Database

1. Set up Database,and put your username and password in the code

2. Make migrations
   python3 manage.py makemigrations awwards

3. Migrate
   python3 manage.py migrate

### Running the Application

1. Run main apllication

   - python3 manage.py runserver

## Technologies Used

- Python3
- Django 3.2
- Bootstrap
- PostgreSQL
- CSS
- Heroku

## Contact Information

For any further inquiries or contributions or comments, reach me at [Mugera Hughes](https://github.com/MugeraH)

### License

[MIT License](https://github.com/MugeraH/django-auth/blob/main/license)

Copyright (c) 2021
