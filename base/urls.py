from django.urls import path
from . import views

urlpatterns = [
	path('login/', views.loginUser, name="login"),
	path('logout/', views.logoutUser, name="logout"),
	path('register/', views.registerUser, name="register"),
	path('', views.home, name="home"),
	path('rooms/<str:pk>/', views.room, name="room"),
	path('profiles/<str:pk>/', views.userProfile, name="user-profile"),
	path('room/create/', views.createRoom, name="create-room"),
	path('rooms/update/<str:pk>/', views.updateRoom, name="update-room"),
	path('rooms/delete/<str:pk>/', views.deleteRoom, name="delete-room"),
	path('message/delete/<str:pk>/', views.deleteMessage, name="delete-message"),
	path('user/update/', views.updateUser, name="update-user"),
	path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
]