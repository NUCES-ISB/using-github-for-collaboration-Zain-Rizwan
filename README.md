Create Virtual Enviroment
python -m venv .venv

for windows
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Create gitignore and requirements.txt file

Enter Virtual Enviroment
.\.venv\Scripts\Activate.ps1

To deactivate
deactivate

show installed packages
pip freeze

Commited

install pytest
pip install pytest

To put all packages and their versions in requirement.txt
pip freeze > requirements.txt

To reinstall packages from requirements.txt 
pip install -r requirements.txt

Add functionality in test.py and app.py and check using pytest