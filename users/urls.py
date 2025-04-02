
from django.urls import path
from django.contrib.auth import views as authViews

from .views import registration_view, LoginView


app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', registration_view, name='signup'),
    path('logout/', authViews.LogoutView.as_view(next_page='/'), name='logout'),
]
