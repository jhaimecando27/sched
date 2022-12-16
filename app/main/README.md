`views.py`
----------
- Chairperson dashboard (`profile`, `schedules`, `department`, `faculty`)
    - First of all sorry hannah hindi ko ma integrate yung [ejs](https://ejs.co/) sa django. Maganda yung nagawa nya pero hindi ko malipat yung [ejs](https://ejs.co/) to [jinja2](https://jinja.palletsprojects.com/en/3.1.x/). So dito ginawa ko nlng sya separate pages yung mga options (profile, schedules, etc.) in single page kasi nagawa nya.
- `faculty_form`
    - form na i-fifill up ng mga prof

`urls.py`
----------
- Nothing special binigyan ko lng yung mga functions sa `views.py` ng url links

`admin.py`
----------
- Dito papakita natin sa admin yung mga kailangan nila. Sa nagawa ko pinakita ko lng yung specific table sa database sa admin page. Kaya sa admin page may makikita kayo na "Availability", "Courses" mga ganun, mga table yun sa database.
- Yung `list_display` yun yung mga columns sa table na ipapakita.

`forms.py`
----------
- `facultyForm`
    - Purpose lng neto is to check yung inputs ng users bago ipasok sa database.

`models.py`
-----------
- Implementation ng [ER-Diagram](https://dbdiagram.io/d/637688d1c9abfc611173801e)
- Nakaspecify na din dito yung mga values na kailangan maging consistent like yung colleges, departments, & employment type. So if may changes na gagawin eto lng need palitan.
