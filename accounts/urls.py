from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('change_password/', views.change_password, name='change_password'),
    path('<username>/profile/', views.profile, name='profile'),
    path('<int:pk>/follow/', views.follow, name='follow'),
]
