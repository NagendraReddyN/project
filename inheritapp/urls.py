from django.urls import path
from.import views

urlpatterns = [
    path('',views.homepage2, name = 'homeurl2')
]