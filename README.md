# Library-Management-System

For Windows system only

Run a SQL Server using a client or SQL shell in your system with the following credentials
         NAME': 'SQL_database' 
        'USER': 'root' 
        'PASSWORD': 'root'
        'PORT': '3306'
        
Now download the project.

Execute the command "pip install -r requirements.txt" at /Library-Management-System path (relative path) to download all the dependencies from the internet. 

Execute the command "python manage.py makemigrations".

Execute "python manage.py migrate" at the same path.

Now, for running the app, execute "python manage.py runserver".

The app can be used at http://127.0.0.1:8000 in your web broswer.

Note: Before doing all the above, python needs to be installed in the system with the environment variables added. 
