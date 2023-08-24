## Set Up your personal settings
Create a `conf.py` configuration file with your personal settings in the root of the project.

File content example:
```ini
# Email connection
HOST = 'smtp.mail.ru'
PORT = 465
EMAIL = 'example@mail.ru'
EMAIL_PASSWORD = '12345678'

# DataBase connection
DB_NAME = 'mailing_manager'
DB_USER = 'postgres'
DB_PASSWORD = '12345'
```
Fill out the file according to your personal data. Create a database in postgresql. The name of the database must match the name specified in the file.
