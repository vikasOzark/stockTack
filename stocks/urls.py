from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexHomeView.as_view(), name='index')
]

