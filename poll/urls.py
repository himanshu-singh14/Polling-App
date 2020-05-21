from django.urls import path
from .views import *

urlpatterns = [
    path('', pollsList, name='polls-list'),
    # path('detail/<int:id>/', pollDetails, name='poll-details'),
    path('<int:id>/', poll, name='single-poll'),
]