from django.urls import path
from .views import *


urlpatterns = [
    path('about/', vista_about),
    path('hobbies/', vista_hobbies),
]