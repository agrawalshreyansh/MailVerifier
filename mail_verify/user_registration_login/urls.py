from django.urls import path
from . import views   
    
urlpatterns = [   
    path('', views.Register, name="Register"),
    path('verify', views.verify, name="verify" ),
    path('submit', views.submit, name="login"),
    path('login', views.login, name="entred")
]