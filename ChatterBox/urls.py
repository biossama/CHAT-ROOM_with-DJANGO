from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name="home"),
	path('room/<int:pk>/', views.room, name="room"),
	path('profile/<int:pk>/', views.profileUser_view, name="profile"),
	path('room-create/', views.create_room, name="create_room"),
	path('room-update/<int:pk>/', views.update_room, name="update_room"),
	path('room-delete/<int:pk>/', views.delete_room, name="delete_room"),
  path('delete-message/<int:pk>/', views.roomRemove_comment, name='delete_message'),

]
