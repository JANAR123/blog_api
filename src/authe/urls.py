from django.urls import path
from authe.views import author_form,confirm_email


urlpatterns = [
     path("register/",author_form),
     path("confirm/<str:code>",confirm_email)
]
