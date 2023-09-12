from django.urls import path
from pssapp import views

#template tagging
app_name = 'pssapp'
urlpatterns = [
    path('register/' , views.register , name = 'register'),
    path("user_login/", views.user_login, name="user_login")
]
