# !!! NOT TESTED !!!
# Incase Email should be used to login (Same goes as the admin login)
# Ref 1 (working): https://stackoverflow.com/questions/37332190/django-login-with-email
# Ref 2 (query email): https://stackoverflow.com/questions/55940228/how-to-get-user-object-by-email-filtering-in-django
# Ref 3: https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#authentication-backends
# Note: 'AUTHENTICATION_BACKENDS' in the 'settings.py' should be commented out before using

# TODO:
# - [ ] Add doc string

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model


class MyBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email__exact=email)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None

