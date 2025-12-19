@echo off
cd /d "D:\College AIML\4th year\sem7\IIC - Django\IIC-Django\IIC"
call .\env\Scripts\activate

start "" http://localhost:8000
python manage.py runserver
pause