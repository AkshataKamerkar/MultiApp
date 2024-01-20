from django.urls import path
from . import views

app_name = 'bot'

urlpatterns = [
    path('',views.home,name='home'),
    path('chatbot',views.index,name='index'),
    path('getResponse',views.getResponse,name='getResponse'),

]