cd venv/Scripts
call activate.bat
cd ..
cd ..
cd website
start cmd.exe /k python manage.py runserver
call timeout 3
start http://127.0.0.1:8000/master/