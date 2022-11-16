from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Ref 1: https://stackoverflow.com/questions/2245895/is-there-a-simple-way-to-get-group-names-of-a-user-in-django
@login_required(login_url='/account/login/')
def home(request):

    groups = request.user.groups

    # User have group (prof / chair)
    if groups.exists():
        if groups.filter(name='prof'):
            return render(request, 'home/prof.html', {})

        if groups.filter(name='chair'):
            return render(request, 'home/chair.html', {})

    # User don't have group (admin)
    return render(request, 'home/home.html', {})


@login_required
def prof(request):
    return render(request, 'home/prof.html', {})


@login_required
def chair(request):
    return render(request, 'home/chair.html', {})
