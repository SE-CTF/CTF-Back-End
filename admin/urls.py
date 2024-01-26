from rest_framework.urls import path

from .views import UserList, UserDetail


urlpatterns = [
    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view())
]
