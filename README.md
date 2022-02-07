# Awwards Clone

# Description

This is an Awwwards Clone website made with Django.It allows a registered user to upload projects so that it can be rated

## Screenshot

1. Login & Register page

![image](./main/static/images/login.png)

![image](./main/static/images/register.png)

2. Landing page

   ![image](./main/static/images/home.png)

   Display projects 

   ![image](./main/static/images/display.png)

3. Project rating view

![image](./main/static/images/ratings.png)

4. Upload view

   ![image](./main/static/images/submit_form.png)

5. Search view

   ![image](./main/static/images/search.png)

## Live Link

[Awwwards Clone](https://awwwclone.herokuapp.com/)

## Author

[Mugera Hughes](https://github.com/mugerah/)

## User Story

1. View posted projects and their details.
2. Post a project to be rated/reviewed.
3. Rate/ review other users' project
4. Search for projects
5. View projects overall score
6. View my profile page

## Behaviour Driven Development (BDD)

1. Sign Up

| Behaviour              |                Input                 |                               Output |
| ---------------------- | :----------------------------------: | -----------------------------------: |
| Allow user to register | user details email,username,password | User account and profile are created |

2. Login

| Behaviour                                |         Input         |                                                                                  Output |
| ---------------------------------------- | :-------------------: | --------------------------------------------------------------------------------------: |
| Allow user to login into the application | Username and password | If user is registered and has correct credentials he/she is redirected to the home page |

3. Search Project

| Behaviour          |   Input    |                                                                                                              Output |
| ------------------ | :--------: | ------------------------------------------------------------------------------------------------------------------: |
| Search for project | searchterm | User gets redirected to search projects page where a list of projects with relation to the searchterm are displayed |

4. Post Project

| Behaviour                     |                  Input                   |                                                                                                     Output |
| ----------------------------- | :--------------------------------------: | ---------------------------------------------------------------------------------------------------------: |
| Post a ne project to be rated | Click submit project button on th navbar | User is redirected to submit project form where by he/she fills in the project details they want to submit |

5. Rate Project

| Behaviour                                  |                      Input                      |                                                                Output |
| ------------------------------------------ | :---------------------------------------------: | --------------------------------------------------------------------: |
| Click visit button on project display card | project ratings input, design,content,usability | Values are taken in and the average scores are returned and displayed |

## Setup/Installation Requirements

### Getting the code

1. clone repository
   https://github.com/MugeraH/Awwards.git
2. Move to the folder and install requirements
   cd instagram_clone
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

2. Run tests
   - python3 manage.py test photos

## Technologies Used

- Python3
- Django 3.2
- Bootstrap
- PostgreSQL
- CSS
- Heroku
- Cloudinary

## Contact Information

For any further inquiries or contributions or comments, reach me at [Mugera Hughes](https://github.com/MugeraH)

### License

[MIT License](https://github.com/MugeraH/Awwards/blob/main/license)

Copyright (c) 2021
