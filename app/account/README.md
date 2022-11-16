## Notes:
- `username` is the id number, may may id number nmn mga prof for sure. *- Jhaime*
- May pre-built urls na yung django (e.g. login) pero gagawa tayo ng saatin kasi may otp tayong ilalagay at baka email gusto nila pang login. For now yung **username/id number** nila muna gagamitin pang log in. Meron kasing ginawa yung django na db at may master list na dun, which is maganda pero medyo tricky yung pag modify ng table na yun. By default kasi `username` yung ginagamit sa `authenticate()` so parang kailan pa i-override yun kung `email` gagamitin. Check nlng ng `backends.py` nandun yung mga kailangan na info. *- Jhaime*

## Login (Possible) Plan:
- Probably gagawa ng panibagong table for prof & chairpersons, wala pa kasi ER so assume nlng natin hahaha. So sa mga table na yun lagyan nlng natin siguro ng `is_first_login` para ma prompt to change pasword agad kung first time. Pero baka sa master list nlng natin lagay kasi dodoble yung column at ayaw natin yun. *- Jhaime*

## TODO:
- [ ] Prompt new login a change password form (my function yung django dito)
- [ ] Add change password form (old user) w/ OTP form, for "reset password"
