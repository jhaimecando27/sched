from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from main.models import extendUser


# Ref 1: https://docs.djangoproject.com/en/4.1/topics/auth/default/#how-to-log-a-user-in
def login_user(request):

    # If user sumbitted via form
    if request.method == 'POST':

        # May sariling form yung django for login page
        # Gagamitin natin yun kasi naka ayos nmn na lahat dun
        # yung reference yung reason kung bat may 'data=request.POST'.
        # Form lang to for UI para i-double check yung inputs.
        # Ref: https://stackoverflow.com/questions/45824046/djangos-authentication-form-is-always-not-valid
        form = AuthenticationForm(data=request.POST)

        # I chcheck nga kung valid yung form. example sa html diba
        # nag lalagay lng ng required para hindi maging empty? so
        # dun sa form nila i dodouble check kung empty or not yung
        # input, kasi pede sila mag inspect element at tanggalin yung required
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            # Sa authenticate like hahanapin lng nya sa user table
            # kung may ganitong username at password
            user = authenticate(request, username=username, password=password)

            # Redirect to a success page.
            if user is not None:
                login(request, user)

                status = extendUser.objects.get(user=request.user.id)

                request.session['is_chairperson'] = status.is_chairperson
                request.session['is_professor'] = status.is_professor

                return redirect('main:profile')
                # return redirect('home')

            # Return an error message (Form is valid but credential is not).
            else:
                messages.error(request, ("Incorrect username or password."))

        # Return an error message (Form is not valid).
        else:
            messages.error(request, "Invalid username or password.")

    # UI form
    form = AuthenticationForm()

    # yung importanteng tandaan lng dito yung 2nd paramerter and last.
    # yung 2nd template lng yan, by default naturo na sya sa loob ng template folder
    # yung last parameter ipapasok natin yung form ng Django.
    return render(request, "account/login_user.html", {"form": form})


# Ref 1: https://docs.djangoproject.com/en/4.1/topics/auth/default/#how-to-log-a-user-out
def logout_user(request):
    logout(request)

    # Redirect to a success page.
    return redirect('main:profile')
