from django.urls import path
from .views import HomePageView, ListStoryView, CreatePostView, UpdatePostView, DeletePostview

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('list/create/', CreatePostView.as_view(), name='create'),
    path('list/<int:pk>/edit/', UpdatePostView.as_view(), name='edit'),
    path('list/<int:pk>/delete/', DeletePostview.as_view(), name='delete'),
    path('list/', ListStoryView.as_view(), name='story'),
]