from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.get_record, name='record'),
    path('record/update/<int:pk>', views.update_record, name='update_record'),
    path('record/delete/<int:pk>', views.delete_record, name='delete_record'),
    path('record/add/', views.add_record, name='add_record'),
]
