> **Warning**
Switch to another web stack [here](https://github.com/hijacque/class_timetable_web)

## Requirement
1. [Python 3](https://www.python.org/)

## Installation
### 1. Clone & go inside the repo
```sh
git clone https://github.com/jhaimecando27/sched.git
cd sched
```
### 2. Setup virtual environemnt
#### windows
```sh
 python -m venv venv         # Create virtual environment
 
 # Pick one to activate virtual environment
 env\Scripts\activate.bat    # In CMD
 env\Scripts\Activate.ps1    # In Powershell
```
#### unix (Mac/Linux)
- Make sure you have python & venv/virtualenv installed
```sh
virtualenv venv              # Create virtual environment

# Activate the virtual environemnt
source venv/bin/activate
```
### 3. Install app's requirements
```sh
pip install -r requirements.txt
```
### 4. Create any necessary database tables
```sh
cd app
python manage.py migrate
```
### 5. Run the server
```sh
python mange.py runserver
```
## Notes
- Creation ng mga account (prof & chair) ay si admin gagawa, type the following para gumawa ng admin account:
```sh
python manage.py createsuperuser
```
- Yung mga user (prof & chair) kailangan ng group para ma access yung prof/chair web pages. Para mabigyan ng group si user (prof/chair):
  - `admin` > `Users` > `<Username>` > `Permissions` > `Groups`
- About sa login security si Django na bahala dun, like example for creation ng user account i-make sure nya na strong yung password and bago ilagay sa database hina-hash nya yung password.
- Sa pag manage ng mga account may binigay na webpage si Django para dun which is for the admin pede nmn i-edit yung page na yun pero baka hassle lng. Kaya about sa pag manage ng accounts oks na lahat, pero kung may kailangan na specific na table na makikita pede nmn lagay dun.
- Si Django may binigay na default database, master list lng nmn yun, kung saan lahat ng needed info ng user like username, email, first name, etc. mga ganun, pede nmn imodify yun.
- Para ma separate yung prof & chairperson na webpage gagamit nlng ng groups (set of permisssions) para madali i handle for the admin.
- To deactivate/exit the virtual environment type `deactivate` in the terminal.
