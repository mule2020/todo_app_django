from django.urls import path
from . import views
urlpatterns = [
    path('about', views.about, name="about"),
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('index/', views.index, name="index"),
    path('update/<int:pk>/', views.updateTask, name="update"),
    path('delete/<int:pk>/', views.deleteTask, name="delete"),
]

