from django.urls import path
from . import views

urlpatterns = [
    path('',views.mainone),
    path('members/', views.members, name='members'),
]