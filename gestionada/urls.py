from django.urls import path
from . import views

urlpatterns = [
    #URL del index
    path('user/', views.list_users),
    path('user/<str:username>/', views.mod_users),
    #path('register/', views.register),
    path('login/', views.loginvw, name='login'),
    path('user/subdelegacion/<str:username>/', views.subdelega_edit),
    path("delete/<str:username>/", views.delete_user),
]
