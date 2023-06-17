from django.urls import path
from . import views
# from rest_framework_social_oauth2.views import TokenView

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    # path('auth/token/', TokenView.as_view(), name='token'),
]

