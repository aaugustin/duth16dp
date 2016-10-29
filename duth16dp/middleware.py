from django.contrib.auth import get_user_model


class AdminAutoLoginMiddleware():
    """
    Automatically creates and logs in a "test" user.

    Replaces ``django.contrib.auth.middleware.AuthenticationMiddleware``.

    Works with any admin-compliant user model i.e. subclass of AbstractUser.

    """
    USERNAME = 'test'

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        User = get_user_model()
        username_condition = {User.USERNAME_FIELD: self.USERNAME}
        try:
            user = User.objects.get(**username_condition)
        except User.DoesNotExist:
            user = User(**username_condition)
            user.is_staff = True
            user.is_superuser = True
            user.set_unusable_password()
            user.save()
        request.user = user

        return self.get_response(request)
