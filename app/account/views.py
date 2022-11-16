from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout


# Ref 1: https://docs.djangoproject.com/en/4.1/topics/auth/default/#how-to-log-a-user-in
def login_user(request):

    # If user sumbitted via form
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # Redirect to a success page.
        if user is not None:
            login(request, user)
            return redirect('home')
        
        # Return an error message.
        else:
            messages.error(request, ("Incorrect email or password."))
            return redirect('login')

    # If user entered the website
    return render(request, 'account/login_user.html', {})


# Ref 1: https://docs.djangoproject.com/en/4.1/topics/auth/default/#how-to-log-a-user-out
def logout_user(request):
    logout(request)

    # Redirect to a success page.
    return redirect('home')
