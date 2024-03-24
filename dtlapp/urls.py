from django.urls import path
from . import views

urlpatterns = [
    path('abc/', views.dtlfun,name = 'homepageurl'),
    path('process/',views.processingdata,name = 'processurl'),
    path('home/,',views.templateFun,name='templateurl'),
    path('third/',views.thirdFun,name = 'thirdurl'),
]