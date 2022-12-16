`views.py`
----------
- `login_user`
    - By default may pre-made ng login page yung Django, pero gagawa tayo ng sarili natin kasi may possible na idagdagdag like pag change ng password for pre-made accounts.

`urls.py`
----------
- Sa password reset ginamit ko lng yung implementation ng Django meron na kasi, and yung babaguhin lng is yung UI kaya pinalitan ko lng yung `template_name`. Eto yung mga urls for password reset:
    - `password_reset/` - Dito need email para ma change yung password. Mag sesend lng ng link to change password.
    - `password_reset/done/` - Sasabihin lng yung result if na send na sa email
    - `reset/<uidb64>/<token>/` - Eto yung isesend sa email to change the password agad. `<uidb64>` yung user. `<token>` for security purposes.
    - `reset/done/` - Sasabihin yung result sa pag change ng password.

note
----
- Password reset (Security)
    - Onced nagamit na yung link na nasend sa email mag e-expire na agad sya. By mean of "nagamit" is na changed na yung password which is purpose ng link.
