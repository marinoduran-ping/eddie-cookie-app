from django.urls import path
from .views import * 

# URLConf
urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout')
]