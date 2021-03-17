from django.urls import path
from authe.views import author_form,confirm_email,login,logout_views

app_name='authe'

urlpatterns = [
     path("register/",author_form),
     path("confirm/<str:code>",confirm_email),
     path("login/",login,name="login"),
     path("logout/",logout_views)
]
