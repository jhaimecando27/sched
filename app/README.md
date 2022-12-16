Project layout
--------------

    ├─ account/         Manages the authentication (login, logout, password reset)
    ├─ app/             application settings (hindi nmn to gagalawin most of the time)
    ├─ main/            prof form & chairperson dashboard
    ├─ static/          css, js, & images
    └─ templates/       html files
----

`account/` and `main/` are both applications kaya parehas lng files nila from the start.

    └─ account/ or main/
       ├─ admin.py            nagamit para i-manage yung mga dapat makita ni admin sa page nila.
       ├─ apps.py             nagamit lng to para ma identify ni Django yung mga files nasa loob.
       ├─ models.py           database models, dahil dito pede tayo gumamit different kind of SQL
       ├─ tests.py            no idea, pero for sure for testing purposes
       ├─ urls.py             dito imamanage yung mga links
       └─ views.py            dito yung backend stuffs, mga implementation ganun.

yung mga files na hindi nyo makikita dito meaning hindi sya pre-made, kasi si Django kasi nag gegenerate ng mga to. So kami gumawa ng files na yun. Probably makikita yung yung:
- `forms.py` - form lng sya for the front-end para i-double check yung validation ng inputs, kasi pede kalkalin ni user yung page using inspect elements.

----
