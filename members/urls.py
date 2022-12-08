from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup_user, name='signup'),
    path('user_access', views.login_account, name='user-account'),
    path('logout_trial', views.trial_logout, name='trial_logout'),
]
