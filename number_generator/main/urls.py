from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'),
    path('auth-cancelled/', views.auth_cancelled, name='auth_cancelled'),
]
