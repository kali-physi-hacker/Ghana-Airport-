from django.urls import path 

from users.views import login_user, sign_in, _logout


urlpatterns = [
    path('accounts/login/', login_user, name="login_user"),
    path('accounts/sign_in/', sign_in, name="sign_in"),
    path('accounts/logout/', _logout, name="_logout")
]
