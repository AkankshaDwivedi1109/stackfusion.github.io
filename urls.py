from django.urls import path
from . import views
urlpatterns = [
    path("home/",views.show,name="show"),
    path("data/",views.register, name="database"),
    path("data/contact",views.contact,name="contact")
    
]
    